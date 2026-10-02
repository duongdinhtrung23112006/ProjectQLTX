from flask import Blueprint, render_template, request, redirect, url_for

from services.database import ket_noi

from services.auth_service import yeu_cau_vai_tro


bon_chua_bp = Blueprint("bon_chua", __name__)


@bon_chua_bp.before_request
@yeu_cau_vai_tro("Quản lý")
def bao_ve_router_bon_chua():
    return None


def lay_danh_sach_bon():
    ket_noi_db = ket_noi()
    cursor = ket_noi_db.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM bon_chua
        ORDER BY CAST(SUBSTRING(ma_bon, 4) AS UNSIGNED)
    """)

    danh_sach_bon = cursor.fetchall()

    cursor.close()
    ket_noi_db.close()

    return danh_sach_bon


@bon_chua_bp.route("/bon-chua")
def danh_sach():

    danh_sach_bon = lay_danh_sach_bon()

    tong_so_bon = len(danh_sach_bon)

    dang_hoat_dong = sum(
        1 for bon in danh_sach_bon
        if bon["trang_thai"] == "Đang hoạt động"
    )

    ngung_hoat_dong = sum(
        1 for bon in danh_sach_bon
        if bon["trang_thai"] == "Ngừng hoạt động"
    )

    return render_template(
        "quanly/bonchua/index.html",
        trang_hien_tai="Bồn chứa",
        danh_sach_bon=danh_sach_bon,
        tong_so_bon=tong_so_bon,
        dang_hoat_dong=dang_hoat_dong,
        ngung_hoat_dong=ngung_hoat_dong
    )


@bon_chua_bp.route(
    "/bon-chua/them",
    methods=["GET", "POST"]
)
def them():

    form_data = {
        "ma_bon": "",
        "ten_bon": "",
        "nhien_lieu": "",
        "suc_chua": "",
        "ton_hien_tai": "",
        "trang_thai": "Đang hoạt động"
    }

    errors = {}

    if request.method == "POST":

        form_data = {
            key: request.form.get(key, "").strip()
            for key in form_data
        }

        ma_bon = form_data["ma_bon"].upper()
        ten_bon = form_data["ten_bon"]
        nhien_lieu = form_data["nhien_lieu"]
        trang_thai = form_data["trang_thai"]

        if not ma_bon:
            errors["ma_bon"] = "Vui lòng nhập mã bồn."

        elif any(
            bon["ma_bon"].upper() == ma_bon
            for bon in lay_danh_sach_bon()
        ):
            errors["ma_bon"] = "Mã bồn này đã tồn tại."

        if not ten_bon:
            errors["ten_bon"] = "Vui lòng nhập tên bồn."

        if nhien_lieu not in {
            "RON 95",
            "E5 RON 92",
            "Diesel"
        }:
            errors["nhien_lieu"] = (
                "Vui lòng chọn loại nhiên liệu hợp lệ."
            )

        try:
            suc_chua = int(form_data["suc_chua"])

            if suc_chua <= 0:
                errors["suc_chua"] = (
                    "Sức chứa phải lớn hơn 0."
                )

        except (TypeError, ValueError):

            suc_chua = None

            errors["suc_chua"] = (
                "Sức chứa phải là số nguyên hợp lệ."
            )

        try:
            ton_hien_tai = int(
                form_data["ton_hien_tai"]
            )

            if ton_hien_tai < 0:
                errors["ton_hien_tai"] = (
                    "Tồn hiện tại không được nhỏ hơn 0."
                )

        except (TypeError, ValueError):

            ton_hien_tai = None

            errors["ton_hien_tai"] = (
                "Tồn hiện tại phải là số nguyên hợp lệ."
            )

        if (
            suc_chua is not None
            and ton_hien_tai is not None
            and ton_hien_tai > suc_chua
        ):
            errors["ton_hien_tai"] = (
                "Tồn hiện tại không được cao hơn sức chứa."
            )

        if trang_thai not in {
            "Đang hoạt động",
            "Ngừng hoạt động"
        }:
            errors["trang_thai"] = (
                "Trạng thái không hợp lệ."
            )

        form_data["ma_bon"] = ma_bon

        if errors:

            return render_template(
                "quanly/bonchua/them.html",
                trang_hien_tai="Bồn chứa",
                errors=errors,
                form_data=form_data
            ), 422

        ket_noi_db = ket_noi()
        cursor = ket_noi_db.cursor()

        cursor.execute(
            """
            INSERT INTO bon_chua
            (
                ma_bon,
                ten_bon,
                nhien_lieu,
                suc_chua,
                ton_hien_tai,
                trang_thai
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                ma_bon,
                ten_bon,
                nhien_lieu,
                int(suc_chua),
                int(ton_hien_tai),
                trang_thai
            )
        )

        ket_noi_db.commit()

        cursor.close()
        ket_noi_db.close()

        return redirect(
            url_for("bon_chua.danh_sach")
        )

    return render_template(
        "quanly/bonchua/them.html",
        trang_hien_tai="Bồn chứa",
        errors=errors,
        form_data=form_data
    )


@bon_chua_bp.route(
    "/bon-chua/sua/<int:id>",
    methods=["GET", "POST"]
)
def sua(id):

    ket_noi_db = ket_noi()

    cursor = ket_noi_db.cursor(
        dictionary=True
    )

    cursor.execute(
        "SELECT * FROM bon_chua WHERE id = %s",
        (id,)
    )

    bon = cursor.fetchone()

    cursor.close()
    ket_noi_db.close()

    if bon is None:
        return "Không tìm thấy bồn chứa", 404

    form_data = {
        "ma_bon": bon["ma_bon"],
        "ten_bon": bon["ten_bon"],
        "nhien_lieu": bon["nhien_lieu"],
        "suc_chua": bon["suc_chua"],
        "ton_hien_tai": bon["ton_hien_tai"],
        "trang_thai": bon["trang_thai"]
    }

    errors = {}

    if request.method == "POST":

        form_data = {
            key: request.form.get(key, "").strip()
            for key in form_data
        }

        ma_bon = form_data["ma_bon"].upper()
        ten_bon = form_data["ten_bon"]
        nhien_lieu = form_data["nhien_lieu"]
        trang_thai = form_data["trang_thai"]

        if not ma_bon:
            errors["ma_bon"] = (
                "Vui lòng nhập mã bồn."
            )

        elif any(
            bon["ma_bon"].upper() == ma_bon
            and bon["id"] != id
            for bon in lay_danh_sach_bon()
        ):
            errors["ma_bon"] = (
                "Mã bồn này đã tồn tại."
            )

        if not ten_bon:
            errors["ten_bon"] = (
                "Vui lòng nhập tên bồn."
            )

        if nhien_lieu not in {
            "RON 95",
            "E5 RON 92",
            "Diesel"
        }:
            errors["nhien_lieu"] = (
                "Vui lòng chọn loại nhiên liệu hợp lệ."
            )

        try:
            suc_chua = int(
                form_data["suc_chua"]
            )

            if suc_chua <= 0:
                errors["suc_chua"] = (
                    "Sức chứa phải lớn hơn 0."
                )

        except (TypeError, ValueError):

            suc_chua = None

            errors["suc_chua"] = (
                "Sức chứa phải là số nguyên hợp lệ."
            )

        try:
            ton_hien_tai = int(
                form_data["ton_hien_tai"]
            )

            if ton_hien_tai < 0:
                errors["ton_hien_tai"] = (
                    "Tồn hiện tại không được nhỏ hơn 0."
                )

        except (TypeError, ValueError):

            ton_hien_tai = None

            errors["ton_hien_tai"] = (
                "Tồn hiện tại phải là số nguyên hợp lệ."
            )

        if (
            suc_chua is not None
            and ton_hien_tai is not None
            and ton_hien_tai > suc_chua
        ):
            errors["ton_hien_tai"] = (
                "Tồn hiện tại không được cao hơn sức chứa."
            )

        if trang_thai not in {
            "Đang hoạt động",
            "Ngừng hoạt động"
        }:
            errors["trang_thai"] = (
                "Trạng thái không hợp lệ."
            )

        form_data["ma_bon"] = ma_bon

        if errors:

            return render_template(
                "quanly/bonchua/sua.html",
                trang_hien_tai="Bồn chứa",
                errors=errors,
                form_data=form_data,
                id=id
            ), 422

        ket_noi_db = ket_noi()

        cursor = ket_noi_db.cursor()

        cursor.execute(
            """
            UPDATE bon_chua
            SET ma_bon = %s,
                ten_bon = %s,
                nhien_lieu = %s,
                suc_chua = %s,
                ton_hien_tai = %s,
                trang_thai = %s
            WHERE id = %s
            """,
            (
                ma_bon,
                ten_bon,
                nhien_lieu,
                int(suc_chua),
                int(ton_hien_tai),
                trang_thai,
                id
            )
        )

        ket_noi_db.commit()

        cursor.close()
        ket_noi_db.close()

        return redirect(
            url_for("bon_chua.danh_sach")
        )

    return render_template(
        "quanly/bonchua/sua.html",
        trang_hien_tai="Bồn chứa",
        errors=errors,
        form_data=form_data,
        id=id
    )


@bon_chua_bp.route(
    "/bon-chua/xoa/<int:id>",
    methods=["POST"]
)
def xoa(id):

    ket_noi_db = ket_noi()

    cursor = ket_noi_db.cursor()

    cursor.execute(
        "DELETE FROM bon_chua WHERE id = %s",
        (id,)
    )

    ket_noi_db.commit()

    cursor.close()
    ket_noi_db.close()

    return redirect(
        url_for("bon_chua.danh_sach")
    )


@bon_chua_bp.route("/bon-chua/xem/<int:id>")
def xem(id):

    ket_noi_db = ket_noi()

    cursor = ket_noi_db.cursor(
        dictionary=True
    )

    cursor.execute(
        "SELECT * FROM bon_chua WHERE id = %s",
        (id,)
    )

    bon = cursor.fetchone()

    cursor.close()
    ket_noi_db.close()

    if bon is None:
        return "Không tìm thấy bồn chứa", 404

    return render_template(
        "quanly/bonchua/xem.html",
        trang_hien_tai="Bồn chứa",
        bon=bon
    )