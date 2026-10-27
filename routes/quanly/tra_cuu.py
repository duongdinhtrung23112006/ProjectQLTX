import mysql.connector
from flask import Blueprint, current_app, render_template, request, url_for

from services.auth_service import yeu_cau_vai_tro
from services.tra_cuu import lay_chi_tiet, lay_trang_tra_cuu


quanly_tra_cuu_bp = Blueprint("quanly_tra_cuu", __name__)


@quanly_tra_cuu_bp.before_request
@yeu_cau_vai_tro("Quản lý")
def bao_ve_route_tra_cuu():
    return None


@quanly_tra_cuu_bp.route("/quanly/tra-cuu")
def danh_sach():
    try:
        du_lieu = lay_trang_tra_cuu(request.args)
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi tải trang tra cứu số liệu quản lý")
        return "Không thể tải dữ liệu tra cứu.", 503

    return render_template(
        "quanly/tra_cuu/index.html",
        **du_lieu,
        trang_hien_tai="Tra cứu",
        endpoint_danh_sach="quanly_tra_cuu.danh_sach",
        endpoint_chi_tiet="quanly_tra_cuu.xem",
        vai_tro="Quản lý",
    )


@quanly_tra_cuu_bp.route("/quanly/tra-cuu/xem/<loai_giao_dich>/<int:id>")
def xem(loai_giao_dich, id):
    try:
        giao_dich = lay_chi_tiet(loai_giao_dich, id)
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi tải chi tiết giao dịch tra cứu quản lý")
        return "Không thể tải chi tiết giao dịch.", 503

    if giao_dich is None:
        return "Không tìm thấy giao dịch.", 404

    return render_template(
        "quanly/tra_cuu/xem.html",
        giao_dich=giao_dich,
        trang_hien_tai="Tra cứu",
        endpoint_danh_sach="quanly_tra_cuu.danh_sach",
        back_url=url_for(
            "quanly_tra_cuu.danh_sach",
            **request.args.to_dict(flat=True),
        ),
    )
