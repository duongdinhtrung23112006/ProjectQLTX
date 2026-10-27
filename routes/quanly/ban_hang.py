from datetime import datetime
from decimal import Decimal, InvalidOperation

import mysql.connector
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from services.auth_service import yeu_cau_vai_tro
from services.database import ket_noi


quanly_ban_hang_bp = Blueprint("quanly_ban_hang", __name__)

TRANG_THAI_CHO_DUYET = "Chờ duyệt"
TRANG_THAI_DA_DUYET = "Đã duyệt"
TRANG_THAI_DA_TU_CHOI = "Đã từ chối"
CAC_TRANG_THAI = {
    TRANG_THAI_CHO_DUYET,
    TRANG_THAI_DA_DUYET,
    TRANG_THAI_DA_TU_CHOI,
}


@quanly_ban_hang_bp.before_request
@yeu_cau_vai_tro("Quản lý")
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


def _quay_lai_danh_sach():
    return redirect(url_for("quanly_ban_hang.danh_sach"))


def _so_nguyen_duong(gia_tri):
    if isinstance(gia_tri, bool):
        return None
    if isinstance(gia_tri, int):
        so_luong = gia_tri
    elif (
        isinstance(gia_tri, str)
        and gia_tri.isascii()
        and gia_tri.isdecimal()
    ):
        so_luong = int(gia_tri)
    else:
        return None
    return so_luong if so_luong > 0 else None


def _thanh_tien_hop_le(don_gia, thanh_tien, so_luong):
    try:
        don_gia = Decimal(str(don_gia))
        thanh_tien = Decimal(str(thanh_tien))
    except (InvalidOperation, TypeError, ValueError):
        return False

    return (
        don_gia.is_finite()
        and thanh_tien.is_finite()
        and don_gia >= 0
        and thanh_tien >= 0
        and thanh_tien == (don_gia * so_luong).quantize(Decimal("0.01"))
    )


@quanly_ban_hang_bp.route("/quanly/ban-hang")
@quanly_ban_hang_bp.route("/ban-hang")
def danh_sach():
    try:
        ket_noi_db, cursor = mo_ket_noi()
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi kết nối khi tải danh sách bán hàng")
        return "Không thể kết nối cơ sở dữ liệu để tải danh sách bán hàng.", 503

    try:
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
                COALESCE(SUM(trang_thai = 'Chờ duyệt'), 0)
                    AS so_phieu_cho_duyet
            FROM ban_hang
            """
        )
        thong_ke = cursor.fetchone()

        dieu_kien = ["1 = 1"]
        tham_so = []
        tu_khoa = request.args.get("q", "").strip()
        trang_thai = request.args.get("trang_thai", "").strip()
        tu_ngay = request.args.get("tu_ngay", "").strip()
        den_ngay = request.args.get("den_ngay", "").strip()
        loi_loc = None

        if tu_khoa:
            dieu_kien.append(
                "(bh.ma_ban LIKE %s OR nl.ten_nhien_lieu LIKE %s "
                "OR bc.ma_bon LIKE %s OR bc.ten_bon LIKE %s "
                "OR nv.ho_ten LIKE %s OR nv.ma_nv LIKE %s)"
            )
            tham_so.extend([f"%{tu_khoa}%"] * 6)

        if trang_thai:
            if trang_thai not in CAC_TRANG_THAI:
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
            ORDER BY
                CASE WHEN bh.trang_thai = 'Chờ duyệt' THEN 0 ELSE 1 END,
                bh.ngay_ban DESC,
                bh.gio_ban DESC,
                bh.id DESC
            """,
            tuple(tham_so),
        )
        danh_sach_phieu = cursor.fetchall()

        return render_template(
            "quanly/banhang/index.html",
            trang_hien_tai="Bán hàng",
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


@quanly_ban_hang_bp.route("/quanly/ban-hang/xem/<int:id>")
@quanly_ban_hang_bp.route("/ban-hang/xem/<int:id>")
def xem(id):
    try:
        ket_noi_db, cursor = mo_ket_noi()
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi kết nối khi xem phiếu bán hàng")
        return "Không thể kết nối cơ sở dữ liệu để xem phiếu bán.", 503

    try:
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
            """,
            (id,),
        )
        phieu = cursor.fetchone()
        if phieu is None:
            return "Không tìm thấy phiếu bán.", 404

        return render_template(
            "quanly/banhang/xem.html",
            trang_hien_tai="Bán hàng",
            phieu=phieu,
        )
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi tải chi tiết phiếu bán hàng")
        return "Không thể tải chi tiết phiếu bán hàng.", 503
    finally:
        cursor.close()
        ket_noi_db.close()


@quanly_ban_hang_bp.route(
    "/quanly/ban-hang/duyet/<int:id>",
    methods=["POST"],
)
@quanly_ban_hang_bp.route("/ban-hang/duyet/<int:id>", methods=["POST"])
def duyet(id):
    try:
        ket_noi_db, cursor = mo_ket_noi()
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi kết nối khi duyệt phiếu bán")
        flash("Không thể kết nối cơ sở dữ liệu để duyệt phiếu bán.", "error")
        return _quay_lai_danh_sach()

    try:
        ket_noi_db.start_transaction()
        cursor.execute(
            """
            SELECT
                id,
                ma_ban,
                bon_id,
                nhien_lieu_id,
                so_luong,
                don_gia,
                thanh_tien,
                trang_thai
            FROM ban_hang
            WHERE id = %s
            FOR UPDATE
            """,
            (id,),
        )
        phieu = cursor.fetchone()
        if phieu is None:
            ket_noi_db.rollback()
            flash("Không tìm thấy phiếu bán.", "error")
            return _quay_lai_danh_sach()
        if phieu["trang_thai"] != TRANG_THAI_CHO_DUYET:
            ket_noi_db.rollback()
            flash("Phiếu này không còn ở trạng thái Chờ duyệt.", "error")
            return _quay_lai_danh_sach()

        so_luong = _so_nguyen_duong(phieu["so_luong"])
        if so_luong is None:
            ket_noi_db.rollback()
            flash("Số lượng trong phiếu bán không hợp lệ.", "error")
            return _quay_lai_danh_sach()
        if not _thanh_tien_hop_le(
            phieu["don_gia"],
            phieu["thanh_tien"],
            so_luong,
        ):
            ket_noi_db.rollback()
            flash("Đơn giá hoặc thành tiền trong phiếu bán không hợp lệ.", "error")
            return _quay_lai_danh_sach()

        cursor.execute(
            """
            SELECT id, nhien_lieu_id, ton_hien_tai, trang_thai
            FROM bon_chua
            WHERE id = %s
            FOR UPDATE
            """,
            (phieu["bon_id"],),
        )
        bon = cursor.fetchone()
        if bon is None:
            ket_noi_db.rollback()
            flash("Không tìm thấy bồn chứa của phiếu bán.", "error")
            return _quay_lai_danh_sach()
        if (
            bon["trang_thai"] != "Đang hoạt động"
            or bon["nhien_lieu_id"] != phieu["nhien_lieu_id"]
        ):
            ket_noi_db.rollback()
            flash("Bồn chứa không hoạt động hoặc không khớp nhiên liệu.", "error")
            return _quay_lai_danh_sach()

        cursor.execute(
            """
            SELECT id, trang_thai
            FROM nhien_lieu
            WHERE id = %s
            FOR UPDATE
            """,
            (phieu["nhien_lieu_id"],),
        )
        nhien_lieu = cursor.fetchone()
        if nhien_lieu is None or nhien_lieu["trang_thai"] != "Đang bán":
            ket_noi_db.rollback()
            flash("Nhiên liệu của phiếu không còn được bán.", "error")
            return _quay_lai_danh_sach()

        ton_hien_tai = _so_nguyen_duong(bon["ton_hien_tai"])
        if ton_hien_tai is None or ton_hien_tai < so_luong:
            ket_noi_db.rollback()
            flash("Tồn bồn hiện tại không đủ để duyệt phiếu bán.", "error")
            return _quay_lai_danh_sach()

        cursor.execute(
            """
            UPDATE bon_chua
            SET ton_hien_tai = ton_hien_tai - %s
            WHERE id = %s
              AND nhien_lieu_id = %s
              AND trang_thai = 'Đang hoạt động'
              AND ton_hien_tai >= %s
            """,
            (so_luong, phieu["bon_id"], phieu["nhien_lieu_id"], so_luong),
        )
        if cursor.rowcount != 1:
            ket_noi_db.rollback()
            flash("Tồn bồn đã thay đổi; không thể duyệt phiếu bán.", "error")
            return _quay_lai_danh_sach()

        cursor.execute(
            """
            UPDATE ban_hang
            SET trang_thai = 'Đã duyệt'
            WHERE id = %s
              AND trang_thai = 'Chờ duyệt'
            """,
            (id,),
        )
        if cursor.rowcount != 1:
            ket_noi_db.rollback()
            flash("Phiếu bán đã được xử lý; không thể duyệt lại.", "error")
            return _quay_lai_danh_sach()

        ket_noi_db.commit()
        flash(
            f"Đã duyệt phiếu bán {phieu['ma_ban']} và trừ "
            f"{so_luong:,} lít khỏi tồn bồn.",
            "success",
        )
    except mysql.connector.Error:
        ket_noi_db.rollback()
        current_app.logger.exception("Lỗi duyệt phiếu bán hàng")
        flash("Không thể duyệt phiếu bán do lỗi cơ sở dữ liệu.", "error")
    finally:
        cursor.close()
        ket_noi_db.close()

    return _quay_lai_danh_sach()


@quanly_ban_hang_bp.route(
    "/quanly/ban-hang/tu-choi/<int:id>",
    methods=["POST"],
)
@quanly_ban_hang_bp.route("/ban-hang/tu-choi/<int:id>", methods=["POST"])
def tu_choi(id):
    try:
        ket_noi_db, cursor = mo_ket_noi()
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi kết nối khi từ chối phiếu bán")
        flash("Không thể kết nối cơ sở dữ liệu để từ chối phiếu bán.", "error")
        return _quay_lai_danh_sach()

    try:
        ket_noi_db.start_transaction()
        cursor.execute(
            """
            SELECT id, ma_ban, trang_thai
            FROM ban_hang
            WHERE id = %s
            FOR UPDATE
            """,
            (id,),
        )
        phieu = cursor.fetchone()
        if phieu is None:
            ket_noi_db.rollback()
            flash("Không tìm thấy phiếu bán.", "error")
            return _quay_lai_danh_sach()
        if phieu["trang_thai"] != TRANG_THAI_CHO_DUYET:
            ket_noi_db.rollback()
            flash("Phiếu này không còn ở trạng thái Chờ duyệt.", "error")
            return _quay_lai_danh_sach()

        cursor.execute(
            """
            UPDATE ban_hang
            SET trang_thai = 'Đã từ chối'
            WHERE id = %s
              AND trang_thai = 'Chờ duyệt'
            """,
            (id,),
        )
        if cursor.rowcount != 1:
            ket_noi_db.rollback()
            flash("Phiếu bán đã được xử lý; không thể từ chối lại.", "error")
            return _quay_lai_danh_sach()

        ket_noi_db.commit()
        flash(f"Đã từ chối phiếu bán {phieu['ma_ban']}.", "success")
    except mysql.connector.Error:
        ket_noi_db.rollback()
        current_app.logger.exception("Lỗi từ chối phiếu bán hàng")
        flash("Không thể từ chối phiếu bán do lỗi cơ sở dữ liệu.", "error")
    finally:
        cursor.close()
        ket_noi_db.close()

    return _quay_lai_danh_sach()


@quanly_ban_hang_bp.route(
    "/quanly/ban-hang/xoa/<int:id>",
    methods=["POST"],
)
@quanly_ban_hang_bp.route("/ban-hang/xoa/<int:id>", methods=["POST"])
def xoa(id):
    try:
        ket_noi_db, cursor = mo_ket_noi()
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi kết nối khi xóa phiếu bán")
        flash("Không thể kết nối cơ sở dữ liệu để xóa phiếu bán.", "error")
        return _quay_lai_danh_sach()

    try:
        ket_noi_db.start_transaction()
        cursor.execute(
            """
            SELECT id, ma_ban, bon_id, so_luong, trang_thai
            FROM ban_hang
            WHERE id = %s
            FOR UPDATE
            """,
            (id,),
        )
        phieu = cursor.fetchone()
        if phieu is None:
            ket_noi_db.rollback()
            flash("Không tìm thấy phiếu bán.", "error")
            return _quay_lai_danh_sach()
        if phieu["trang_thai"] not in CAC_TRANG_THAI:
            ket_noi_db.rollback()
            flash("Trạng thái phiếu bán không hợp lệ; không thể xóa.", "error")
            return _quay_lai_danh_sach()

        if phieu["trang_thai"] == TRANG_THAI_DA_DUYET:
            so_luong = _so_nguyen_duong(phieu["so_luong"])
            if so_luong is None:
                ket_noi_db.rollback()
                flash("Số lượng trong phiếu bán không hợp lệ.", "error")
                return _quay_lai_danh_sach()

            cursor.execute(
                """
                SELECT id, suc_chua, ton_hien_tai
                FROM bon_chua
                WHERE id = %s
                FOR UPDATE
                """,
                (phieu["bon_id"],),
            )
            bon = cursor.fetchone()
            if bon is None:
                ket_noi_db.rollback()
                flash("Không tìm thấy bồn chứa để hoàn trả tồn.", "error")
                return _quay_lai_danh_sach()

            try:
                suc_chua = int(bon["suc_chua"])
                ton_hien_tai = int(bon["ton_hien_tai"])
            except (TypeError, ValueError, OverflowError):
                suc_chua = ton_hien_tai = -1

            if (
                suc_chua < 0
                or ton_hien_tai < 0
                or ton_hien_tai + so_luong > suc_chua
            ):
                ket_noi_db.rollback()
                flash(
                    "Không thể xóa phiếu vì hoàn trả số lượng sẽ vượt sức chứa bồn.",
                    "error",
                )
                return _quay_lai_danh_sach()

            cursor.execute(
                """
                UPDATE bon_chua
                SET ton_hien_tai = ton_hien_tai + %s
                WHERE id = %s
                  AND ton_hien_tai + %s <= suc_chua
                """,
                (so_luong, phieu["bon_id"], so_luong),
            )
            if cursor.rowcount != 1:
                ket_noi_db.rollback()
                flash("Tồn bồn đã thay đổi; không thể xóa phiếu bán.", "error")
                return _quay_lai_danh_sach()

        cursor.execute(
            "DELETE FROM ban_hang WHERE id = %s AND trang_thai = %s",
            (id, phieu["trang_thai"]),
        )
        if cursor.rowcount != 1:
            ket_noi_db.rollback()
            flash("Phiếu bán đã thay đổi; không thể xóa.", "error")
            return _quay_lai_danh_sach()

        ket_noi_db.commit()
        flash(f"Đã xóa phiếu bán {phieu['ma_ban']}.", "success")
    except mysql.connector.Error:
        ket_noi_db.rollback()
        current_app.logger.exception("Lỗi xóa phiếu bán hàng")
        flash("Không thể xóa phiếu bán do lỗi cơ sở dữ liệu.", "error")
    finally:
        cursor.close()
        ket_noi_db.close()

    return _quay_lai_danh_sach()
