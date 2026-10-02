from flask import Blueprint, render_template

from services.database import ket_noi
from services.auth_service import yeu_cau_vai_tro


nhanvien_nhien_lieu_bp = Blueprint(
    "nhanvien_nhien_lieu",
    __name__
)


@nhanvien_nhien_lieu_bp.before_request
@yeu_cau_vai_tro("Nhân viên ca")
def bao_ve_router_nhien_lieu():
    return None


def lay_danh_sach_nhien_lieu():
    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                ma_nhien_lieu,
                ten_nhien_lieu,
                don_vi,
                don_gia,
                trang_thai
            FROM nhien_lieu
            ORDER BY ma_nhien_lieu
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        db.close()


# =========================
# XEM DANH SÁCH
# =========================

@nhanvien_nhien_lieu_bp.route("/nhanvien/nhien-lieu")
def danh_sach():

    danh_sach_nhien_lieu = (
        lay_danh_sach_nhien_lieu()
    )

    return render_template(
        "nhanvien/nhienlieu/index.html",
        trang_hien_tai="Nhiên liệu",
        danh_sach_nhien_lieu=danh_sach_nhien_lieu,
        tong_so_nhien_lieu=len(
            danh_sach_nhien_lieu
        ),
        dang_ban=sum(
            nhien_lieu["trang_thai"] == "Đang bán"
            for nhien_lieu in danh_sach_nhien_lieu
        ),
        ngung_ban=sum(
            nhien_lieu["trang_thai"] == "Ngừng bán"
            for nhien_lieu in danh_sach_nhien_lieu
        )
    )


# =========================
# XEM CHI TIẾT
# =========================

@nhanvien_nhien_lieu_bp.route(
    "/nhanvien/nhien-lieu/xem/<int:id>"
)
def xem(id):

    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                ma_nhien_lieu,
                ten_nhien_lieu,
                don_vi,
                don_gia,
                trang_thai
            FROM nhien_lieu
            WHERE id = %s
        """, (id,))

        nhien_lieu = cursor.fetchone()

    finally:
        cursor.close()
        db.close()

    if nhien_lieu is None:
        return "Không tìm thấy nhiên liệu", 404

    return render_template(
        "nhanvien/nhienlieu/xem.html",
        trang_hien_tai="Nhiên liệu",
        nhien_lieu=nhien_lieu
    )