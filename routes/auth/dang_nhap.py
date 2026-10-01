from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash

from services.database import ket_noi


dang_nhap_bp = Blueprint(
    "dang_nhap",
    __name__,
    url_prefix="/dang-nhap"
)


@dang_nhap_bp.route("/", methods=["GET", "POST"])
def dang_nhap():

    loi = ""

    # Giữ lại tên đăng nhập khi đăng nhập sai
    ten_dang_nhap = ""

    if request.method == "POST":

        ten_dang_nhap = request.form.get(
            "ten_dang_nhap",
            ""
        ).strip()

        mat_khau = request.form.get(
            "mat_khau",
            ""
        )

        # Kiểm tra tên đăng nhập
        if not ten_dang_nhap:
            loi = "Vui lòng nhập tên đăng nhập."

        # Kiểm tra mật khẩu
        elif not mat_khau:
            loi = "Vui lòng nhập mật khẩu."

        else:
            ket_noi_db = ket_noi()
            cursor = ket_noi_db.cursor(dictionary=True)

            try:
                cursor.execute(
                    """
                    SELECT *
                    FROM tai_khoan
                    WHERE ten_dang_nhap = %s
                    """,
                    (ten_dang_nhap,)
                )

                tai_khoan = cursor.fetchone()

                # Không tìm thấy tài khoản
                if not tai_khoan:
                    loi = "Tên đăng nhập hoặc mật khẩu không đúng."

                # Mật khẩu sai
                elif not check_password_hash(
                    tai_khoan["mat_khau"],
                    mat_khau
                ):
                    loi = "Tên đăng nhập hoặc mật khẩu không đúng."

                else:
                    # =========================
                    # ĐĂNG NHẬP THÀNH CÔNG
                    # =========================

                    session["tai_khoan_id"] = tai_khoan["id"]

                    session["nhan_vien_id"] = tai_khoan["nhan_vien_id"]

                    session["vai_tro"] = tai_khoan["vai_tro"]

                    session["ten_dang_nhap"] = tai_khoan["ten_dang_nhap"]

                    if tai_khoan["vai_tro"] == "Quản lý":
                      return redirect(
                      url_for("quanly_trang_chu.home")
                    )

                    elif tai_khoan["vai_tro"] == "Nhân viên ca":
                      return redirect(
                      url_for("nhanvien_trang_chu.home")
                    )

                    elif tai_khoan["vai_tro"] == "Kế toán":
                      return redirect(
                      url_for("ketoan_trang_chu.home")
                    )

                    else:
                     session.clear()
                     loi = "Vai trò tài khoản không hợp lệ."
        

            except Exception as e:
                print(f"Lỗi đăng nhập: {e}")
                loi = "Có lỗi xảy ra khi đăng nhập."

            finally:
                cursor.close()
                ket_noi_db.close()

    return render_template(
        "auth/dang_nhap.html",
        loi=loi,
        ten_dang_nhap=ten_dang_nhap
    )

@dang_nhap_bp.route("/dang-xuat")
def dang_xuat():

    # Xóa toàn bộ thông tin đăng nhập
    session.clear()

    # Quay về trang đăng nhập
    return redirect(
        url_for("dang_nhap.dang_nhap")
    )