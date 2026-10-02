from flask import Blueprint, render_template, request, redirect, url_for

from services.database import ket_noi
from services.auth_service import yeu_cau_vai_tro


ca_lam_viec_bp = Blueprint(
    "ca_lam_viec",
    __name__
)


@ca_lam_viec_bp.before_request
@yeu_cau_vai_tro("Quản lý")
def bao_ve_router_ca_lam_viec():
    return None


SHIFT_RULES = {
    "Ca Sáng": {
        "ma": "SANG",
        "bat_dau": "06:00:00",
        "ket_thuc": "12:00:00"
    },
    "Ca Chiều": {
        "ma": "CHIEU",
        "bat_dau": "12:00:00",
        "ket_thuc": "18:00:00"
    },
    "Ca Tối": {
        "ma": "TOI",
        "bat_dau": "18:00:00",
        "ket_thuc": "23:59:00"
    }
}


def lay_danh_sach_nhan_vien():
    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            nv.id,
            nv.ma_nv,
            nv.ho_ten
        FROM nhan_vien nv
        INNER JOIN tai_khoan tk
            ON nv.id = tk.nhan_vien_id
        WHERE nv.trang_thai = 'Đang làm việc'
          AND tk.vai_tro = 'Nhân viên ca'
        ORDER BY nv.ho_ten
    """)

    danh_sach = cursor.fetchall()

    cursor.close()
    db.close()

    return danh_sach


def lay_danh_sach_ca():
    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            ca.id,
            ca.ma_ca,
            ca.ten_ca,
            ca.ngay_lam_viec,
            ca.nhan_vien_id,
            ca.trang_thai,
            nv.ma_nv,
            nv.ho_ten
        FROM ca_lam_viec ca
        INNER JOIN nhan_vien nv
            ON ca.nhan_vien_id = nv.id
        ORDER BY
            ca.ngay_lam_viec ASC,
            ca.id ASC
    """)

    danh_sach = cursor.fetchall()

    cursor.close()
    db.close()

    for ca in danh_sach:

        quy_tac = SHIFT_RULES.get(
            ca["ten_ca"]
        )

        if quy_tac:

            ca["thoi_gian_bat_dau"] = (
                quy_tac["bat_dau"]
            )

            ca["thoi_gian_ket_thuc"] = (
                quy_tac["ket_thuc"]
            )

        else:

            ca["thoi_gian_bat_dau"] = None
            ca["thoi_gian_ket_thuc"] = None

        ca["nhan_vien_text"] = (
            f'{ca["ho_ten"]} ({ca["ma_nv"]})'
        )

    return danh_sach


def lay_form_data():

    ten_ca = request.form.get(
        "ten_ca",
        ""
    ).strip()

    quy_tac = SHIFT_RULES.get(
        ten_ca
    )

    return {
        "ma_ca": (
            quy_tac["ma"]
            if quy_tac
            else ""
        ),

        "ten_ca": ten_ca,

        "ngay_lam_viec": request.form.get(
            "ngay_lam_viec",
            ""
        ).strip(),

        "nhan_vien_id": request.form.get(
            "nhan_vien_id",
            ""
        ).strip(),

        "trang_thai": request.form.get(
            "trang_thai",
            ""
        ).strip()
    }


def kiem_tra(
    form_data,
    danh_sach_nhan_vien,
    ca_id=None
):

    errors = {}

    if form_data["ten_ca"] not in SHIFT_RULES:

        errors["ten_ca"] = (
            "Vui lòng chọn tên ca làm việc."
        )

    if not form_data["ngay_lam_viec"]:

        errors["ngay_lam_viec"] = (
            "Vui lòng chọn ngày làm việc."
        )

    if ca_id is None:

        if not form_data["nhan_vien_id"]:

            errors["nhan_vien_id"] = (
                "Vui lòng chọn nhân viên."
            )

        else:

            id_hop_le = {
                str(nhan_vien["id"])
                for nhan_vien in danh_sach_nhan_vien
            }

            if form_data["nhan_vien_id"] not in id_hop_le:

                errors["nhan_vien_id"] = (
                    "Nhân viên không hợp lệ."
                )

    if form_data["trang_thai"] not in {
        "Đang hoạt động",
        "Đã đóng"
    }:

        errors["trang_thai"] = (
            "Trạng thái không hợp lệ."
        )

    if not errors:

        db = ket_noi()
        cursor = db.cursor(
            dictionary=True
        )

        if ca_id is None:

            cursor.execute("""
                SELECT id
                FROM ca_lam_viec
                WHERE ten_ca = %s
                  AND ngay_lam_viec = %s
            """, (
                form_data["ten_ca"],
                form_data["ngay_lam_viec"]
            ))

        else:

            cursor.execute("""
                SELECT id
                FROM ca_lam_viec
                WHERE ten_ca = %s
                  AND ngay_lam_viec = %s
                  AND id != %s
            """, (
                form_data["ten_ca"],
                form_data["ngay_lam_viec"],
                ca_id
            ))

        ca_trung = cursor.fetchone()

        cursor.close()
        db.close()

        if ca_trung:

            errors["ten_ca"] = (
                "Ca làm việc này đã tồn tại "
                "trong ngày đã chọn."
            )

    return errors


@ca_lam_viec_bp.route("/ca-lam-viec")
def danh_sach():

    danh_sach_ca = (
        lay_danh_sach_ca()
    )

    return render_template(
        "quanly/calamviec/index.html",

        trang_hien_tai="Ca làm việc",

        danh_sach_ca=danh_sach_ca,

        tong_so_ca=len(
            danh_sach_ca
        ),

        dang_hoat_dong=sum(
            ca["trang_thai"] == "Đang hoạt động"
            for ca in danh_sach_ca
        ),

        da_dong=sum(
            ca["trang_thai"] == "Đã đóng"
            for ca in danh_sach_ca
        )
    )


@ca_lam_viec_bp.route(
    "/ca-lam-viec/them",
    methods=["GET", "POST"]
)
def them():

    danh_sach_nhan_vien = (
        lay_danh_sach_nhan_vien()
    )

    form_data = {
        "ma_ca": "",
        "ten_ca": "",
        "ngay_lam_viec": "",
        "nhan_vien_id": "",
        "trang_thai": "Đang hoạt động"
    }

    errors = {}

    if request.method == "POST":

        form_data = lay_form_data()

        errors = kiem_tra(
            form_data,
            danh_sach_nhan_vien
        )

        if not errors:

            db = ket_noi()
            cursor = db.cursor()

            cursor.execute("""
                INSERT INTO ca_lam_viec
                (
                    ma_ca,
                    ten_ca,
                    ngay_lam_viec,
                    nhan_vien_id,
                    trang_thai
                )
                VALUES (%s, %s, %s, %s, %s)
            """, (
                form_data["ma_ca"],
                form_data["ten_ca"],
                form_data["ngay_lam_viec"],
                int(
                    form_data["nhan_vien_id"]
                ),
                form_data["trang_thai"]
            ))

            db.commit()

            cursor.close()
            db.close()

            return redirect(
                url_for(
                    "ca_lam_viec.danh_sach"
                )
            )

    return render_template(
        "quanly/calamviec/them.html",

        trang_hien_tai="Ca làm việc",

        form_data=form_data,

        errors=errors,

        danh_sach_nhan_vien=danh_sach_nhan_vien,

        shift_options=sorted(
            SHIFT_RULES
        )
    )


@ca_lam_viec_bp.route(
    "/ca-lam-viec/sua/<int:id>",
    methods=["GET", "POST"]
)
def sua(id):

    db = ket_noi()
    cursor = db.cursor(
        dictionary=True
    )

    cursor.execute(
        "SELECT * FROM ca_lam_viec WHERE id = %s",
        (id,)
    )

    ca = cursor.fetchone()

    cursor.close()
    db.close()

    if ca is None:
        return (
            "Không tìm thấy ca làm việc",
            404
        )

    danh_sach_nhan_vien = (
        lay_danh_sach_nhan_vien()
    )

    form_data = {
        "ma_ca": ca["ma_ca"],

        "ten_ca": ca["ten_ca"],

        "ngay_lam_viec":
            ca["ngay_lam_viec"].strftime(
                "%Y-%m-%d"
            ),

        "nhan_vien_id":
            str(ca["nhan_vien_id"]),

        "trang_thai":
            ca["trang_thai"]
    }

    errors = {}

    if request.method == "POST":

        form_data = lay_form_data()

        form_data["nhan_vien_id"] = str(
            ca["nhan_vien_id"]
        )

        errors = kiem_tra(
            form_data,
            danh_sach_nhan_vien,
            id
        )

        if not errors:

            db = ket_noi()
            cursor = db.cursor()

            cursor.execute("""
                UPDATE ca_lam_viec
                SET
                    ma_ca = %s,
                    ten_ca = %s,
                    ngay_lam_viec = %s,
                    trang_thai = %s
                WHERE id = %s
            """, (
                form_data["ma_ca"],
                form_data["ten_ca"],
                form_data["ngay_lam_viec"],
                form_data["trang_thai"],
                id
            ))

            db.commit()

            cursor.close()
            db.close()

            return redirect(
                url_for(
                    "ca_lam_viec.danh_sach"
                )
            )

    return render_template(
        "quanly/calamviec/sua.html",

        trang_hien_tai="Ca làm việc",

        form_data=form_data,

        errors=errors,

        danh_sach_nhan_vien=danh_sach_nhan_vien,

        id=id,

        shift_options=sorted(
            SHIFT_RULES
        )
    )


@ca_lam_viec_bp.route(
    "/ca-lam-viec/xoa/<int:id>",
    methods=["POST"]
)
def xoa(id):

    db = ket_noi()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM ca_lam_viec WHERE id = %s",
        (id,)
    )

    db.commit()

    cursor.close()
    db.close()

    return redirect(
        url_for(
            "ca_lam_viec.danh_sach"
        )
    )


@ca_lam_viec_bp.route(
    "/ca-lam-viec/xem/<int:id>"
)
def xem(id):

    db = ket_noi()
    cursor = db.cursor(
        dictionary=True
    )

    cursor.execute("""
        SELECT
            ca.id,
            ca.ma_ca,
            ca.ten_ca,
            ca.ngay_lam_viec,
            ca.nhan_vien_id,
            ca.trang_thai,
            nv.ma_nv,
            nv.ho_ten,
            nv.so_dien_thoai,
            nv.chuc_vu
        FROM ca_lam_viec ca
        INNER JOIN nhan_vien nv
            ON ca.nhan_vien_id = nv.id
        WHERE ca.id = %s
    """, (id,))

    ca = cursor.fetchone()

    cursor.close()
    db.close()

    if ca is None:
        return (
            "Không tìm thấy ca làm việc",
            404
        )

    quy_tac = SHIFT_RULES.get(
        ca["ten_ca"]
    )

    if quy_tac:

        ca["thoi_gian_bat_dau"] = (
            quy_tac["bat_dau"]
        )

        ca["thoi_gian_ket_thuc"] = (
            quy_tac["ket_thuc"]
        )

    else:

        ca["thoi_gian_bat_dau"] = None
        ca["thoi_gian_ket_thuc"] = None

    return render_template(
        "quanly/calamviec/xem.html",

        trang_hien_tai="Ca làm việc",

        ca=ca
    )