from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from services.database import ket_noi
from services.auth_service import yeu_cau_vai_tro


nhap_hang_bp = Blueprint(
    "nhap_hang",
    __name__
)


@nhap_hang_bp.before_request
@yeu_cau_vai_tro("Quản lý")
def bao_ve_router_nhap_hang():
    return None


# =========================================================
# LẤY DANH SÁCH PHIẾU NHẬP
# =========================================================

def lay_danh_sach_phieu_nhap():
    ma_nhap = request.args.get(
        "ma_nhap",
        ""
    ).strip()

    ngay_tu = request.args.get(
        "ngay_tu",
        ""
    ).strip()

    ngay_den = request.args.get(
        "ngay_den",
        ""
    ).strip()

    trang_thai = request.args.get(
        "trang_thai",
        ""
    ).strip()

    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    try:
        sql = """
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

            WHERE 1 = 1
        """

        params = []

        # Tìm theo mã phiếu
        if ma_nhap:
            sql += """
                AND nh.ma_nhap LIKE %s
            """
            params.append(
                f"%{ma_nhap}%"
            )

        # Tìm từ ngày
        if ngay_tu:
            sql += """
                AND nh.ngay_tao >= %s
            """
            params.append(ngay_tu)

        # Tìm đến ngày
        if ngay_den:
            sql += """
                AND nh.ngay_tao <= %s
            """
            params.append(ngay_den)

        # Lọc trạng thái
        if trang_thai:
            sql += """
                AND nh.trang_thai = %s
            """
            params.append(trang_thai)

        # Phiếu chờ duyệt nằm trên cùng
        sql += """
            ORDER BY
                CASE
                    WHEN nh.trang_thai = 'Chờ duyệt'
                    THEN 0
                    ELSE 1
                END,
                nh.ngay_tao DESC,
                nh.id DESC
        """

        cursor.execute(
            sql,
            tuple(params)
        )

        return cursor.fetchall()

    finally:
        cursor.close()
        db.close()


# =========================================================
# DANH SÁCH
# =========================================================

@nhap_hang_bp.route(
    "/quanly/nhap-hang"
)
def danh_sach():

    danh_sach_phieu = (
        lay_danh_sach_phieu_nhap()
    )

    tong_so_phieu = len(
        danh_sach_phieu
    )

    cho_duyet = sum(
        1
        for phieu in danh_sach_phieu
        if phieu["trang_thai"] == "Chờ duyệt"
    )

    da_duyet = sum(
        1
        for phieu in danh_sach_phieu
        if phieu["trang_thai"] == "Đã duyệt"
    )

    tu_choi = sum(
        1
        for phieu in danh_sach_phieu
        if phieu["trang_thai"] == "Từ chối"
    )

    return render_template(
        "quanly/nhaphang/index.html",
        trang_hien_tai="Nhập hàng",
        danh_sach_phieu=danh_sach_phieu,
        tong_so_phieu=tong_so_phieu,
        cho_duyet=cho_duyet,
        da_duyet=da_duyet,
        tu_choi=tu_choi,
        ma_nhap=request.args.get(
            "ma_nhap",
            ""
        ),
        ngay_tu=request.args.get(
            "ngay_tu",
            ""
        ),
        ngay_den=request.args.get(
            "ngay_den",
            ""
        ),
        trang_thai=request.args.get(
            "trang_thai",
            ""
        )
    )


# =========================================================
# XEM CHI TIẾT PHIẾU
# =========================================================

@nhap_hang_bp.route(
    "/quanly/nhap-hang/xem/<int:id>"
)
def xem(id):

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
        """, (id,))

        phieu = cursor.fetchone()

    finally:
        cursor.close()
        db.close()

    if phieu is None:
        return "Không tìm thấy phiếu nhập.", 404

    return render_template(
        "quanly/nhaphang/xem.html",
        trang_hien_tai="Nhập hàng",
        phieu=phieu
    )


# =========================================================
# DUYỆT PHIẾU
# =========================================================

@nhap_hang_bp.route(
    "/quanly/nhap-hang/duyet/<int:id>",
    methods=["POST"]
)
def duyet(id):

    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    try:
        # 1. Lấy phiếu và khóa dòng phiếu
        cursor.execute("""
            SELECT
                nh.id,
                nh.so_luong,
                nh.trang_thai,
                nh.bon_id

            FROM nhap_hang nh

            WHERE nh.id = %s

            FOR UPDATE
        """, (id,))

        phieu = cursor.fetchone()

        if phieu is None:
            db.rollback()

            flash(
                "Không tìm thấy phiếu nhập.",
                "error"
            )

            return redirect(
                url_for(
                    "nhap_hang.danh_sach"
                )
            )

        # 2. Chỉ được duyệt phiếu Chờ duyệt
        if phieu["trang_thai"] != "Chờ duyệt":
            db.rollback()

            flash(
                "Phiếu này không còn ở trạng thái Chờ duyệt.",
                "error"
            )

            return redirect(
                url_for(
                    "nhap_hang.danh_sach"
                )
            )

        # 3. Khóa và lấy thông tin bồn
        cursor.execute("""
            SELECT
                id,
                ma_bon,
                suc_chua,
                ton_hien_tai

            FROM bon_chua

            WHERE id = %s

            FOR UPDATE
        """, (phieu["bon_id"],))

        bon = cursor.fetchone()

        if bon is None:
            db.rollback()

            flash(
                "Không tìm thấy bồn chứa.",
                "error"
            )

            return redirect(
                url_for(
                    "nhap_hang.danh_sach"
                )
            )

        # 4. Kiểm tra sức chứa
        ton_hien_tai = int(
            bon["ton_hien_tai"]
        )

        suc_chua = int(
            bon["suc_chua"]
        )

        so_luong_nhap = int(
            phieu["so_luong"]
        )

        ton_sau_khi_nhap = (
            ton_hien_tai
            + so_luong_nhap
        )

        if ton_sau_khi_nhap > suc_chua:
            db.rollback()

            flash(
                (
                    f"Bồn {bon['ma_bon']} "
                    f"không đủ sức chứa. "
                    f"Tồn hiện tại: {ton_hien_tai:,} lít, "
                    f"nhập thêm: {so_luong_nhap:,} lít, "
                    f"sức chứa: {suc_chua:,} lít."
                ),
                "error"
            )

            return redirect(
                url_for(
                    "nhap_hang.danh_sach"
                )
            )

        # 5. Cộng số lượng nhập vào tồn bồn
        cursor.execute("""
            UPDATE bon_chua

            SET ton_hien_tai =
                ton_hien_tai + %s

            WHERE id = %s
        """, (
            so_luong_nhap,
            phieu["bon_id"]
        ))

        # 6. Chuyển phiếu sang Đã duyệt
        cursor.execute("""
            UPDATE nhap_hang

            SET trang_thai = 'Đã duyệt'

            WHERE id = %s
                AND trang_thai = 'Chờ duyệt'
        """, (id,))

        # 7. Hoàn tất giao dịch
        db.commit()

        flash(
            (
                f"Đã duyệt phiếu nhập thành công. "
                f"Tồn bồn {bon['ma_bon']} "
                f"đã cộng thêm "
                f"{so_luong_nhap:,} lít."
            ),
            "success"
        )

    except Exception:
        db.rollback()

        flash(
            "Có lỗi xảy ra khi duyệt phiếu nhập.",
            "error"
        )

    finally:
        cursor.close()
        db.close()

    return redirect(
        url_for(
            "nhap_hang.danh_sach"
        )
    )


# =========================================================
# TỪ CHỐI PHIẾU
# =========================================================

@nhap_hang_bp.route(
    "/quanly/nhap-hang/tu-choi/<int:id>",
    methods=["POST"]
)
def tu_choi(id):

    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                trang_thai

            FROM nhap_hang

            WHERE id = %s

            FOR UPDATE
        """, (id,))

        phieu = cursor.fetchone()

        if phieu is None:
            db.rollback()

            flash(
                "Không tìm thấy phiếu nhập.",
                "error"
            )

            return redirect(
                url_for(
                    "nhap_hang.danh_sach"
                )
            )

        if phieu["trang_thai"] != "Chờ duyệt":
            db.rollback()

            flash(
                "Phiếu này không còn ở trạng thái Chờ duyệt.",
                "error"
            )

            return redirect(
                url_for(
                    "nhap_hang.danh_sach"
                )
            )

        cursor.execute("""
            UPDATE nhap_hang

            SET trang_thai = 'Từ chối'

            WHERE id = %s
                AND trang_thai = 'Chờ duyệt'
        """, (id,))

        db.commit()

        flash(
            "Đã từ chối phiếu nhập.",
            "success"
        )

    except Exception:
        db.rollback()

        flash(
            "Có lỗi xảy ra khi từ chối phiếu nhập.",
            "error"
        )

    finally:
        cursor.close()
        db.close()

    return redirect(
        url_for(
            "nhap_hang.danh_sach"
        )
    )

# =========================================================
# XÓA PHIẾU
# =========================================================

@nhap_hang_bp.route(
    "/quanly/nhap-hang/xoa/<int:id>",
    methods=["POST"]
)
def xoa(id):
    db = ket_noi()
    cursor = db.cursor(dictionary=True)

    try:
        # 1. Lấy phiếu và khóa dòng phiếu
        cursor.execute("""
            SELECT
                id,
                ma_nhap,
                trang_thai
            FROM nhap_hang
            WHERE id = %s
            FOR UPDATE
        """, (id,))

        phieu = cursor.fetchone()

        # 2. Không tìm thấy phiếu
        if phieu is None:
            db.rollback()

            flash(
                "Không tìm thấy phiếu nhập.",
                "error"
            )

            return redirect(
                url_for(
                    "nhap_hang.danh_sach"
                )
            )

        # 3. Chỉ cho xóa phiếu Chờ duyệt
        if phieu["trang_thai"] != "Chờ duyệt":
            db.rollback()

            flash(
                "Chỉ được xóa phiếu đang Chờ duyệt.",
                "error"
            )

            return redirect(
                url_for(
                    "nhap_hang.danh_sach"
                )
            )

        # 4. Xóa phiếu
        cursor.execute("""
            DELETE FROM nhap_hang
            WHERE id = %s
              AND trang_thai = 'Chờ duyệt'
        """, (id,))

        # 5. Hoàn tất
        db.commit()

        flash(
            f"Đã xóa phiếu nhập {phieu['ma_nhap']}.",
            "success"
        )

    except Exception:
        db.rollback()

        flash(
            "Có lỗi xảy ra khi xóa phiếu nhập.",
            "error"
        )

    finally:
        cursor.close()
        db.close()

    return redirect(
        url_for(
            "nhap_hang.danh_sach"
        )
    )