from datetime import datetime

import mysql.connector

from services.database import ket_noi


SO_DONG_MOI_TRANG = 20
CAC_LOAI_DU_LIEU = {"tat_ca", "ban_hang", "nhap_hang"}
CAC_TRANG_THAI = {"Chờ duyệt", "Đã duyệt", "Đã từ chối", "Từ chối"}


def _mo_cursor():
    db = ket_noi()
    try:
        cursor = db.cursor(dictionary=True)
    except mysql.connector.Error:
        db.close()
        raise
    return db, cursor


def _so_nguyen_duong(gia_tri, mac_dinh=None):
    if not isinstance(gia_tri, str) or not gia_tri.isascii() or not gia_tri.isdecimal():
        return mac_dinh
    so = int(gia_tri)
    return so if so > 0 else mac_dinh


def _lay_bo_loc(args):
    bo_loc = {
        "q": args.get("q", "").strip()[:100],
        "tu_ngay": args.get("tu_ngay", "").strip(),
        "den_ngay": args.get("den_ngay", "").strip(),
        "loai": args.get("loai", "tat_ca").strip(),
        "trang_thai": args.get("trang_thai", "").strip(),
        "ca_id": args.get("ca_id", "").strip(),
        "nhan_vien_id": args.get("nhan_vien_id", "").strip(),
        "nhien_lieu_id": args.get("nhien_lieu_id", "").strip(),
        "bon_id": args.get("bon_id", "").strip(),
    }
    loi_loc = None

    if bo_loc["loai"] not in CAC_LOAI_DU_LIEU:
        bo_loc["loai"] = "tat_ca"
        loi_loc = "Loại dữ liệu tra cứu không hợp lệ."
    if bo_loc["trang_thai"] and bo_loc["trang_thai"] not in CAC_TRANG_THAI:
        bo_loc["trang_thai"] = ""
        loi_loc = "Trạng thái giao dịch không hợp lệ."

    for truong in ("tu_ngay", "den_ngay"):
        if bo_loc[truong]:
            try:
                ngay = datetime.strptime(bo_loc[truong], "%Y-%m-%d")
                if ngay.strftime("%Y-%m-%d") != bo_loc[truong]:
                    raise ValueError
            except ValueError:
                loi_loc = "Ngày tra cứu không hợp lệ."

    if (
        bo_loc["tu_ngay"]
        and bo_loc["den_ngay"]
        and bo_loc["tu_ngay"] > bo_loc["den_ngay"]
    ):
        loi_loc = "Ngày bắt đầu không được sau ngày kết thúc."

    for truong in ("ca_id", "nhan_vien_id", "nhien_lieu_id", "bon_id"):
        if bo_loc[truong] and _so_nguyen_duong(bo_loc[truong]) is None:
            loi_loc = "Điều kiện lọc không hợp lệ."
            bo_loc[truong] = ""

    return bo_loc, loi_loc


def _dieu_kien(loai, bo_loc, chi_tinh_da_duyet=False):
    alias = "bh" if loai == "ban_hang" else "nh"
    truong_ngay = "ngay_ban" if loai == "ban_hang" else "ngay_tao"
    dieu_kien = ["1 = 1"]
    tham_so = []

    if bo_loc["q"]:
        truong_ma = "ma_ban" if loai == "ban_hang" else "ma_nhap"
        dieu_kien.append(f"{alias}.{truong_ma} LIKE %s")
        tham_so.append(f"%{bo_loc['q']}%")
    if bo_loc["tu_ngay"]:
        dieu_kien.append(f"{alias}.{truong_ngay} >= %s")
        tham_so.append(bo_loc["tu_ngay"])
    if bo_loc["den_ngay"]:
        dieu_kien.append(f"{alias}.{truong_ngay} <= %s")
        tham_so.append(bo_loc["den_ngay"])
    if bo_loc["nhan_vien_id"]:
        dieu_kien.append(f"{alias}.nhan_vien_id = %s")
        tham_so.append(int(bo_loc["nhan_vien_id"]))
    if bo_loc["nhien_lieu_id"]:
        dieu_kien.append(f"{alias}.nhien_lieu_id = %s")
        tham_so.append(int(bo_loc["nhien_lieu_id"]))
    if bo_loc["bon_id"]:
        dieu_kien.append(f"{alias}.bon_id = %s")
        tham_so.append(int(bo_loc["bon_id"]))

    if loai == "ban_hang" and bo_loc["ca_id"]:
        dieu_kien.append("bh.ca_lam_viec_id = %s")
        tham_so.append(int(bo_loc["ca_id"]))

    trang_thai = bo_loc["trang_thai"]
    trang_thai_hop_le = {
        "ban_hang": {"Chờ duyệt", "Đã duyệt", "Đã từ chối"},
        "nhap_hang": {"Chờ duyệt", "Đã duyệt", "Từ chối"},
    }[loai]
    if trang_thai:
        if trang_thai in trang_thai_hop_le:
            dieu_kien.append(f"{alias}.trang_thai = %s")
            tham_so.append(trang_thai)
        else:
            dieu_kien.append("1 = 0")

    if chi_tinh_da_duyet:
        dieu_kien.append(f"{alias}.trang_thai = %s")
        tham_so.append("Đã duyệt")

    return " AND ".join(dieu_kien), tham_so


def _lay_tuy_chon(cursor):
    tuy_chon = {}
    for ten, sql in (
        (
            "ca_lam_viec",
            "SELECT id, ma_ca, ten_ca, ngay_lam_viec FROM ca_lam_viec ORDER BY ngay_lam_viec DESC, id DESC",
        ),
        (
            "nhan_vien",
            "SELECT id, ma_nv, ho_ten FROM nhan_vien ORDER BY ho_ten, id",
        ),
        (
            "nhien_lieu",
            "SELECT id, ma_nhien_lieu, ten_nhien_lieu, don_vi FROM nhien_lieu ORDER BY ten_nhien_lieu, id",
        ),
        (
            "bon_chua",
            "SELECT id, ma_bon, ten_bon FROM bon_chua ORDER BY ma_bon, id",
        ),
    ):
        cursor.execute(sql)
        tuy_chon[ten] = cursor.fetchall()
    return tuy_chon


def _lay_thong_ke(cursor, loai, bo_loc):
    where_sql, params = _dieu_kien(loai, bo_loc, chi_tinh_da_duyet=True)
    alias = "bh" if loai == "ban_hang" else "nh"
    bang = "ban_hang" if loai == "ban_hang" else "nhap_hang"
    cursor.execute(
        f"""
        SELECT nl.don_vi, COALESCE(SUM({alias}.so_luong), 0) AS so_luong
        FROM {bang} {alias}
        JOIN nhien_lieu nl ON nl.id = {alias}.nhien_lieu_id
        WHERE {where_sql}
        GROUP BY nl.don_vi
        ORDER BY nl.don_vi
        """,
        tuple(params),
    )
    so_luong_theo_don_vi = cursor.fetchall()

    cursor.execute(
        f"""
        SELECT COUNT(*) AS tong_so
        FROM {bang} {alias}
        WHERE {where_sql}
        """,
        tuple(params),
    )
    so_giao_dich = cursor.fetchone()["tong_so"]

    tong_tien = None
    if loai == "ban_hang":
        where_sql, params = _dieu_kien(loai, bo_loc, chi_tinh_da_duyet=True)
        cursor.execute(
            f"""
            SELECT COALESCE(SUM(bh.thanh_tien), 0) AS tong_tien
            FROM ban_hang bh
            WHERE {where_sql}
            """,
            tuple(params),
        )
        tong_tien = cursor.fetchone()["tong_tien"]

    return {
        "so_luong_theo_don_vi": so_luong_theo_don_vi,
        "so_giao_dich": so_giao_dich,
        "tong_tien": tong_tien,
    }


def _lay_danh_sach(cursor, loai, bo_loc, trang):
    where_sql, params = _dieu_kien(loai, bo_loc)
    alias = "bh" if loai == "ban_hang" else "nh"
    bang = "ban_hang" if loai == "ban_hang" else "nhap_hang"
    cursor.execute(
        f"SELECT COUNT(*) AS tong_so FROM {bang} {alias} WHERE {where_sql}",
        tuple(params),
    )
    tong_so = cursor.fetchone()["tong_so"]
    tong_trang = max(
        1,
        (tong_so + SO_DONG_MOI_TRANG - 1) // SO_DONG_MOI_TRANG,
    )
    trang = min(trang, tong_trang)
    offset = (trang - 1) * SO_DONG_MOI_TRANG

    if loai == "ban_hang":
        sql = f"""
            SELECT
                bh.id, bh.ma_ban AS ma_giao_dich, bh.ngay_ban AS ngay,
                bh.gio_ban AS gio, bh.so_luong, bh.don_gia, bh.thanh_tien,
                bh.trang_thai, ca.ma_ca, ca.ten_ca, nv.ma_nv, nv.ho_ten,
                nl.ten_nhien_lieu, nl.don_vi, bc.ma_bon, bc.ten_bon
            FROM ban_hang bh
            JOIN ca_lam_viec ca ON ca.id = bh.ca_lam_viec_id
            JOIN nhan_vien nv ON nv.id = bh.nhan_vien_id
            JOIN nhien_lieu nl ON nl.id = bh.nhien_lieu_id
            JOIN bon_chua bc ON bc.id = bh.bon_id
            WHERE {where_sql}
            ORDER BY bh.ngay_ban DESC, bh.gio_ban DESC, bh.id DESC
            LIMIT %s OFFSET %s
        """
    else:
        sql = f"""
            SELECT
                nh.id, nh.ma_nhap AS ma_giao_dich, nh.ngay_tao AS ngay,
                NULL AS gio, nh.so_luong, NULL AS don_gia,
                NULL AS thanh_tien, nh.trang_thai, NULL AS ma_ca,
                NULL AS ten_ca, nv.ma_nv, nv.ho_ten, nl.ten_nhien_lieu,
                nl.don_vi, bc.ma_bon, bc.ten_bon
            FROM nhap_hang nh
            JOIN nhan_vien nv ON nv.id = nh.nhan_vien_id
            JOIN nhien_lieu nl ON nl.id = nh.nhien_lieu_id
            JOIN bon_chua bc ON bc.id = nh.bon_id
            WHERE {where_sql}
            ORDER BY nh.ngay_tao DESC, nh.id DESC
            LIMIT %s OFFSET %s
        """
    cursor.execute(sql, tuple(params + [SO_DONG_MOI_TRANG, offset]))

    return {
        "danh_sach": cursor.fetchall(),
        "tong_so": tong_so,
        "trang": trang,
        "tong_trang": tong_trang,
    }


def lay_trang_tra_cuu(args):
    bo_loc, loi_loc = _lay_bo_loc(args)
    trang_ban = _so_nguyen_duong(args.get("page_ban", "1"), 1)
    trang_nhap = _so_nguyen_duong(args.get("page_nhap", "1"), 1)
    db, cursor = _mo_cursor()
    try:
        tuy_chon = _lay_tuy_chon(cursor)
        don_vi_duoc_chon = next(
            (
                nl["don_vi"]
                for nl in tuy_chon["nhien_lieu"]
                if str(nl["id"]) == bo_loc["nhien_lieu_id"]
            ),
            None,
        )
        cac_don_vi = {nl["don_vi"] for nl in tuy_chon["nhien_lieu"]}
        thong_ke = {
            "ban_hang": {
                "so_luong_theo_don_vi": [],
                "so_giao_dich": 0,
                "tong_tien": 0,
            },
            "nhap_hang": {
                "so_luong_theo_don_vi": [],
                "so_giao_dich": 0,
                "tong_tien": None,
            },
        }
        danh_sach = {
            "ban_hang": {"danh_sach": [], "tong_so": 0, "trang": 1, "tong_trang": 1},
            "nhap_hang": {"danh_sach": [], "tong_so": 0, "trang": 1, "tong_trang": 1},
        }

        if not loi_loc:
            cac_loai = (
                ("ban_hang", "nhap_hang")
                if bo_loc["loai"] == "tat_ca"
                else (bo_loc["loai"],)
            )
            for loai in cac_loai:
                thong_ke[loai] = _lay_thong_ke(cursor, loai, bo_loc)
                trang = trang_ban if loai == "ban_hang" else trang_nhap
                danh_sach[loai] = _lay_danh_sach(
                    cursor,
                    loai,
                    bo_loc,
                    trang,
                )

        return {
            "filters": bo_loc,
            "loi_loc": loi_loc,
            "tuy_chon": tuy_chon,
            "don_vi_mac_dinh": don_vi_duoc_chon or (
                next(iter(cac_don_vi)) if len(cac_don_vi) == 1 else ""
            ),
            "thong_ke": thong_ke,
            "ban_hang": danh_sach["ban_hang"],
            "nhap_hang": danh_sach["nhap_hang"],
            "so_dong_moi_trang": SO_DONG_MOI_TRANG,
        }
    finally:
        cursor.close()
        db.close()


def lay_chi_tiet(loai, id):
    if loai not in {"ban_hang", "nhap_hang"}:
        return None

    db, cursor = _mo_cursor()
    try:
        if loai == "ban_hang":
            cursor.execute(
                """
                SELECT
                    bh.id, bh.ma_ban AS ma_giao_dich, bh.ngay_ban AS ngay,
                    bh.gio_ban AS gio, bh.so_luong, bh.don_gia,
                    bh.thanh_tien, bh.ghi_chu, bh.trang_thai,
                    ca.ma_ca, ca.ten_ca, nv.ma_nv, nv.ho_ten,
                    nl.ma_nhien_lieu, nl.ten_nhien_lieu, nl.don_vi,
                    bc.ma_bon, bc.ten_bon
                FROM ban_hang bh
                JOIN ca_lam_viec ca ON ca.id = bh.ca_lam_viec_id
                JOIN nhan_vien nv ON nv.id = bh.nhan_vien_id
                JOIN nhien_lieu nl ON nl.id = bh.nhien_lieu_id
                JOIN bon_chua bc ON bc.id = bh.bon_id
                WHERE bh.id = %s
                """,
                (id,),
            )
        else:
            cursor.execute(
                """
                SELECT
                    nh.id, nh.ma_nhap AS ma_giao_dich, nh.ngay_tao AS ngay,
                    NULL AS gio, nh.so_luong, NULL AS don_gia,
                    NULL AS thanh_tien, NULL AS ghi_chu, nh.trang_thai,
                    NULL AS ma_ca, NULL AS ten_ca, nv.ma_nv, nv.ho_ten,
                    nl.ma_nhien_lieu, nl.ten_nhien_lieu, nl.don_vi,
                    bc.ma_bon, bc.ten_bon
                FROM nhap_hang nh
                JOIN nhan_vien nv ON nv.id = nh.nhan_vien_id
                JOIN nhien_lieu nl ON nl.id = nh.nhien_lieu_id
                JOIN bon_chua bc ON bc.id = nh.bon_id
                WHERE nh.id = %s
                """,
                (id,),
            )
        giao_dich = cursor.fetchone()
        if giao_dich is not None:
            giao_dich["loai"] = loai
        return giao_dich
    finally:
        cursor.close()
        db.close()
