import mysql.connector
from flask import Blueprint, current_app, render_template, request, url_for

from services.auth_service import yeu_cau_vai_tro
from services.thong_ke import lay_chi_tiet_giao_dich, lay_du_lieu_thong_ke


quanly_thong_ke_bp = Blueprint("quanly_thong_ke", __name__)


@quanly_thong_ke_bp.before_request
@yeu_cau_vai_tro("Quản lý")
def bao_ve_route_thong_ke():
    return None


@quanly_thong_ke_bp.route("/quanly/thong-ke")
def danh_sach():
    try:
        du_lieu = lay_du_lieu_thong_ke(request.args)
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi tải dashboard thống kê quản lý")
        return "Không thể tải dữ liệu thống kê.", 503

    for canh_bao in du_lieu["canh_bao"]:
        if canh_bao.get("loai") == "bon":
            canh_bao["url"] = url_for(
                "quanly_ton_bon.xem",
                id=canh_bao["bon_id"],
            )
        elif canh_bao.get("loai") == "giao_dich":
            canh_bao["url"] = url_for("quanly_tra_cuu.danh_sach")

    return render_template(
        "quanly/thongke/index.html",
        **du_lieu,
        trang_hien_tai="Thống kê",
        endpoint_danh_sach="quanly_thong_ke.danh_sach",
        endpoint_chi_tiet="quanly_thong_ke.xem",
        endpoint_ton_bon="quanly_ton_bon.danh_sach",
        endpoint_tra_cuu="quanly_tra_cuu.danh_sach",
    )


@quanly_thong_ke_bp.route("/quanly/thong-ke/xem/<loai_giao_dich>/<int:id>")
def xem(loai_giao_dich, id):
    try:
        giao_dich = lay_chi_tiet_giao_dich(loai_giao_dich, id)
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi tải chi tiết giao dịch thống kê quản lý")
        return "Không thể tải chi tiết giao dịch.", 503

    if giao_dich is None:
        return "Không tìm thấy giao dịch.", 404

    return render_template(
        "quanly/thongke/xem.html",
        giao_dich=giao_dich,
        trang_hien_tai="Thống kê",
        back_url=url_for(
            "quanly_thong_ke.danh_sach",
            **request.args.to_dict(flat=True),
        ),
    )
