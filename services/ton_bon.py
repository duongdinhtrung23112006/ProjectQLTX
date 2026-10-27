import mysql.connector

from services.database import ket_noi


NGUONG_BON_GAN_HET = 20


def _mo_cursor():
    ket_noi_db = ket_noi()
    try:
        cursor = ket_noi_db.cursor(dictionary=True)
    except mysql.connector.Error:
        ket_noi_db.close()
        raise
    return ket_noi_db, cursor


def _so_nguyen(gia_tri):
    try:
        so = int(gia_tri)
    except (TypeError, ValueError, OverflowError):
        return None
    return so


def _tinh_thong_tin_bon(bon):
    suc_chua = _so_nguyen(bon["suc_chua"])
    ton_hien_tai = _so_nguyen(bon["ton_hien_tai"])
    du_lieu_bat_thuong = (
        suc_chua is None
        or ton_hien_tai is None
        or suc_chua <= 0
        or ton_hien_tai < 0
        or ton_hien_tai > suc_chua
    )

    dung_tich_con = (
        suc_chua - ton_hien_tai
        if suc_chua is not None and ton_hien_tai is not None
        else None
    )
    ty_le_lap_day = (
        ton_hien_tai / suc_chua * 100
        if suc_chua is not None and suc_chua > 0 and ton_hien_tai is not None
        else None
    )
    
    # Kiểm tra gần hết (dưới hoặc bằng 20%) và kiểm tra cạn kiệt (bằng 0)
    bon_gan_het = (
        not du_lieu_bat_thuong
        and ty_le_lap_day is not None
        and ty_le_lap_day <= NGUONG_BON_GAN_HET
        and ton_hien_tai > 0
    )
    
    bon_het_hang = (
        not du_lieu_bat_thuong
        and ton_hien_tai is not None
        and ton_hien_tai == 0
    )

    ty_le_thanh_tien_trinh = (
        min(max(ty_le_lap_day, 0), 100)
        if ty_le_lap_day is not None
        else 0
    )

    return {
        **bon,
        "suc_chua_tinh": suc_chua,
        "ton_hien_tai_tinh": ton_hien_tai,
        "dung_tich_con": dung_tich_con,
        "ty_le_lap_day": ty_le_lap_day,
        "ty_le_thanh_tien_trinh": ty_le_thanh_tien_trinh,
        "du_lieu_bat_thuong": du_lieu_bat_thuong,
        "bon_gan_het": bon_gan_het,
        "bon_het_hang": bon_het_hang,
    }


def lay_du_lieu_ton_bon(tu_khoa="", nhien_lieu_id="", trang_thai=""):
    ket_noi_db, cursor = _mo_cursor()

    try:
        cursor.execute(
            """
            SELECT
                bc.id,
                bc.ma_bon,
                bc.ten_bon,
                bc.nhien_lieu_id,
                bc.suc_chua,
                bc.ton_hien_tai,
                bc.trang_thai,
                nl.ma_nhien_lieu,
                nl.ten_nhien_lieu,
                nl.don_vi
            FROM bon_chua bc
            JOIN nhien_lieu nl
                ON nl.id = bc.nhien_lieu_id
            ORDER BY
                CAST(SUBSTRING(bc.ma_bon, 3) AS UNSIGNED),
                bc.ma_bon
            """
        )
        tat_ca_bon = [
            _tinh_thong_tin_bon(bon)
            for bon in cursor.fetchall()
        ]
    finally:
        cursor.close()
        ket_noi_db.close()

    tong_suc_chua = sum(
        bon["suc_chua_tinh"]
        for bon in tat_ca_bon
        if bon["suc_chua_tinh"] is not None
    )
    tong_ton_hien_tai = sum(
        bon["ton_hien_tai_tinh"]
        for bon in tat_ca_bon
        if bon["ton_hien_tai_tinh"] is not None
    )
    ty_le_lap_day_tong = (
        tong_ton_hien_tai / tong_suc_chua * 100
        if tong_suc_chua > 0
        else None
    )

    tu_khoa_chuan_hoa = tu_khoa.casefold()
    bon_sau_loc = []
    for bon in tat_ca_bon:
        if nhien_lieu_id and str(bon["nhien_lieu_id"]) != nhien_lieu_id:
            continue
        if trang_thai and bon["trang_thai"] != trang_thai:
            continue
        if tu_khoa_chuan_hoa and not any(
            tu_khoa_chuan_hoa in str(gia_tri or "").casefold()
            for gia_tri in (bon["ma_bon"], bon["ten_bon"])
        ):
            continue
        bon_sau_loc.append(bon)

    danh_sach_nhien_lieu = sorted(
        {
            (bon["nhien_lieu_id"], bon["ma_nhien_lieu"], bon["ten_nhien_lieu"])
            for bon in tat_ca_bon
        },
        key=lambda nhien_lieu: nhien_lieu[1],
    )
    danh_sach_trang_thai = sorted(
        {bon["trang_thai"] for bon in tat_ca_bon}
    )

    return {
        "danh_sach_bon": bon_sau_loc,
        "danh_sach_nhien_lieu": danh_sach_nhien_lieu,
        "danh_sach_trang_thai": danh_sach_trang_thai,
        "filters": {
            "q": tu_khoa,
            "nhien_lieu_id": nhien_lieu_id,
            "trang_thai": trang_thai,
        },
        "thong_ke": {
            "tong_so_bon": len(tat_ca_bon),
            "tong_suc_chua": tong_suc_chua,
            "tong_ton_hien_tai": tong_ton_hien_tai,
            "ty_le_lap_day": ty_le_lap_day_tong,
            "so_bon_bat_thuong": sum(
                bon["du_lieu_bat_thuong"] for bon in tat_ca_bon
            ),
            "so_bon_gan_het": sum(
                bon["bon_gan_het"] for bon in tat_ca_bon
            ),
            "so_bon_het_hang": sum(
                bon["bon_het_hang"] for bon in tat_ca_bon
            ),
        },
    }


def lay_chi_tiet_bon(id):
    ket_noi_db, cursor = _mo_cursor()

    try:
        cursor.execute(
            """
            SELECT
                bc.id,
                bc.ma_bon,
                bc.ten_bon,
                bc.nhien_lieu_id,
                bc.suc_chua,
                bc.ton_hien_tai,
                bc.trang_thai,
                nl.ma_nhien_lieu,
                nl.ten_nhien_lieu,
                nl.don_vi
            FROM bon_chua bc
            JOIN nhien_lieu nl
                ON nl.id = bc.nhien_lieu_id
            WHERE bc.id = %s
            """,
            (id,),
        )
        bon = cursor.fetchone()
        return _tinh_thong_tin_bon(bon) if bon else None
    finally:
        cursor.close()
        ket_noi_db.close()