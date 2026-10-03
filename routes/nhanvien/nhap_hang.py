from datetime import date

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from services.database import ket_noi
from services.auth_service import yeu_cau_vai_tro


nhanvien_nhap_hang_bp = Blueprint(
    "nhanvien_nhap_hang",
    __name__
)


@nhanvien_nhap_hang_bp.before_request
@yeu_cau_vai_tro("Nhân viên ca")
def bao_ve_router_nhap_hang():
    return None


# =========================================================
# LẤY NHÂN VIÊN ĐANG ĐĂNG NHẬP
# =========================================================

def lay_nhan_vien_dang_dang_nhap():
    tai_khoan_id = session.get("tai_khoan_id")

    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                tk.id,
                tk.nhan_vien_id,
                nv.ma_nv,
                nv.ho_ten
            FROM tai_khoan tk
            JOIN nhan_vien nv
                ON tk.nhan_vien_id = nv.id
            WHERE tk.id = %s
        """, (tai_khoan_id,))

        return cursor.fetchone()

    finally:
        cursor.close()
        db.close()


# =========================================================
# LẤY DANH SÁCH PHIẾU
# =========================================================

def lay_danh_sach_phieu_nhap(nhan_vien_id):
    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                nh.id,
                nh.ma_nhap,
                nh.ngay_tao,
                nl.ma_nhien_lieu,
                nl.ten_nhien_lieu,
                bc.ma_bon,
                bc.ten_bon,
                nh.so_luong,
                nh.trang_thai,
                nv.ma_nv,
                nv.ho_ten
            FROM nhap_hang nh
            JOIN nhien_lieu nl
                ON nh.nhien_lieu_id = nl.id
            JOIN bon_chua bc
                ON nh.bon_id = bc.id
            JOIN nhan_vien nv
                ON nh.nhan_vien_id = nv.id
            WHERE nh.nhan_vien_id = %s
            ORDER BY
                nh.ngay_tao ASC,
                nh.id ASC
        """, (nhan_vien_id,))

        return cursor.fetchall()

    finally:
        cursor.close()
        db.close()


# =========================================================
# LẤY DỮ LIỆU FORM
# =========================================================

def lay_form_data():
    return {
        "nhien_lieu_id": request.form.get(
            "nhien_lieu_id",
            ""
        ).strip(),

        "bon_id": request.form.get(
            "bon_id",
            ""
        ).strip(),

        "so_luong": request.form.get(
            "so_luong",
            ""
        ).strip()
    }


# =========================================================
# LẤY NHIÊN LIỆU ĐANG BÁN
# =========================================================

def lay_danh_sach_nhien_lieu():
    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                ma_nhien_lieu,
                ten_nhien_lieu,
                don_vi
            FROM nhien_lieu
            WHERE trang_thai = 'Đang bán'
            ORDER BY ma_nhien_lieu
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        db.close()


# =========================================================
# LẤY BỒN ĐANG HOẠT ĐỘNG
# =========================================================

def lay_danh_sach_bon():
    db = ket_noi()
    cursor = db.cursor(dictionary=True)

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
                bc.suc_chua,
                bc.ton_hien_tai
            FROM bon_chua bc
            JOIN nhien_lieu nl
                ON bc.nhien_lieu_id = nl.id
            WHERE bc.trang_thai = 'Đang hoạt động'
            ORDER BY
                CAST(
                    SUBSTRING(bc.ma_bon, 3)
                    AS UNSIGNED
                )
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        db.close()


# =========================================================
# KIỂM TRA FORM
# =========================================================

def kiem_tra_form(form_data):
    errors = {}

    nhien_lieu_id = form_data["nhien_lieu_id"]
    bon_id = form_data["bon_id"]
    so_luong = form_data["so_luong"]

    # -----------------------------
    # Nhiên liệu
    # -----------------------------

    if not nhien_lieu_id:
        errors["nhien_lieu_id"] = (
            "Vui lòng chọn nhiên liệu."
        )

    # -----------------------------
    # Bồn
    # -----------------------------

    if not bon_id:
        errors["bon_id"] = (
            "Vui lòng chọn bồn nhận."
        )

    # -----------------------------
    # Số lượng
    # -----------------------------

    so_luong_int = None

    if not so_luong:
        errors["so_luong"] = (
            "Vui lòng nhập số lượng."
        )

    else:
        try:
            so_luong_int = int(so_luong)

            if so_luong_int <= 0:
                errors["so_luong"] = (
                    "Số lượng phải lớn hơn 0."
                )

        except ValueError:
            errors["so_luong"] = (
                "Số lượng phải là số nguyên."
            )

    # -----------------------------
    # Kiểm tra nhiên liệu + bồn
    # -----------------------------

    if not errors:
        db = ket_noi()
        cursor = db.cursor(dictionary=True)

        try:
            cursor.execute("""
                SELECT
                    nl.id AS nhien_lieu_id,
                    nl.ten_nhien_lieu,
                    bc.id AS bon_id,
                    bc.ma_bon,
                    bc.ten_bon,
                    bc.nhien_lieu_id AS nhien_lieu_bon_id,
                    bc.suc_chua,
                    bc.ton_hien_tai
                FROM nhien_lieu nl
                JOIN bon_chua bc
                    ON bc.id = %s
                WHERE nl.id = %s
                  AND nl.trang_thai = 'Đang bán'
                  AND bc.trang_thai = 'Đang hoạt động'
            """, (
                bon_id,
                nhien_lieu_id
            ))

            thong_tin = cursor.fetchone()

            if thong_tin is None:
                errors["bon_id"] = (
                    "Nhiên liệu hoặc bồn không hợp lệ."
                )

            else:
                # Kiểm tra bằng ID
                if (
                    int(thong_tin["nhien_lieu_id"])
                    != int(thong_tin["nhien_lieu_bon_id"])
                ):
                    errors["bon_id"] = (
                        "Bồn không chứa loại "
                        "nhiên liệu đã chọn."
                    )

                elif so_luong_int is not None:
                    suc_chua_con_lai = (
                        thong_tin["suc_chua"]
                        - thong_tin["ton_hien_tai"]
                    )

                    if so_luong_int > suc_chua_con_lai:
                        errors["so_luong"] = (
                            "Số lượng vượt sức chứa "
                            "còn lại của bồn "
                            f"({suc_chua_con_lai})."
                        )

        finally:
            cursor.close()
            db.close()

    return errors


# =========================================================
# SINH MÃ PHIẾU
# =========================================================

def sinh_ma_nhap():
    db = ket_noi()
    cursor = db.cursor()

    try:
        cursor.execute("""
            SELECT ma_nhap
            FROM nhap_hang
            ORDER BY id DESC
            LIMIT 1
        """)

        dong_cuoi = cursor.fetchone()

        if dong_cuoi is None:
            return "NH001"

        ma_cu = dong_cuoi[0]

        try:
            so_cu = int(
                ma_cu.replace("NH", "")
            )

        except ValueError:
            so_cu = 0

        return f"NH{so_cu + 1:03d}"

    finally:
        cursor.close()
        db.close()


# =========================================================
# DANH SÁCH
# =========================================================

@nhanvien_nhap_hang_bp.route(
    "/nhanvien/nhap-hang"
)
def danh_sach():

    nhan_vien = (
        lay_nhan_vien_dang_dang_nhap()
    )

    if nhan_vien is None:
        return (
            "Không tìm thấy nhân viên đang đăng nhập.",
            404
        )

    danh_sach_phieu_nhap = (
        lay_danh_sach_phieu_nhap(
            nhan_vien["nhan_vien_id"]
        )
    )

    tong_so_phieu_nhap = len(
        danh_sach_phieu_nhap
    )

    # Chỉ tính số lượng của phiếu ĐÃ DUYỆT
    tong_so_luong_nhap = sum(
        phieu["so_luong"]
        for phieu in danh_sach_phieu_nhap
        if phieu["trang_thai"] == "Đã duyệt"
    )

    so_phieu_cho_duyet = sum(
        phieu["trang_thai"] == "Chờ duyệt"
        for phieu in danh_sach_phieu_nhap
    )

    return render_template(
        "nhanvien/nhaphang/index.html",
        trang_hien_tai="Nhập hàng",
        nhan_vien=nhan_vien,
        danh_sach_phieu_nhap=danh_sach_phieu_nhap,
        tong_so_phieu_nhap=tong_so_phieu_nhap,
        tong_so_luong_nhap=tong_so_luong_nhap,
        so_phieu_cho_duyet=so_phieu_cho_duyet
    )


# =========================================================
# THÊM PHIẾU
# =========================================================

@nhanvien_nhap_hang_bp.route(
    "/nhanvien/nhap-hang/them",
    methods=["GET", "POST"]
)
def them():

    nhan_vien = (
        lay_nhan_vien_dang_dang_nhap()
    )

    if nhan_vien is None:
        return (
            "Không tìm thấy nhân viên đang đăng nhập.",
            404
        )

    danh_sach_nhien_lieu = (
        lay_danh_sach_nhien_lieu()
    )

    danh_sach_bon = (
        lay_danh_sach_bon()
    )

    form_data = {
        "nhien_lieu_id": "",
        "bon_id": "",
        "so_luong": ""
    }

    errors = {}

    if request.method == "POST":

        form_data = lay_form_data()

        errors = kiem_tra_form(
            form_data
        )

        if not errors:

            db = ket_noi()
            cursor = db.cursor()

            try:
                ma_nhap = sinh_ma_nhap()

                cursor.execute("""
                    INSERT INTO nhap_hang (
                        ma_nhap,
                        ngay_tao,
                        nhien_lieu_id,
                        bon_id,
                        so_luong,
                        nhan_vien_id,
                        trang_thai
                    )
                    VALUES (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        'Chờ duyệt'
                    )
                """, (
                    ma_nhap,
                    date.today(),
                    form_data["nhien_lieu_id"],
                    form_data["bon_id"],
                    int(form_data["so_luong"]),
                    nhan_vien["nhan_vien_id"]
                ))

                db.commit()

            except Exception:
                db.rollback()
                raise

            finally:
                cursor.close()
                db.close()

            return redirect(
                url_for(
                    "nhanvien_nhap_hang.danh_sach"
                )
            )

    return render_template(
        "nhanvien/nhaphang/them.html",
        trang_hien_tai="Nhập hàng",
        nhan_vien=nhan_vien,
        danh_sach_nhien_lieu=danh_sach_nhien_lieu,
        danh_sach_bon=danh_sach_bon,
        form_data=form_data,
        errors=errors
    )


# =========================================================
# XEM PHIẾU
# =========================================================

@nhanvien_nhap_hang_bp.route(
    "/nhanvien/nhap-hang/xem/<int:id>"
)
def xem(id):

    nhan_vien = (
        lay_nhan_vien_dang_dang_nhap()
    )

    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                nh.id,
                nh.ma_nhap,
                nh.ngay_tao,
                nh.so_luong,
                nh.trang_thai,
                nl.ma_nhien_lieu,
                nl.ten_nhien_lieu,
                nl.don_vi,
                bc.ma_bon,
                bc.ten_bon,
                bc.suc_chua,
                bc.ton_hien_tai,
                nv.ma_nv,
                nv.ho_ten
            FROM nhap_hang nh
            JOIN nhien_lieu nl
                ON nh.nhien_lieu_id = nl.id
            JOIN bon_chua bc
                ON nh.bon_id = bc.id
            JOIN nhan_vien nv
                ON nh.nhan_vien_id = nv.id
            WHERE nh.id = %s
              AND nh.nhan_vien_id = %s
        """, (
            id,
            nhan_vien["nhan_vien_id"]
        ))

        phieu = cursor.fetchone()

    finally:
        cursor.close()
        db.close()

    if phieu is None:
        return "Không tìm thấy phiếu nhập.", 404

    return render_template(
        "nhanvien/nhaphang/xem.html",
        trang_hien_tai="Nhập hàng",
        phieu=phieu
    )


# =========================================================
# SỬA PHIẾU
# =========================================================

@nhanvien_nhap_hang_bp.route(
    "/nhanvien/nhap-hang/sua/<int:id>",
    methods=["GET", "POST"]
)
def sua(id):

    nhan_vien = (
        lay_nhan_vien_dang_dang_nhap()
    )

    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT *
            FROM nhap_hang
            WHERE id = %s
              AND nhan_vien_id = %s
        """, (
            id,
            nhan_vien["nhan_vien_id"]
        ))

        phieu = cursor.fetchone()

    finally:
        cursor.close()
        db.close()

    if phieu is None:
        return "Không tìm thấy phiếu nhập.", 404

    # ĐÃ DUYỆT → KHÔNG ĐƯỢC SỬA
    if phieu["trang_thai"] != "Chờ duyệt":
        return (
            "Phiếu đã được duyệt "
            "và không thể chỉnh sửa.",
            403
        )

    danh_sach_nhien_lieu = (
        lay_danh_sach_nhien_lieu()
    )

    danh_sach_bon = (
        lay_danh_sach_bon()
    )

    form_data = {
        "nhien_lieu_id": str(
            phieu["nhien_lieu_id"]
        ),
        "bon_id": str(
            phieu["bon_id"]
        ),
        "so_luong": str(
            phieu["so_luong"]
        )
    }

    errors = {}

    if request.method == "POST":

        form_data = lay_form_data()

        errors = kiem_tra_form(
            form_data
        )

        if not errors:

            db = ket_noi()
            cursor = db.cursor()

            try:
                cursor.execute("""
                    UPDATE nhap_hang
                    SET
                        nhien_lieu_id = %s,
                        bon_id = %s,
                        so_luong = %s
                    WHERE id = %s
                      AND nhan_vien_id = %s
                      AND trang_thai = 'Chờ duyệt'
                """, (
                    form_data["nhien_lieu_id"],
                    form_data["bon_id"],
                    int(form_data["so_luong"]),
                    id,
                    nhan_vien["nhan_vien_id"]
                ))

                db.commit()

            except Exception:
                db.rollback()
                raise

            finally:
                cursor.close()
                db.close()

            return redirect(
                url_for(
                    "nhanvien_nhap_hang.danh_sach"
                )
            )

    return render_template(
        "nhanvien/nhaphang/sua.html",
        trang_hien_tai="Nhập hàng",
        phieu=phieu,
        danh_sach_nhien_lieu=danh_sach_nhien_lieu,
        danh_sach_bon=danh_sach_bon,
        form_data=form_data,
        errors=errors
    )


# =========================================================
# XÓA PHIẾU
# =========================================================

@nhanvien_nhap_hang_bp.route(
    "/nhanvien/nhap-hang/xoa/<int:id>",
    methods=["POST"]
)
def xoa(id):

    nhan_vien = (
        lay_nhan_vien_dang_dang_nhap()
    )

    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                trang_thai
            FROM nhap_hang
            WHERE id = %s
              AND nhan_vien_id = %s
        """, (
            id,
            nhan_vien["nhan_vien_id"]
        ))

        phieu = cursor.fetchone()

        if phieu is None:
            return "Không tìm thấy phiếu nhập.", 404

        if phieu["trang_thai"] != "Chờ duyệt":
            return (
                "Phiếu đã được duyệt "
                "và không thể xóa.",
                403
            )

        cursor.execute("""
            DELETE FROM nhap_hang
            WHERE id = %s
              AND nhan_vien_id = %s
              AND trang_thai = 'Chờ duyệt'
        """, (
            id,
            nhan_vien["nhan_vien_id"]
        ))

        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        cursor.close()
        db.close()

    return redirect(
        url_for(
            "nhanvien_nhap_hang.danh_sach"
        )
    )