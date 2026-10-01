from flask import Blueprint, render_template, request, redirect, url_for
from services.database import ket_noi
from services.auth_service import yeu_cau_dang_nhap

nhien_lieu_bp = Blueprint("nhien_lieu", __name__)


@nhien_lieu_bp.before_request
@yeu_cau_dang_nhap
def bao_ve_router_nhien_lieu():
    return None


def lay_danh_sach_nhien_lieu():
    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id,
            ma_nhien_lieu,
            ten_nhien_lieu,
            don_vi_tinh,
            don_gia,
            trang_thai
        FROM nhien_lieu
        ORDER BY id DESC
    """)

    danh_sach = cursor.fetchall()

    cursor.close()
    db.close()

    return danh_sach


def lay_form_data():
    return {
        "ma_nhien_lieu": request.form.get(
            "ma_nhien_lieu", ""
        ).strip(),

        "ten_nhien_lieu": request.form.get(
            "ten_nhien_lieu", ""
        ).strip(),

        "don_vi_tinh": request.form.get(
            "don_vi_tinh", ""
        ).strip(),

        "don_gia": request.form.get(
            "don_gia", ""
        ).strip(),

        "trang_thai": request.form.get(
            "trang_thai", ""
        ).strip()
    }


def kiem_tra(form_data, nhien_lieu_id=None):
    errors = {}

    if not form_data["ma_nhien_lieu"]:
        errors["ma_nhien_lieu"] = "Vui lòng nhập mã nhiên liệu."

    if not form_data["ten_nhien_lieu"]:
        errors["ten_nhien_lieu"] = "Vui lòng nhập tên nhiên liệu."

    if not form_data["don_vi_tinh"]:
        errors["don_vi_tinh"] = "Vui lòng nhập đơn vị tính."

    if not form_data["don_gia"]:
        errors["don_gia"] = "Vui lòng nhập đơn giá."
    else:
        try:
            don_gia = float(form_data["don_gia"])

            if don_gia <= 0:
                errors["don_gia"] = "Đơn giá phải lớn hơn 0."

        except ValueError:
            errors["don_gia"] = "Đơn giá không hợp lệ."

    if form_data["trang_thai"] not in {
        "Đang kinh doanh",
        "Ngừng kinh doanh"
    }:
        errors["trang_thai"] = "Trạng thái không hợp lệ."

    if not errors:
        db = ket_noi()
        cursor = db.cursor(dictionary=True)

        if nhien_lieu_id is None:
            cursor.execute("""
                SELECT id
                FROM nhien_lieu
                WHERE ma_nhien_lieu = %s
            """, (form_data["ma_nhien_lieu"],))
        else:
            cursor.execute("""
                SELECT id
                FROM nhien_lieu
                WHERE ma_nhien_lieu = %s
                  AND id != %s
            """, (
                form_data["ma_nhien_lieu"],
                nhien_lieu_id
            ))

        trung = cursor.fetchone()

        cursor.close()
        db.close()

        if trung:
            errors["ma_nhien_lieu"] = (
                "Mã nhiên liệu đã tồn tại."
            )

    return errors


@nhien_lieu_bp.route("/nhien-lieu")
def danh_sach():
    danh_sach = lay_danh_sach_nhien_lieu()

    return render_template(
        "quanly/nhien_lieu/index.html",
        trang_hien_tai="Nhiên liệu",
        danh_sach_nhien_lieu=danh_sach,
        tong_so_nhien_lieu=len(danh_sach),
        dang_kinh_doanh=sum(
            nhien_lieu["trang_thai"] == "Đang kinh doanh"
            for nhien_lieu in danh_sach
        ),
        ngung_kinh_doanh=sum(
            nhien_lieu["trang_thai"] == "Ngừng kinh doanh"
            for nhien_lieu in danh_sach
        )
    )


@nhien_lieu_bp.route(
    "/nhien-lieu/them",
    methods=["GET", "POST"]
)
def them():
    form_data = {
        "ma_nhien_lieu": "",
        "ten_nhien_lieu": "",
        "don_vi_tinh": "Lít",
        "don_gia": "",
        "trang_thai": "Đang kinh doanh"
    }

    errors = {}

    if request.method == "POST":
        form_data = lay_form_data()

        errors = kiem_tra(form_data)

        if not errors:
            db = ket_noi()
            cursor = db.cursor()

            cursor.execute("""
                INSERT INTO nhien_lieu
                (
                    ma_nhien_lieu,
                    ten_nhien_lieu,
                    don_vi_tinh,
                    don_gia,
                    trang_thai
                )
                VALUES (%s, %s, %s, %s, %s)
            """, (
                form_data["ma_nhien_lieu"],
                form_data["ten_nhien_lieu"],
                form_data["don_vi_tinh"],
                float(form_data["don_gia"]),
                form_data["trang_thai"]
            ))

            db.commit()

            cursor.close()
            db.close()

            return redirect(
                url_for("nhien_lieu.danh_sach")
            )

    return render_template(
        "quanly/nhien_lieu/them.html",
        trang_hien_tai="Nhiên liệu",
        form_data=form_data,
        errors=errors
    )


@nhien_lieu_bp.route(
    "/nhien-lieu/sua/<int:id>",
    methods=["GET", "POST"]
)
def sua(id):
    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM nhien_lieu WHERE id = %s",
        (id,)
    )

    nhien_lieu = cursor.fetchone()

    cursor.close()
    db.close()

    if nhien_lieu is None:
        return "Không tìm thấy nhiên liệu", 404

    form_data = {
        "ma_nhien_lieu": nhien_lieu["ma_nhien_lieu"],
        "ten_nhien_lieu": nhien_lieu["ten_nhien_lieu"],
        "don_vi_tinh": nhien_lieu["don_vi_tinh"],
        "don_gia": str(nhien_lieu["don_gia"]),
        "trang_thai": nhien_lieu["trang_thai"]
    }

    errors = {}

    if request.method == "POST":
        form_data = lay_form_data()

        errors = kiem_tra(
            form_data,
            id
        )

        if not errors:
            db = ket_noi()
            cursor = db.cursor()

            cursor.execute("""
                UPDATE nhien_lieu
                SET ma_nhien_lieu = %s,
                    ten_nhien_lieu = %s,
                    don_vi_tinh = %s,
                    don_gia = %s,
                    trang_thai = %s
                WHERE id = %s
            """, (
                form_data["ma_nhien_lieu"],
                form_data["ten_nhien_lieu"],
                form_data["don_vi_tinh"],
                float(form_data["don_gia"]),
                form_data["trang_thai"],
                id
            ))

            db.commit()

            cursor.close()
            db.close()

            return redirect(
                url_for("nhien_lieu.danh_sach")
            )

    return render_template(
        "quanly/nhien_lieu/sua.html",
        trang_hien_tai="Nhiên liệu",
        form_data=form_data,
        errors=errors,
        id=id
    )


@nhien_lieu_bp.route(
    "/nhien-lieu/xoa/<int:id>",
    methods=["POST"]
)
def xoa(id):
    db = ket_noi()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM nhien_lieu WHERE id = %s",
        (id,)
    )

    db.commit()

    cursor.close()
    db.close()

    return redirect(
        url_for("nhien_lieu.danh_sach")
    )


@nhien_lieu_bp.route(
    "/nhien-lieu/xem/<int:id>"
)
def xem(id):
    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM nhien_lieu WHERE id = %s",
        (id,)
    )

    nhien_lieu = cursor.fetchone()

    cursor.close()
    db.close()

    if nhien_lieu is None:
        return "Không tìm thấy nhiên liệu", 404

    return render_template(
        "quanly/nhien_lieu/xem.html",
        trang_hien_tai="Nhiên liệu",
        nhien_lieu=nhien_lieu
    )