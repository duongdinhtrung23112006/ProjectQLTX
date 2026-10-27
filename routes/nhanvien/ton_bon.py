import mysql.connector
from flask import Blueprint, current_app, render_template, request

from services.auth_service import yeu_cau_vai_tro
from services.ton_bon import (
    NGUONG_BON_GAN_HET,
    lay_chi_tiet_bon,
    lay_du_lieu_ton_bon,
)


nhanvien_ton_bon_bp = Blueprint("nhanvien_ton_bon", __name__)


@nhanvien_ton_bon_bp.before_request
@yeu_cau_vai_tro("Nhân viên ca")
def bao_ve_router_ton_bon():
    return None


def _tham_so_trang():
    return {
        "layout_template": "nhanvien/khungnhanvien.html",
        "trang_hien_tai": "Tồn bồn",
        "endpoint_danh_sach": "nhanvien_ton_bon.danh_sach",
        "endpoint_chi_tiet": "nhanvien_ton_bon.xem",
        "vai_tro": "Nhân viên ca",
        "nguong_bon_gan_het": NGUONG_BON_GAN_HET,
    }


@nhanvien_ton_bon_bp.route("/nhanvien/ton-bon")
def danh_sach():
    try:
        du_lieu = lay_du_lieu_ton_bon(
            tu_khoa=request.args.get("q", "").strip(),
            nhien_lieu_id=request.args.get("nhien_lieu_id", "").strip(),
            trang_thai=request.args.get("trang_thai", "").strip(),
        )
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi tải danh sách tồn bồn nhân viên")
        return "Không thể tải dữ liệu tồn bồn.", 503

    return render_template(
        "nhanvien/tonbon/index.html",
        **_tham_so_trang(),
        **du_lieu,
    )


@nhanvien_ton_bon_bp.route("/nhanvien/ton-bon/xem/<int:id>")
def xem(id):
    try:
        bon = lay_chi_tiet_bon(id)
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi tải chi tiết bồn cho nhân viên")
        return "Không thể tải chi tiết bồn chứa.", 503

    if bon is None:
        return "Không tìm thấy bồn chứa.", 404

    return render_template(
        "nhanvien/tonbon/xem.html",
        **_tham_so_trang(),
        bon=bon,
    )
