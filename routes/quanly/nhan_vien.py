from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from services.auth_service import yeu_cau_dang_nhap

from services.database import ket_noi

nhan_vien_bp = Blueprint("nhan_vien", __name__)

@nhan_vien_bp.before_request
@yeu_cau_dang_nhap
def bao_ve_router_nhan_vien():
    return None


def lay_danh_sach_nhan_vien():
    ket_noi_db = ket_noi()
    cursor = ket_noi_db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM nhan_vien ORDER BY id DESC")

    danh_sach_nhan_vien = cursor.fetchall()

    cursor.close()
    ket_noi_db.close()

    return danh_sach_nhan_vien


@nhan_vien_bp.route("/nhan-vien")
@yeu_cau_dang_nhap
def danh_sach():
    danh_sach_nhan_vien = lay_danh_sach_nhan_vien()

    tong_so_nhan_vien = len(danh_sach_nhan_vien)

    dang_lam_viec = sum(
        1 for nhan_vien in danh_sach_nhan_vien
        if nhan_vien["trang_thai"] == "Đang làm việc"
    )

    ngung_lam_viec = sum(
        1 for nhan_vien in danh_sach_nhan_vien
        if nhan_vien["trang_thai"] == "Ngừng làm việc"
    )

    return render_template(
        "quanly/nhanvien/index.html",
        trang_hien_tai="Nhân viên",
        danh_sach_nhan_vien=danh_sach_nhan_vien,
        tong_so_nhan_vien=tong_so_nhan_vien,
        dang_lam_viec=dang_lam_viec,
        ngung_lam_viec=ngung_lam_viec
    )


@nhan_vien_bp.route("/nhan-vien/them", methods=["GET", "POST"])
def them():
    form_data = {
        "ma_nv": "",
        "ho_ten": "",
        "so_dien_thoai": "",
        "dia_chi": "",
        "chuc_vu": "",
        "ngay_vao_lam": "",
        "trang_thai": "Đang làm việc",
        "ten_dang_nhap": ""
    }

    errors = {}

    if request.method == "POST":
        form_data = {
            "ma_nv": request.form.get("ma_nv", "").strip(),
            "ho_ten": request.form.get("ho_ten", "").strip(),
            "so_dien_thoai": request.form.get(
                "so_dien_thoai", ""
            ).strip(),
            "dia_chi": request.form.get(
                "dia_chi", ""
            ).strip(),
            "chuc_vu": request.form.get(
                "chuc_vu", ""
            ).strip(),
            "ngay_vao_lam": request.form.get(
                "ngay_vao_lam", ""
            ).strip(),
            "trang_thai": request.form.get(
                "trang_thai", ""
            ).strip(),
            "ten_dang_nhap": request.form.get(
                "ten_dang_nhap", ""
            ).strip()
        }

        mat_khau = request.form.get("mat_khau", "")
        xac_nhan_mat_khau = request.form.get(
            "xac_nhan_mat_khau", ""
        )

        # =========================
        # KIỂM TRA THÔNG TIN NHÂN VIÊN
        # =========================

        if not form_data["ma_nv"]:
            errors["ma_nv"] = "Vui lòng nhập mã nhân viên."

        if not form_data["ho_ten"]:
            errors["ho_ten"] = "Vui lòng nhập họ và tên."

        if not form_data["chuc_vu"]:
            errors["chuc_vu"] = "Vui lòng chọn chức vụ."

        if form_data["trang_thai"] not in {
            "Đang làm việc",
            "Ngừng làm việc"
        }:
            errors["trang_thai"] = "Trạng thái không hợp lệ."

        # =========================
        # KIỂM TRA THÔNG TIN TÀI KHOẢN
        # =========================

        if not form_data["ten_dang_nhap"]:
            errors["ten_dang_nhap"] = (
                "Vui lòng nhập tên đăng nhập."
            )

        if not mat_khau:
            errors["mat_khau"] = (
                "Vui lòng nhập mật khẩu."
            )

        if not xac_nhan_mat_khau:
            errors["xac_nhan_mat_khau"] = (
                "Vui lòng xác nhận mật khẩu."
            )

        if (
            mat_khau
            and xac_nhan_mat_khau
            and mat_khau != xac_nhan_mat_khau
        ):
            errors["xac_nhan_mat_khau"] = (
                "Mật khẩu xác nhận không khớp."
            )

        # =========================
        # LƯU NHÂN VIÊN + TÀI KHOẢN
        # =========================

        if not errors:
            ket_noi_db = ket_noi()
            cursor = ket_noi_db.cursor(dictionary=True)

            try:
                # Kiểm tra mã nhân viên
                cursor.execute(
                    """
                    SELECT id
                    FROM nhan_vien
                    WHERE ma_nv = %s
                    """,
                    (form_data["ma_nv"],)
                )

                nhan_vien_trung = cursor.fetchone()

                if nhan_vien_trung:
                    errors["ma_nv"] = (
                        "Mã nhân viên đã tồn tại."
                    )

                # Kiểm tra tên đăng nhập
                cursor.execute(
                    """
                    SELECT id
                    FROM tai_khoan
                    WHERE ten_dang_nhap = %s
                    """,
                    (form_data["ten_dang_nhap"],)
                )

                tai_khoan_trung = cursor.fetchone()

                if tai_khoan_trung:
                    errors["ten_dang_nhap"] = (
                        "Tên đăng nhập đã tồn tại."
                    )

                if not errors:
                    # -------------------------
                    # 1. TẠO NHÂN VIÊN
                    # -------------------------

                    cursor.execute(
                        """
                        INSERT INTO nhan_vien
                        (
                            ma_nv,
                            ho_ten,
                            so_dien_thoai,
                            dia_chi,
                            chuc_vu,
                            ngay_vao_lam,
                            trang_thai
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            form_data["ma_nv"],
                            form_data["ho_ten"],
                            form_data["so_dien_thoai"] or None,
                            form_data["dia_chi"] or None,
                            form_data["chuc_vu"],
                            form_data["ngay_vao_lam"] or None,
                            form_data["trang_thai"]
                        )
                    )

                    # Lấy ID nhân viên vừa tạo
                    nhan_vien_id = cursor.lastrowid

                    # -------------------------
                    # 2. HASH MẬT KHẨU
                    # -------------------------

                    mat_khau_da_hash = generate_password_hash(
                        mat_khau
                    )

                    # -------------------------
                    # 3. TẠO TÀI KHOẢN
                    # -------------------------

                    cursor.execute(
                        """
                        INSERT INTO tai_khoan
                        (
                            ten_dang_nhap,
                            mat_khau,
                            vai_tro,
                            nhan_vien_id
                        )
                        VALUES (%s, %s, %s, %s)
                        """,
                        (
                            form_data["ten_dang_nhap"],
                            mat_khau_da_hash,
                            form_data["chuc_vu"],
                            nhan_vien_id
                        )
                    )

                    # Cả nhân viên và tài khoản
                    # đều được lưu cùng lúc
                    ket_noi_db.commit()

                    cursor.close()
                    ket_noi_db.close()

                    return redirect(
                        url_for("nhan_vien.danh_sach")
                    )

            except Exception as e:
                ket_noi_db.rollback()

                print(
                    f"Lỗi khi tạo nhân viên và tài khoản: {e}"
                )

                errors["chung"] = (
                    "Không thể tạo nhân viên và tài khoản."
                )

            finally:
                cursor.close()
                ket_noi_db.close()

    return render_template(
        "quanly/nhanvien/them.html",
        trang_hien_tai="Nhân viên",
        form_data=form_data,
        errors=errors
    )


@nhan_vien_bp.route(
    "/nhan-vien/sua/<int:id>",
    methods=["GET", "POST"]
)
def sua(id):
    ket_noi_db = ket_noi()
    cursor = ket_noi_db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM nhan_vien WHERE id = %s",
        (id,)
    )

    nhan_vien = cursor.fetchone()

    cursor.close()
    ket_noi_db.close()

    if nhan_vien is None:
        return "Không tìm thấy nhân viên", 404

    form_data = {
        "ma_nv": nhan_vien["ma_nv"],
        "ho_ten": nhan_vien["ho_ten"],
        "so_dien_thoai": nhan_vien["so_dien_thoai"],
        "dia_chi": nhan_vien["dia_chi"],
        "chuc_vu": nhan_vien["chuc_vu"],
        "ngay_vao_lam": (
            nhan_vien["ngay_vao_lam"].strftime("%Y-%m-%d")
            if nhan_vien["ngay_vao_lam"]
            else ""
        ),
        "trang_thai": nhan_vien["trang_thai"]
    }

    errors = {}

    if request.method == "POST":
        form_data = {
            "ma_nv": request.form.get("ma_nv", "").strip(),
            "ho_ten": request.form.get("ho_ten", "").strip(),
            "so_dien_thoai": request.form.get(
                "so_dien_thoai", ""
            ).strip(),
            "dia_chi": request.form.get(
                "dia_chi", ""
            ).strip(),
            "chuc_vu": request.form.get(
                "chuc_vu", ""
            ).strip(),
            "ngay_vao_lam": request.form.get(
                "ngay_vao_lam", ""
            ).strip(),
            "trang_thai": request.form.get(
                "trang_thai", ""
            ).strip()
        }

        if not form_data["ma_nv"]:
            errors["ma_nv"] = (
                "Vui lòng nhập mã nhân viên."
            )

        elif any(
            item["ma_nv"] == form_data["ma_nv"]
            and item["id"] != id
            for item in lay_danh_sach_nhan_vien()
        ):
            errors["ma_nv"] = (
                "Mã nhân viên đã tồn tại."
            )

        if not form_data["ho_ten"]:
            errors["ho_ten"] = (
                "Vui lòng nhập họ và tên."
            )

        if not form_data["chuc_vu"]:
            errors["chuc_vu"] = (
                "Vui lòng chọn chức vụ."
            )

        if form_data["trang_thai"] not in {
            "Đang làm việc",
            "Ngừng làm việc"
        }:
            errors["trang_thai"] = (
                "Trạng thái không hợp lệ."
            )

        if errors:
            return render_template(
                "quanly/nhanvien/sua.html",
                trang_hien_tai="Nhân viên",
                form_data=form_data,
                errors=errors,
                id=id
            ), 422

        ket_noi_db = ket_noi()
        cursor = ket_noi_db.cursor()

        try:
            cursor.execute(
                """
                UPDATE nhan_vien
                SET ma_nv = %s,
                    ho_ten = %s,
                    so_dien_thoai = %s,
                    dia_chi = %s,
                    chuc_vu = %s,
                    ngay_vao_lam = %s,
                    trang_thai = %s
                WHERE id = %s
                """,
                (
                    form_data["ma_nv"],
                    form_data["ho_ten"],
                    form_data["so_dien_thoai"] or None,
                    form_data["dia_chi"] or None,
                    form_data["chuc_vu"],
                    form_data["ngay_vao_lam"] or None,
                    form_data["trang_thai"],
                    id
                )
            )

            if form_data["trang_thai"] == "Ngừng làm việc":
                cursor.execute(
                    """
                    UPDATE ca_lam_viec
                    SET trang_thai = 'Đã đóng'
                    WHERE nhan_vien_id = %s
                    """,
                    (id,)
                )

            ket_noi_db.commit()

        except Exception as e:
            ket_noi_db.rollback()
            print(f"Lỗi khi sửa nhân viên: {e}")

        finally:
            cursor.close()
            ket_noi_db.close()

        return redirect(
            url_for("nhan_vien.danh_sach")
        )

    return render_template(
        "quanly/nhanvien/sua.html",
        trang_hien_tai="Nhân viên",
        form_data=form_data,
        errors=errors,
        id=id
    )


@nhan_vien_bp.route(
    "/nhan-vien/xoa/<int:id>",
    methods=["POST"]
)
def xoa(id):
    ket_noi_db = ket_noi()
    cursor = ket_noi_db.cursor()

    try:
        # Xóa tất cả ca làm việc của nhân viên này
        cursor.execute(
            """
            DELETE FROM ca_lam_viec
            WHERE nhan_vien_id = %s
            """,
            (id,)
        )

        # Xóa tài khoản đăng nhập của nhân viên này
        cursor.execute(
            """
            DELETE FROM tai_khoan
            WHERE nhan_vien_id = %s
            """,
            (id,)
        )

        # Xóa nhân viên
        cursor.execute(
            """
            DELETE FROM nhan_vien
            WHERE id = %s
            """,
            (id,)
        )

        ket_noi_db.commit()

    except Exception as e:
        ket_noi_db.rollback()

        print(
            f"Lỗi khi xóa nhân viên: {e}"
        )

    finally:
        cursor.close()
        ket_noi_db.close()

    return redirect(
        url_for("nhan_vien.danh_sach")
    )

@nhan_vien_bp.route("/nhan-vien/xem/<int:id>")
def xem(id):
    ket_noi_db = ket_noi()
    cursor = ket_noi_db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM nhan_vien WHERE id = %s",
        (id,)
    )

    nhan_vien = cursor.fetchone()

    cursor.close()
    ket_noi_db.close()

    if nhan_vien is None:
        return "Không tìm thấy nhân viên", 404

    return render_template(
        "quanly/nhanvien/xem.html",
        trang_hien_tai="Nhân viên",
        nhan_vien=nhan_vien
    )