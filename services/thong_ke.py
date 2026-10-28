from datetime import date, datetime, timedelta

import mysql.connector

from services.database import ket_noi
from services.ton_bon import NGUONG_BON_GAN_HET, lay_du_lieu_ton_bon
from services.tra_cuu import lay_chi_tiet


CAC_KHOANG_THOI_GIAN = {
    "hom_nay": "Hôm nay",
    "7_ngay": "7 ngày gần nhất",
    "30_ngay": "30 ngày gần nhất",
    "thang_nay": "Tháng này",
    "tuy_chinh": "Khoảng thời gian tùy chọn",
}


def _mo_cursor():
    db = ket_noi()
    try:
        cursor = db.cursor(dictionary=True)
    except mysql.connector.Error:
        db.close()
        raise
    return db, cursor


def _lay_khoang_thoi_gian(args, hom_nay=None):
    hom_nay = hom_nay or date.today()
    loai_khoang = args.get("khoang", "7_ngay").strip()
    if loai_khoang not in CAC_KHOANG_THOI_GIAN:
        loai_khoang = "7_ngay"

    ngay_tu = ngay_den = None
    loi_loc = None
    if loai_khoang == "hom_nay":
        ngay_tu = ngay_den = hom_nay
    elif loai_khoang == "7_ngay":
        ngay_tu, ngay_den = hom_nay - timedelta(days=6), hom_nay
    elif loai_khoang == "30_ngay":
        ngay_tu, ngay_den = hom_nay - timedelta(days=29), hom_nay
    elif loai_khoang == "thang_nay":
        ngay_tu, ngay_den = hom_nay.replace(day=1), hom_nay
    else:
        try:
            ngay_tu = date.fromisoformat(args.get("tu_ngay", ""))
            ngay_den = date.fromisoformat(args.get("den_ngay", ""))
            if ngay_tu.isoformat() != args.get("tu_ngay") or ngay_den.isoformat() != args.get("den_ngay"):
                raise ValueError
            if ngay_tu > ngay_den:
                loi_loc = "Ngày bắt đầu không được sau ngày kết thúc."
        except ValueError:
            loi_loc = "Vui lòng chọn khoảng ngày hợp lệ."

    if ngay_tu and ngay_den and (ngay_den - ngay_tu).days > 3650:
        loi_loc = "Khoảng thời gian không được vượt quá 10 năm."

    return {
        "khoang": loai_khoang,
        "tu_ngay": ngay_tu.isoformat() if ngay_tu else args.get("tu_ngay", ""),
        "den_ngay": ngay_den.isoformat() if ngay_den else args.get("den_ngay", ""),
        "nhan_khoang": CAC_KHOANG_THOI_GIAN[loai_khoang],
        "loi_loc": loi_loc,
        "ngay_hien_tai": hom_nay,
    }


def _lay_thong_ke_giao_dich(cursor, ten_bang, alias, ten_ngay, ngay_tu, ngay_den):
    cursor.execute(
        f"""
        SELECT
            COUNT(*) AS so_giao_dich,
            COALESCE(SUM({alias}.so_luong), 0) AS tong_so_luong
            {", COALESCE(SUM(" + alias + ".thanh_tien), 0) AS tong_tien" if ten_bang == "ban_hang" else ""}
        FROM {ten_bang} {alias}
        WHERE {alias}.trang_thai = %s
          AND {alias}.{ten_ngay} >= %s
          AND {alias}.{ten_ngay} <= %s
        """,
        ("Đã duyệt", ngay_tu, ngay_den),
    )
    return cursor.fetchone()


def _lay_theo_don_vi(cursor, ten_bang, alias, ten_ngay, ngay_tu, ngay_den):
    cursor.execute(
        f"""
        SELECT nl.don_vi, COALESCE(SUM({alias}.so_luong), 0) AS so_luong
        FROM {ten_bang} {alias}
        JOIN nhien_lieu nl ON nl.id = {alias}.nhien_lieu_id
        WHERE {alias}.trang_thai = %s
          AND {alias}.{ten_ngay} >= %s
          AND {alias}.{ten_ngay} <= %s
        GROUP BY nl.don_vi
        ORDER BY nl.don_vi
        """,
        ("Đã duyệt", ngay_tu, ngay_den),
    )
    return cursor.fetchall()


def _lay_chuoi_thoi_gian(cursor, ten_bang, alias, ten_ngay, ngay_tu, ngay_den, dinh_dang):
    cursor.execute(
        f"""
        SELECT
            DATE_FORMAT({alias}.{ten_ngay}, %s) AS ky,
            nl.don_vi,
            COALESCE(SUM({alias}.so_luong), 0) AS so_luong
            {", COALESCE(SUM(" + alias + ".thanh_tien), 0) AS doanh_thu" if ten_bang == "ban_hang" else ""}
        FROM {ten_bang} {alias}
        JOIN nhien_lieu nl ON nl.id = {alias}.nhien_lieu_id
        WHERE {alias}.trang_thai = %s
          AND {alias}.{ten_ngay} >= %s
          AND {alias}.{ten_ngay} <= %s
        GROUP BY ky, nl.don_vi
        ORDER BY ky, nl.don_vi
        """,
        (dinh_dang, "Đã duyệt", ngay_tu, ngay_den),
    )
    return cursor.fetchall()


def _lay_doanh_thu_theo_ky(cursor, ngay_tu, ngay_den, dinh_dang):
    cursor.execute(
        """
        SELECT
            DATE_FORMAT(bh.ngay_ban, %s) AS ky,
            COALESCE(SUM(bh.thanh_tien), 0) AS doanh_thu
        FROM ban_hang bh
        WHERE bh.trang_thai = %s
          AND bh.ngay_ban >= %s
          AND bh.ngay_ban <= %s
        GROUP BY ky
        ORDER BY ky
        """,
        (dinh_dang, "Đã duyệt", ngay_tu, ngay_den),
    )
    return cursor.fetchall()


def _lay_co_cau_nhien_lieu(cursor, ngay_tu, ngay_den):
    cursor.execute(
        """
        SELECT
            nl.ten_nhien_lieu,
            nl.don_vi,
            COALESCE(SUM(bh.so_luong), 0) AS so_luong
        FROM ban_hang bh
        JOIN nhien_lieu nl ON nl.id = bh.nhien_lieu_id
        WHERE bh.trang_thai = %s
          AND bh.ngay_ban >= %s
          AND bh.ngay_ban <= %s
        GROUP BY nl.id, nl.ten_nhien_lieu, nl.don_vi
        ORDER BY nl.ten_nhien_lieu
        """,
        ("Đã duyệt", ngay_tu, ngay_den),
    )
    return cursor.fetchall()


def _lay_giao_dich_gan_day(cursor, ten_bang):
    if ten_bang == "ban_hang":
        cursor.execute(
            """
            SELECT
                bh.id, bh.ma_ban AS ma_giao_dich, 'ban_hang' AS loai,
                bh.ngay_ban AS ngay, bh.gio_ban AS gio, nv.ho_ten,
                nl.ten_nhien_lieu, nl.don_vi, bh.so_luong, bh.thanh_tien,
                bh.trang_thai
            FROM ban_hang bh
            JOIN nhan_vien nv ON nv.id = bh.nhan_vien_id
            JOIN nhien_lieu nl ON nl.id = bh.nhien_lieu_id
            ORDER BY bh.ngay_ban DESC, bh.gio_ban DESC, bh.id DESC
            LIMIT 8
            """
        )
    else:
        cursor.execute(
            """
            SELECT
                nh.id, nh.ma_nhap AS ma_giao_dich, 'nhap_hang' AS loai,
                nh.ngay_tao AS ngay, NULL AS gio, nv.ho_ten,
                nl.ten_nhien_lieu, nl.don_vi, nh.so_luong,
                NULL AS thanh_tien, nh.trang_thai
            FROM nhap_hang nh
            JOIN nhan_vien nv ON nv.id = nh.nhan_vien_id
            JOIN nhien_lieu nl ON nl.id = nh.nhien_lieu_id
            ORDER BY nh.ngay_tao DESC, nh.id DESC
            LIMIT 8
            """
        )
    return cursor.fetchall()


def _tao_bieu_do(ngay_tu, ngay_den, doanh_thu, chuoi_ban, chuoi_nhap, co_cau):
    so_ngay = (ngay_den - ngay_tu).days
    dinh_dang = "%Y-%m-%d" if so_ngay <= 31 else "%Y-%m"
    if so_ngay <= 31:
        cac_ky = [
            (ngay_tu + timedelta(days=offset)).strftime("%Y-%m-%d")
            for offset in range(so_ngay + 1)
        ]
        nhan_ky = {
            ky: datetime.strptime(ky, "%Y-%m-%d").strftime("%d/%m")
            for ky in cac_ky
        }
    else:
        cac_ky = []
        cursor_thang = ngay_tu.replace(day=1)
        while cursor_thang <= ngay_den:
            ky = cursor_thang.strftime("%Y-%m")
            cac_ky.append(ky)
            if cursor_thang.month == 12:
                cursor_thang = cursor_thang.replace(
                    year=cursor_thang.year + 1,
                    month=1,
                )
            else:
                cursor_thang = cursor_thang.replace(month=cursor_thang.month + 1)
        nhan_ky = {
            ky: datetime.strptime(ky, "%Y-%m").strftime("%m/%Y")
            for ky in cac_ky
        }

    doanh_thu_theo_ky = {row["ky"]: row["doanh_thu"] for row in doanh_thu}
    cac_don_vi = sorted(
        {row["don_vi"] for row in chuoi_ban}
        | {row["don_vi"] for row in chuoi_nhap}
    )
    chuoi_theo_don_vi = []
    for don_vi in cac_don_vi:
        ban = {
            row["ky"]: row["so_luong"]
            for row in chuoi_ban
            if row["don_vi"] == don_vi
        }
        nhap = {
            row["ky"]: row["so_luong"]
            for row in chuoi_nhap
            if row["don_vi"] == don_vi
        }
        cac_ky_du_lieu = [
            {
                "ky": ky,
                "nhan": nhan_ky[ky],
                "so_luong_ban": ban.get(ky, 0),
                "so_luong_nhap": nhap.get(ky, 0),
            }
            for ky in cac_ky
        ]
        max_san_luong = max(
            (
                max(item["so_luong_ban"], item["so_luong_nhap"])
                for item in cac_ky_du_lieu
            ),
            default=0,
        )
        for item in cac_ky_du_lieu:
            item["ty_le_ban"] = (
                item["so_luong_ban"] / max_san_luong * 100
                if max_san_luong
                else 0
            )
            item["ty_le_nhap"] = (
                item["so_luong_nhap"] / max_san_luong * 100
                if max_san_luong
                else 0
            )
        chuoi_theo_don_vi.append(
            {
                "don_vi": don_vi,
                "cac_ky": cac_ky_du_lieu,
            }
        )

    doanh_thu_values = [doanh_thu_theo_ky.get(ky, 0) for ky in cac_ky]
    max_doanh_thu = max(doanh_thu_values, default=0)
    max_co_cau = {}
    for hang in co_cau:
        max_co_cau[hang["don_vi"]] = max(
            max_co_cau.get(hang["don_vi"], 0),
            hang["so_luong"],
        )
    for hang in co_cau:
        max_don_vi = max_co_cau[hang["don_vi"]]
        hang["ty_le"] = (
            hang["so_luong"] / max_don_vi * 100 if max_don_vi else 0
        )

    return {
        "doanh_thu": [
            {
                "ky": ky,
                "nhan": nhan_ky[ky],
                "gia_tri": doanh_thu_theo_ky.get(ky, 0),
                "ty_le": (
                    doanh_thu_theo_ky.get(ky, 0) / max_doanh_thu * 100
                    if max_doanh_thu
                    else 0
                ),
            }
            for ky in cac_ky
        ],
        "co_cau_nhien_lieu": co_cau,
        "so_sanh_san_luong": chuoi_theo_don_vi,
        "dinh_dang": dinh_dang,
    }


def lay_du_lieu_thong_ke(args):
    khoang = _lay_khoang_thoi_gian(args)
    ngay_tu = date.fromisoformat(khoang["tu_ngay"]) if not khoang["loi_loc"] else None
    ngay_den = date.fromisoformat(khoang["den_ngay"]) if not khoang["loi_loc"] else None
    ket_noi_db, cursor = _mo_cursor()
    try:
        if khoang["loi_loc"]:
            return {
                "khoang": khoang,
                "kpi": {},
                "bieu_do": {},
                "bon_chua": [],
                "thong_ke_bon": {},
                "giao_dich_gan_day": [],
                "canh_bao": [],
                "nguong_bon_gan_het": NGUONG_BON_GAN_HET,
            }

        bat_dau_sql = ngay_tu.isoformat()
        ket_thuc_sql = ngay_den.isoformat()
        ban_hang = _lay_thong_ke_giao_dich(
            cursor, "ban_hang", "bh", "ngay_ban", bat_dau_sql, ket_thuc_sql
        )
        nhap_hang = _lay_thong_ke_giao_dich(
            cursor, "nhap_hang", "nh", "ngay_tao", bat_dau_sql, ket_thuc_sql
        )
        luong_ban = _lay_theo_don_vi(
            cursor, "ban_hang", "bh", "ngay_ban", bat_dau_sql, ket_thuc_sql
        )
        luong_nhap = _lay_theo_don_vi(
            cursor, "nhap_hang", "nh", "ngay_tao", bat_dau_sql, ket_thuc_sql
        )

        cursor.execute(
            """
            SELECT COUNT(*) AS so_cho_duyet
            FROM ban_hang
            WHERE trang_thai = %s
            """,
            ("Chờ duyệt",),
        )
        cho_duyet_ban = cursor.fetchone()["so_cho_duyet"]
        cursor.execute(
            """
            SELECT COUNT(*) AS so_cho_duyet
            FROM nhap_hang
            WHERE trang_thai = %s
            """,
            ("Chờ duyệt",),
        )
        cho_duyet_nhap = cursor.fetchone()["so_cho_duyet"]

        dinh_dang = "%Y-%m-%d" if (ngay_den - ngay_tu).days <= 31 else "%Y-%m"
        doanh_thu_theo_ky = _lay_doanh_thu_theo_ky(
            cursor, bat_dau_sql, ket_thuc_sql, dinh_dang
        )
        chuoi_ban = _lay_chuoi_thoi_gian(
            cursor, "ban_hang", "bh", "ngay_ban", bat_dau_sql, ket_thuc_sql, dinh_dang
        )
        chuoi_nhap = _lay_chuoi_thoi_gian(
            cursor, "nhap_hang", "nh", "ngay_tao", bat_dau_sql, ket_thuc_sql, dinh_dang
        )
        co_cau = _lay_co_cau_nhien_lieu(cursor, bat_dau_sql, ket_thuc_sql)

        bon_data = lay_du_lieu_ton_bon()
        bon_chua = bon_data["danh_sach_bon"]
        giao_dich_gan_day = (
            _lay_giao_dich_gan_day(cursor, "ban_hang")
            + _lay_giao_dich_gan_day(cursor, "nhap_hang")
        )
        giao_dich_gan_day.sort(
            key=lambda item: (
                item["ngay"],
                str(item.get("gio") or ""),
                item["id"],
            ),
            reverse=True,
        )
        giao_dich_gan_day = giao_dich_gan_day[:10]

        don_vi_bon = {
            item.get("don_vi")
            for item in bon_chua
            if item.get("don_vi")
        }
        tong_suc_chua = sum(
            item["suc_chua_tinh"]
            for item in bon_chua
            if item["suc_chua_tinh"] is not None
        )
        tong_ton = sum(
            item["ton_hien_tai_tinh"]
            for item in bon_chua
            if item["ton_hien_tai_tinh"] is not None
        )
        ty_le_su_dung = (
            tong_ton / tong_suc_chua * 100
            if len(don_vi_bon) == 1 and tong_suc_chua > 0
            else None
        )
        thong_ke_bon = {
            "tong_so": len(bon_chua),
            "dang_hoat_dong": sum(
                item["trang_thai"] == "Đang hoạt động" for item in bon_chua
            ),
            "ngung_hoat_dong": sum(
                item["trang_thai"] != "Đang hoạt động" for item in bon_chua
            ),
            "ty_le_su_dung": ty_le_su_dung,
            "don_vi": next(iter(don_vi_bon)) if len(don_vi_bon) == 1 else "",
        }
        canh_bao = []
        if cho_duyet_ban + cho_duyet_nhap:
            canh_bao.append(
                {
                    "muc_do": "can-chu-y",
                    "tieu_de": "Giao dịch đang chờ duyệt",
                    "mo_ta": (
                        f"{cho_duyet_ban} phiếu bán và {cho_duyet_nhap} phiếu nhập "
                        "cần được xem xét."
                    ),
                    "url": None,
                    "loai": "giao_dich",
                }
            )
        for bon in bon_chua:
            if bon["du_lieu_bat_thuong"]:
                canh_bao.append(
                    {
                        "muc_do": "canh-bao",
                        "tieu_de": f"Dữ liệu bồn {bon['ma_bon']} bất thường",
                        "mo_ta": bon["ten_bon"],
                        "url": None,
                        "loai": "bon",
                        "bon_id": bon["id"],
                    }
                )
            elif bon["trang_thai"] == "Đang hoạt động" and bon["bon_gan_het"]:
                canh_bao.append(
                    {
                        "muc_do": "can-chu-y",
                        "tieu_de": f"Bồn {bon['ma_bon']} tồn thấp",
                        "mo_ta": (
                            f"{bon['ten_bon']} còn "
                            f"{bon['ty_le_lap_day']:.1f}% sức chứa."
                        ),
                        "url": None,
                        "loai": "bon",
                        "bon_id": bon["id"],
                    }
                )

        return {
            "khoang": khoang,
            "kpi": {
                "doanh_thu": ban_hang["tong_tien"],
                "luong_ban": luong_ban,
                "luong_nhap": luong_nhap,
                "so_giao_dich_ban": ban_hang["so_giao_dich"],
                "so_giao_dich_nhap": nhap_hang["so_giao_dich"],
                "cho_duyet_ban": cho_duyet_ban,
                "cho_duyet_nhap": cho_duyet_nhap,
                "tong_cho_duyet": cho_duyet_ban + cho_duyet_nhap,
            },
            "bieu_do": _tao_bieu_do(
                ngay_tu,
                ngay_den,
                doanh_thu_theo_ky,
                chuoi_ban,
                chuoi_nhap,
                co_cau,
            ),
            "bon_chua": bon_chua,
            "thong_ke_bon": thong_ke_bon,
            "giao_dich_gan_day": giao_dich_gan_day,
            "canh_bao": canh_bao,
            "nguong_bon_gan_het": NGUONG_BON_GAN_HET,
        }
    finally:
        cursor.close()
        ket_noi_db.close()


def lay_chi_tiet_giao_dich(loai_giao_dich, id):
    return lay_chi_tiet(loai_giao_dich, id)
