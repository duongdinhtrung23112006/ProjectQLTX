from flask import Blueprint, render_template

from services.database import ket_noi
from services.auth_service import yeu_cau_vai_tro


nhanvien_bon_chua_bp = Blueprint(
    "nhanvien_bon_chua",
    __name__
)


@nhanvien_bon_chua_bp.before_request
@yeu_cau_vai_tro("Nhân viên ca")
def bao_ve_router_bon_chua():
    return None


def lay_danh_sach_bon():
    ket_noi_db = ket_noi()
    cursor = ket_noi_db.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                bc.id,
                bc.ma_bon,
                bc.ten_bon,
                bc.nhien_lieu_id,
                nl.ma_nhien_lieu,
                nl.ten_nhien_lieu,
                nl.don_vi,
                nl.don_gia,
                bc.suc_chua,
                bc.ton_hien_tai,
                bc.trang_thai
            FROM bon_chua bc
            JOIN nhien_lieu nl
                ON bc.nhien_lieu_id = nl.id
            ORDER BY
                CAST(
                    SUBSTRING(bc.ma_bon, 3)
                    AS UNSIGNED
                )
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        ket_noi_db.close()


@nhanvien_bon_chua_bp.route(
    "/nhanvien/bon-chua"
)
def danh_sach():

    danh_sach_bon = lay_danh_sach_bon()

    tong_so_bon = len(danh_sach_bon)

    dang_hoat_dong = sum(
        1
        for bon in danh_sach_bon
        if bon["trang_thai"] == "Đang hoạt động"
    )

    ngung_hoat_dong = sum(
        1
        for bon in danh_sach_bon
        if bon["trang_thai"] == "Ngừng hoạt động"
    )

    return render_template(
        "nhanvien/bonchua/index.html",
        trang_hien_tai="Bồn chứa",
        danh_sach_bon=danh_sach_bon,
        tong_so_bon=tong_so_bon,
        dang_hoat_dong=dang_hoat_dong,
        ngung_hoat_dong=ngung_hoat_dong
    )


@nhanvien_bon_chua_bp.route(
    "/nhanvien/bon-chua/xem/<int:id>"
)
def xem(id):

    ket_noi_db = ket_noi()
    cursor = ket_noi_db.cursor(
        dictionary=True
    )

    try:
        cursor.execute("""
            SELECT
                bc.id,
                bc.ma_bon,
                bc.ten_bon,
                bc.nhien_lieu_id,
                nl.ma_nhien_lieu,
                nl.ten_nhien_lieu,
                nl.don_vi,
                nl.don_gia,
                bc.suc_chua,
                bc.ton_hien_tai,
                bc.trang_thai
            FROM bon_chua bc
            JOIN nhien_lieu nl
                ON bc.nhien_lieu_id = nl.id
            WHERE bc.id = %s
        """, (id,))

        bon = cursor.fetchone()

    finally:
        cursor.close()
        ket_noi_db.close()

    if bon is None:
        return "Không tìm thấy bồn chứa", 404

    return render_template(
        "nhanvien/bonchua/xem.html",
        trang_hien_tai="Bồn chứa",
        bon=bon
    )