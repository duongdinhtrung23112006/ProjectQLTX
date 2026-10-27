from datetime import datetime
from decimal import Decimal, InvalidOperation
import secrets

import mysql.connector
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from services.auth_service import yeu_cau_vai_tro
from services.database import ket_noi


nhanvien_ban_hang_bp = Blueprint(
    "nhanvien_ban_hang",
    __name__,
)

TRANG_THAI_CHO_DUYET = "Chờ duyệt"
TRANG_THAI_DA_DUYET = "Đã duyệt"
SO_LUONG_TOI_DA = 2147483647
THANH_TIEN_TOI_DA = Decimal("999999999999.99")


@nhanvien_ban_hang_bp.before_request
@yeu_cau_vai_tro("Nhân viên ca")
def bao_ve_router_ban_hang():
    return None


def mo_ket_noi():
    ket_noi_db = ket_noi()
    try:
        cursor = ket_noi_db.cursor(dictionary=True)
    except mysql.connector.Error:
        ket_noi_db.close()
        raise
    return ket_noi_db, cursor


def lay_nhan_vien_dang_dang_nhap(cursor):
    cursor.execute(
        """
        SELECT
            nv.id AS nhan_vien_id,
            nv.ma_nv,
            nv.ho_ten
        FROM tai_khoan tk
        JOIN nhan_vien nv
            ON nv.id = tk.nhan_vien_id
        WHERE tk.id = %s
          AND tk.vai_tro = 'Nhân viên ca'
          AND nv.trang_thai = 'Đang làm việc'
        """,
        (session.get("tai_khoan_id"),),
    )
    return cursor.fetchone()


def lay_du_lieu_form(cursor, nhan_vien_id, ngay_ban=None):
    if ngay_ban is None:
        cursor.execute(
            """
            SELECT id, ma_ca, ten_ca, ngay_lam_viec
            FROM ca_lam_viec
            WHERE nhan_vien_id = %s
              AND ngay_lam_viec = CURRENT_DATE()
              AND trang_thai = 'Đang hoạt động'
            ORDER BY id
            """,
            (nhan_vien_id,),
        )
    else:
        cursor.execute(
            """
            SELECT id, ma_ca, ten_ca, ngay_lam_viec
            FROM ca_lam_viec
            WHERE nhan_vien_id = %s
              AND ngay_lam_viec = %s
            ORDER BY id
            """,
            (nhan_vien_id, ngay_ban),
        )
    danh_sach_ca = cursor.fetchall()

    cursor.execute(
        """
        SELECT id, ma_nhien_lieu, ten_nhien_lieu, don_vi, don_gia
        FROM nhien_lieu
        WHERE trang_thai = 'Đang bán'
        ORDER BY ma_nhien_lieu
        """
    )
    danh_sach_nhien_lieu = cursor.fetchall()

    cursor.execute(
        """
        SELECT
            bc.id,
            bc.ma_bon,
            bc.ten_bon,
            bc.nhien_lieu_id,
            bc.ton_hien_tai,
            nl.ten_nhien_lieu,
            nl.don_vi
        FROM bon_chua bc
        JOIN nhien_lieu nl
            ON nl.id = bc.nhien_lieu_id
        WHERE bc.trang_thai = 'Đang hoạt động'
          AND nl.trang_thai = 'Đang bán'
        ORDER BY bc.ma_bon
        """
    )
    danh_sach_bon = cursor.fetchall()

    return danh_sach_ca, danh_sach_nhien_lieu, danh_sach_bon


def lay_form_data():
    return {
        "ca_lam_viec_id": request.form.get(
            "ca_lam_viec_id",
            "",
        ).strip(),
        "nhien_lieu_id": request.form.get(
            "nhien_lieu_id",
            "",
        ).strip(),
        "bon_id": request.form.get(
            "bon_id",
            "",
        ).strip(),
        "so_luong": request.form.get(
            "so_luong",
            "",
        ).strip(),
        "ghi_chu": request.form.get(
            "ghi_chu",
            "",
        ).strip(),
    }


def lay_id_hop_le(gia_tri):
    if not gia_tri or not gia_tri.isascii() or not gia_tri.isdecimal():
        return None

    try:
        gia_tri_int = int(gia_tri)
    except ValueError:
        return None

    return gia_tri_int if gia_tri_int > 0 else None


def kiem_tra_form(
    form_data,
    danh_sach_ca,
    danh_sach_nhien_lieu,
    danh_sach_bon,
):
    errors = {}
    ca_id = lay_id_hop_le(form_data["ca_lam_viec_id"])
    nhien_lieu_id = lay_id_hop_le(form_data["nhien_lieu_id"])
    bon_id = lay_id_hop_le(form_data["bon_id"])
    so_luong = None

    cac_ca_hop_le = {
        ca["id"]: ca
        for ca in danh_sach_ca
    }
    cac_nhien_lieu_hop_le = {
        nhien_lieu["id"]: nhien_lieu
        for nhien_lieu in danh_sach_nhien_lieu
    }
    cac_bon_hop_le = {
        bon["id"]: bon
        for bon in danh_sach_bon
    }

    if ca_id is None or ca_id not in cac_ca_hop_le:
        errors["ca_lam_viec_id"] = (
            "Vui lòng chọn ca đang hoạt động được phân công cho bạn hôm nay."
        )

    if nhien_lieu_id is None or nhien_lieu_id not in cac_nhien_lieu_hop_le:
        errors["nhien_lieu_id"] = (
            "Vui lòng chọn nhiên liệu đang được bán."
        )

    if bon_id is None or bon_id not in cac_bon_hop_le:
        errors["bon_id"] = (
            "Vui lòng chọn bồn chứa đang hoạt động."
        )

    if not form_data["so_luong"]:
        errors["so_luong"] = "Vui lòng nhập số lượng bán."
    elif (
        not form_data["so_luong"].isascii()
        or not form_data["so_luong"].isdecimal()
        or len(form_data["so_luong"]) > 10
    ):
        errors["so_luong"] = "Số lượng bán phải là số nguyên dương."
    else:
        so_luong = int(form_data["so_luong"])
        if so_luong <= 0 or so_luong > SO_LUONG_TOI_DA:
            errors["so_luong"] = (
                "Số lượng bán phải lớn hơn 0 và nằm trong giới hạn cho phép."
            )

    nhien_lieu = cac_nhien_lieu_hop_le.get(nhien_lieu_id)
    bon = cac_bon_hop_le.get(bon_id)
    if nhien_lieu and bon and bon["nhien_lieu_id"] != nhien_lieu_id:
        errors["bon_id"] = (
            "Bồn chứa không tương ứng với nhiên liệu đã chọn."
        )

    don_gia = None
    thanh_tien = None
    if nhien_lieu and so_luong is not None and not errors.get("so_luong"):
        try:
            don_gia = Decimal(str(nhien_lieu["don_gia"]))
        except (InvalidOperation, TypeError, ValueError):
            errors["nhien_lieu_id"] = (
                "Không thể xác định đơn giá hiện tại của nhiên liệu."
            )
        else:
            if not don_gia.is_finite() or don_gia < 0:
                errors["nhien_lieu_id"] = (
                    "Đơn giá nhiên liệu không hợp lệ."
                )
            else:
                thanh_tien = (don_gia * so_luong).quantize(
                    Decimal("0.01")
                )
                if thanh_tien > THANH_TIEN_TOI_DA:
                    errors["so_luong"] = (
                        "Thành tiền vượt giới hạn lưu trữ cho phép."
                    )

    canh_bao_ton = None
    if (
        bon
        and so_luong is not None
        and not errors.get("so_luong")
        and so_luong > bon["ton_hien_tai"]
    ):
        canh_bao_ton = (
            "Số lượng lớn hơn tồn bồn hiện tại để tham khảo. "
            "Phiếu vẫn chưa trừ tồn và có thể không được duyệt nếu "
            "tồn thực tế không đủ tại thời điểm duyệt."
        )

    du_lieu_hop_le = {
        "ca_lam_viec_id": ca_id,
        "nhien_lieu_id": nhien_lieu_id,
        "bon_id": bon_id,
        "so_luong": so_luong,
        "don_gia": don_gia,
        "thanh_tien": thanh_tien,
        "ghi_chu": form_data["ghi_chu"] or None,
    }
    return errors, du_lieu_hop_le, canh_bao_ton


def tao_ma_ban():
    return (
        "BH"
        + datetime.now().strftime("%y%m%d%H%M%S")
        + secrets.token_hex(3).upper()
    )


def render_form(
    *,
    trang,
    nhan_vien,
    danh_sach_ca,
    danh_sach_nhien_lieu,
    danh_sach_bon,
    form_data,
    errors,
    phieu=None,
    canh_bao_ton=None,
    status=200,
):
    return (
        render_template(
            (
                "nhanvien/banhang/sua.html"
                if phieu
                else "nhanvien/banhang/them.html"
            ),
            trang_hien_tai="Bán hàng",
            tieu_de=trang,
            nhan_vien=nhan_vien,
            danh_sach_ca=danh_sach_ca,
            danh_sach_nhien_lieu=danh_sach_nhien_lieu,
            danh_sach_bon=danh_sach_bon,
            form_data=form_data,
            errors=errors,
            phieu=phieu,
            canh_bao_ton=canh_bao_ton,
        ),
        status,
    )


@nhanvien_ban_hang_bp.route("/nhanvien/ban-hang")
def danh_sach():
    try:
        ket_noi_db, cursor = mo_ket_noi()
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi kết nối khi tải danh sách bán hàng")
        return "Không thể kết nối cơ sở dữ liệu để tải danh sách bán hàng.", 503

    try:
        nhan_vien = lay_nhan_vien_dang_dang_nhap(cursor)
        if nhan_vien is None:
            return "Không tìm thấy nhân viên đang đăng nhập.", 404

        cursor.execute(
            """
            SELECT
                COUNT(*) AS tong_so_phieu,
                COALESCE(
                    SUM(
                        CASE
                            WHEN trang_thai = 'Đã duyệt' THEN so_luong
                            ELSE 0
                        END
                    ),
                    0
                ) AS tong_so_luong_ban,
                COALESCE(
                    SUM(trang_thai = 'Chờ duyệt'),
                    0
                ) AS so_phieu_cho_duyet
            FROM ban_hang
            WHERE nhan_vien_id = %s
            """,
            (nhan_vien["nhan_vien_id"],),
        )
        thong_ke = cursor.fetchone()

        dieu_kien = ["bh.nhan_vien_id = %s"]
        tham_so = [nhan_vien["nhan_vien_id"]]
        tu_khoa = request.args.get("q", "").strip()
        trang_thai = request.args.get("trang_thai", "").strip()
        tu_ngay = request.args.get("tu_ngay", "").strip()
        den_ngay = request.args.get("den_ngay", "").strip()
        loi_loc = None

        if tu_khoa:
            dieu_kien.append(
                "(bh.ma_ban LIKE %s OR nl.ten_nhien_lieu LIKE %s "
                "OR bc.ma_bon LIKE %s OR bc.ten_bon LIKE %s)"
            )
            chuoi_tim_kiem = f"%{tu_khoa}%"
            tham_so.extend([chuoi_tim_kiem] * 4)

        if trang_thai:
            if trang_thai not in {
                TRANG_THAI_CHO_DUYET,
                TRANG_THAI_DA_DUYET,
            }:
                loi_loc = "Trạng thái lọc không hợp lệ."
            else:
                dieu_kien.append("bh.trang_thai = %s")
                tham_so.append(trang_thai)

        ngay_hop_le = {}
        for ten_truong, gia_tri in (
            ("tu_ngay", tu_ngay),
            ("den_ngay", den_ngay),
        ):
            if not gia_tri:
                continue
            try:
                ngay_hop_le[ten_truong] = datetime.strptime(
                    gia_tri,
                    "%Y-%m-%d",
                ).date()
            except ValueError:
                loi_loc = "Ngày lọc không hợp lệ."

        if (
            ngay_hop_le.get("tu_ngay")
            and ngay_hop_le.get("den_ngay")
            and ngay_hop_le["tu_ngay"] > ngay_hop_le["den_ngay"]
        ):
            loi_loc = "Ngày bắt đầu không được sau ngày kết thúc."
        else:
            if "tu_ngay" in ngay_hop_le:
                dieu_kien.append("bh.ngay_ban >= %s")
                tham_so.append(ngay_hop_le["tu_ngay"])
            if "den_ngay" in ngay_hop_le:
                dieu_kien.append("bh.ngay_ban <= %s")
                tham_so.append(ngay_hop_le["den_ngay"])

        cursor.execute(
            f"""
            SELECT
                bh.id,
                bh.ma_ban,
                bh.ngay_ban,
                bh.gio_ban,
                bh.so_luong,
                bh.don_gia,
                bh.thanh_tien,
                bh.trang_thai,
                ca.ten_ca,
                nv.ma_nv,
                nv.ho_ten,
                nl.ten_nhien_lieu,
                nl.don_vi,
                bc.ma_bon,
                bc.ten_bon
            FROM ban_hang bh
            JOIN ca_lam_viec ca
                ON ca.id = bh.ca_lam_viec_id
            JOIN nhan_vien nv
                ON nv.id = bh.nhan_vien_id
            JOIN nhien_lieu nl
                ON nl.id = bh.nhien_lieu_id
            JOIN bon_chua bc
                ON bc.id = bh.bon_id
            WHERE {" AND ".join(dieu_kien)}
            ORDER BY bh.ngay_ban DESC, bh.gio_ban DESC, bh.id DESC
            """,
            tuple(tham_so),
        )
        danh_sach_phieu = cursor.fetchall()

        return render_template(
            "nhanvien/banhang/index.html",
            trang_hien_tai="Bán hàng",
            nhan_vien=nhan_vien,
            danh_sach_phieu=danh_sach_phieu,
            tong_so_phieu=thong_ke["tong_so_phieu"],
            tong_so_luong_ban=thong_ke["tong_so_luong_ban"],
            so_phieu_cho_duyet=thong_ke["so_phieu_cho_duyet"],
            filters={
                "q": tu_khoa,
                "trang_thai": trang_thai,
                "tu_ngay": tu_ngay,
                "den_ngay": den_ngay,
            },
            loi_loc=loi_loc,
        )
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi tải danh sách phiếu bán hàng")
        return "Không thể tải danh sách phiếu bán hàng.", 503
    finally:
        cursor.close()
        ket_noi_db.close()


@nhanvien_ban_hang_bp.route(
    "/nhanvien/ban-hang/them",
    methods=["GET", "POST"],
)
def them():
    try:
        ket_noi_db, cursor = mo_ket_noi()
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi kết nối khi tạo phiếu bán hàng")
        return "Không thể kết nối cơ sở dữ liệu để tạo phiếu bán.", 503
    danh_sach_ca = []
    danh_sach_nhien_lieu = []
    danh_sach_bon = []
    form_data = {
        "ca_lam_viec_id": "",
        "nhien_lieu_id": "",
        "bon_id": "",
        "so_luong": "",
        "ghi_chu": "",
    }
    errors = {}
    canh_bao_ton = None

    try:
        if request.method == "POST":
            ket_noi_db.start_transaction()

        nhan_vien = lay_nhan_vien_dang_dang_nhap(cursor)
        if nhan_vien is None:
            return "Không tìm thấy nhân viên đang đăng nhập.", 404

        (
            danh_sach_ca,
            danh_sach_nhien_lieu,
            danh_sach_bon,
        ) = lay_du_lieu_form(cursor, nhan_vien["nhan_vien_id"])

        if request.method == "POST":
            form_data = lay_form_data()
            errors, du_lieu, canh_bao_ton = kiem_tra_form(
                form_data,
                danh_sach_ca,
                danh_sach_nhien_lieu,
                danh_sach_bon,
            )

            if not errors:
                for lan_thu in range(5):
                    ma_ban = tao_ma_ban()
                    try:
                        cursor.execute(
                            """
                            INSERT INTO ban_hang (
                                ma_ban,
                                ngay_ban,
                                gio_ban,
                                ca_lam_viec_id,
                                nhan_vien_id,
                                nhien_lieu_id,
                                bon_id,
                                so_luong,
                                don_gia,
                                thanh_tien,
                                ghi_chu,
                                trang_thai
                            )
                            VALUES (
                                %s,
                                CURRENT_DATE(),
                                CURRENT_TIME(),
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                'Chờ duyệt'
                            )
                            """,
                            (
                                ma_ban,
                                du_lieu["ca_lam_viec_id"],
                                nhan_vien["nhan_vien_id"],
                                du_lieu["nhien_lieu_id"],
                                du_lieu["bon_id"],
                                du_lieu["so_luong"],
                                du_lieu["don_gia"],
                                du_lieu["thanh_tien"],
                                du_lieu["ghi_chu"],
                            ),
                        )
                    except mysql.connector.IntegrityError as loi_db:
                        ket_noi_db.rollback()
                        if loi_db.errno == 1062 and lan_thu < 4:
                            continue
                        if loi_db.errno == 1062:
                            errors["database"] = (
                                "Không thể sinh mã phiếu bán duy nhất. "
                                "Vui lòng thử lại."
                            )
                            break
                        raise
                    else:
                        ket_noi_db.commit()
                        flash(
                            f"Đã tạo phiếu bán {ma_ban} ở trạng thái Chờ duyệt.",
                            "success",
                        )
                        return redirect(
                            url_for("nhanvien_ban_hang.danh_sach")
                        )

        return render_form(
            trang="Tạo phiếu bán",
            nhan_vien=nhan_vien,
            danh_sach_ca=danh_sach_ca,
            danh_sach_nhien_lieu=danh_sach_nhien_lieu,
            danh_sach_bon=danh_sach_bon,
            form_data=form_data,
            errors=errors,
            canh_bao_ton=canh_bao_ton,
            status=409 if errors.get("database") else 200,
        )
    except mysql.connector.Error:
        ket_noi_db.rollback()
        current_app.logger.exception("Lỗi tạo phiếu bán hàng")
        errors["database"] = (
            "Không thể lưu phiếu bán do lỗi cơ sở dữ liệu. "
            "Vui lòng kiểm tra dữ liệu và thử lại."
        )
        if "nhan_vien" not in locals() or nhan_vien is None:
            return "Không thể truy cập dữ liệu nhân viên.", 503
        return render_form(
            trang="Tạo phiếu bán",
            nhan_vien=nhan_vien,
            danh_sach_ca=danh_sach_ca,
            danh_sach_nhien_lieu=danh_sach_nhien_lieu,
            danh_sach_bon=danh_sach_bon,
            form_data=form_data,
            errors=errors,
            canh_bao_ton=canh_bao_ton,
            status=503,
        )
    finally:
        cursor.close()
        ket_noi_db.close()


@nhanvien_ban_hang_bp.route("/nhanvien/ban-hang/xem/<int:id>")
def xem(id):
    try:
        ket_noi_db, cursor = mo_ket_noi()
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi kết nối khi xem phiếu bán hàng")
        return "Không thể kết nối cơ sở dữ liệu để xem phiếu bán.", 503

    try:
        nhan_vien = lay_nhan_vien_dang_dang_nhap(cursor)
        if nhan_vien is None:
            return "Không tìm thấy nhân viên đang đăng nhập.", 404

        cursor.execute(
            """
            SELECT
                bh.id,
                bh.ma_ban,
                bh.ngay_ban,
                bh.gio_ban,
                bh.so_luong,
                bh.don_gia,
                bh.thanh_tien,
                bh.ghi_chu,
                bh.trang_thai,
                ca.ma_ca,
                ca.ten_ca,
                nv.ma_nv,
                nv.ho_ten,
                nl.ma_nhien_lieu,
                nl.ten_nhien_lieu,
                nl.don_vi,
                bc.ma_bon,
                bc.ten_bon,
                bc.ton_hien_tai
            FROM ban_hang bh
            JOIN ca_lam_viec ca
                ON ca.id = bh.ca_lam_viec_id
            JOIN nhan_vien nv
                ON nv.id = bh.nhan_vien_id
            JOIN nhien_lieu nl
                ON nl.id = bh.nhien_lieu_id
            JOIN bon_chua bc
                ON bc.id = bh.bon_id
            WHERE bh.id = %s
              AND bh.nhan_vien_id = %s
            """,
            (id, nhan_vien["nhan_vien_id"]),
        )
        phieu = cursor.fetchone()
        if phieu is None:
            return "Không tìm thấy phiếu bán.", 404

        return render_template(
            "nhanvien/banhang/xem.html",
            trang_hien_tai="Bán hàng",
            phieu=phieu,
        )
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi tải chi tiết phiếu bán hàng")
        return "Không thể tải chi tiết phiếu bán hàng.", 503
    finally:
        cursor.close()
        ket_noi_db.close()


@nhanvien_ban_hang_bp.route(
    "/nhanvien/ban-hang/sua/<int:id>",
    methods=["GET", "POST"],
)
def sua(id):
    try:
        ket_noi_db, cursor = mo_ket_noi()
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi kết nối khi sửa phiếu bán hàng")
        return "Không thể kết nối cơ sở dữ liệu để sửa phiếu bán.", 503
    danh_sach_ca = []
    danh_sach_nhien_lieu = []
    danh_sach_bon = []
    errors = {}
    canh_bao_ton = None

    try:
        if request.method == "POST":
            ket_noi_db.start_transaction()

        nhan_vien = lay_nhan_vien_dang_dang_nhap(cursor)
        if nhan_vien is None:
            return "Không tìm thấy nhân viên đang đăng nhập.", 404

        cursor.execute(
            """
            SELECT *
            FROM ban_hang
            WHERE id = %s
              AND nhan_vien_id = %s
            """,
            (id, nhan_vien["nhan_vien_id"]),
        )
        phieu = cursor.fetchone()
        if phieu is None:
            return "Không tìm thấy phiếu bán.", 404

        if phieu["trang_thai"] != TRANG_THAI_CHO_DUYET:
            return "Phiếu đã được xử lý và không thể chỉnh sửa.", 403

        (
            danh_sach_ca,
            danh_sach_nhien_lieu,
            danh_sach_bon,
        ) = lay_du_lieu_form(
            cursor,
            nhan_vien["nhan_vien_id"],
            phieu["ngay_ban"],
        )

        form_data = {
            "ca_lam_viec_id": str(phieu["ca_lam_viec_id"]),
            "nhien_lieu_id": str(phieu["nhien_lieu_id"]),
            "bon_id": str(phieu["bon_id"]),
            "so_luong": str(phieu["so_luong"]),
            "ghi_chu": phieu["ghi_chu"] or "",
        }

        if request.method == "POST":
            form_data = lay_form_data()
            errors, du_lieu, canh_bao_ton = kiem_tra_form(
                form_data,
                danh_sach_ca,
                danh_sach_nhien_lieu,
                danh_sach_bon,
            )

            if not errors:
                cursor.execute(
                    """
                    SELECT trang_thai
                    FROM ban_hang
                    WHERE id = %s
                      AND nhan_vien_id = %s
                    FOR UPDATE
                    """,
                    (id, nhan_vien["nhan_vien_id"]),
                )
                trang_thai_hien_tai = cursor.fetchone()

                if trang_thai_hien_tai is None:
                    return "Không tìm thấy phiếu bán.", 404
                if trang_thai_hien_tai["trang_thai"] != TRANG_THAI_CHO_DUYET:
                    return (
                        "Phiếu đã được duyệt trong lúc bạn đang chỉnh sửa "
                        "và không thể cập nhật.",
                        403,
                    )

                cursor.execute(
                    """
                    UPDATE ban_hang
                    SET
                        ca_lam_viec_id = %s,
                        nhien_lieu_id = %s,
                        bon_id = %s,
                        so_luong = %s,
                        don_gia = %s,
                        thanh_tien = %s,
                        ghi_chu = %s
                    WHERE id = %s
                      AND nhan_vien_id = %s
                      AND trang_thai = 'Chờ duyệt'
                    """,
                    (
                        du_lieu["ca_lam_viec_id"],
                        du_lieu["nhien_lieu_id"],
                        du_lieu["bon_id"],
                        du_lieu["so_luong"],
                        du_lieu["don_gia"],
                        du_lieu["thanh_tien"],
                        du_lieu["ghi_chu"],
                        id,
                        nhan_vien["nhan_vien_id"],
                    ),
                )
                ket_noi_db.commit()
                flash("Đã cập nhật phiếu bán.", "success")
                return redirect(url_for("nhanvien_ban_hang.danh_sach"))

        return render_form(
            trang="Sửa phiếu bán",
            nhan_vien=nhan_vien,
            danh_sach_ca=danh_sach_ca,
            danh_sach_nhien_lieu=danh_sach_nhien_lieu,
            danh_sach_bon=danh_sach_bon,
            form_data=form_data,
            errors=errors,
            phieu=phieu,
            canh_bao_ton=canh_bao_ton,
        )
    except mysql.connector.Error:
        ket_noi_db.rollback()
        current_app.logger.exception("Lỗi sửa phiếu bán hàng")
        return "Không thể cập nhật phiếu bán do lỗi cơ sở dữ liệu.", 503
    finally:
        cursor.close()
        ket_noi_db.close()


@nhanvien_ban_hang_bp.route(
    "/nhanvien/ban-hang/xoa/<int:id>",
    methods=["POST"],
)
def xoa(id):
    try:
        ket_noi_db, cursor = mo_ket_noi()
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi kết nối khi xóa phiếu bán hàng")
        return "Không thể kết nối cơ sở dữ liệu để xóa phiếu bán.", 503

    try:
        ket_noi_db.start_transaction()
        nhan_vien = lay_nhan_vien_dang_dang_nhap(cursor)
        if nhan_vien is None:
            return "Không tìm thấy nhân viên đang đăng nhập.", 404

        cursor.execute(
            """
            SELECT trang_thai
            FROM ban_hang
            WHERE id = %s
              AND nhan_vien_id = %s
            FOR UPDATE
            """,
            (id, nhan_vien["nhan_vien_id"]),
        )
        phieu = cursor.fetchone()

        if phieu is None:
            return "Không tìm thấy phiếu bán.", 404
        if phieu["trang_thai"] != TRANG_THAI_CHO_DUYET:
            return "Phiếu đã được xử lý và không thể xóa.", 403

        cursor.execute(
            """
            DELETE FROM ban_hang
            WHERE id = %s
              AND nhan_vien_id = %s
              AND trang_thai = 'Chờ duyệt'
            """,
            (id, nhan_vien["nhan_vien_id"]),
        )
        if cursor.rowcount != 1:
            ket_noi_db.rollback()
            return "Phiếu đã được xử lý và không thể xóa.", 403

        ket_noi_db.commit()
        flash("Đã xóa phiếu bán đang chờ duyệt.", "success")
        return redirect(url_for("nhanvien_ban_hang.danh_sach"))
    except mysql.connector.Error:
        ket_noi_db.rollback()
        current_app.logger.exception("Lỗi xóa phiếu bán hàng")
        flash("Không thể xóa phiếu bán do lỗi cơ sở dữ liệu.", "error")
        return redirect(url_for("nhanvien_ban_hang.danh_sach"))
    finally:
        cursor.close()
        ket_noi_db.close()
