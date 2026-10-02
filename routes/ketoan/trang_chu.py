from flask import Blueprint, render_template, session
from services.auth_service import yeu_cau_dang_nhap
from services.database import ket_noi


ketoan_trang_chu_bp = Blueprint(
    "ketoan_trang_chu",
    __name__,
  #url_prefix="/nhan-vien"
)


@ketoan_trang_chu_bp.route("/kt")
@yeu_cau_dang_nhap
def home():
    ket_noi_db = ket_noi()
    cursor = ket_noi_db.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT ho_ten
            FROM nhan_vien
            WHERE id = %s
            """,
            (session["nhan_vien_id"],)
        )

        nhan_vien = cursor.fetchone()

        return render_template(
            "ketoan/index/index.html",
            trang_hien_tai="Trang chủ",
            ho_ten=nhan_vien["ho_ten"]
        )

    finally:
        cursor.close()
        ket_noi_db.close()