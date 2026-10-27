import mysql.connector
from flask import Blueprint, current_app, render_template, request

from services.auth_service import yeu_cau_vai_tro
from services.ton_bon import (
    NGUONG_BON_GAN_HET,
    lay_chi_tiet_bon,
    lay_du_lieu_ton_bon,
)


ketoan_ton_bon_bp = Blueprint("ketoan_ton_bon", __name__)


@ketoan_ton_bon_bp.before_request
@yeu_cau_vai_tro("Kế toán")
def bao_ve_router_ton_bon():
    return None


def _tham_so_trang():
    return {
        "layout_template": "quanly/khungquanly.html",
        "trang_hien_tai": "Tồn bồn",
        "endpoint_danh_sach": "ketoan_ton_bon.danh_sach",
        "endpoint_chi_tiet": "ketoan_ton_bon.xem",
        "vai_tro": "Kế toán",
        "nguong_bon_gan_het": NGUONG_BON_GAN_HET,
    }


@ketoan_ton_bon_bp.route("/ketoan/ton-bon")
def danh_sach():
    try:
        du_lieu = lay_du_lieu_ton_bon(
            tu_khoa=request.args.get("q", "").strip(),
            nhien_lieu_id=request.args.get("nhien_lieu_id", "").strip(),
            trang_thai=request.args.get("trang_thai", "").strip(),
        )
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi tải danh sách tồn bồn kế toán")
        return "Không thể tải dữ liệu tồn bồn.", 503

    return render_template(
        "quanly/tonbon/index.html",
        **_tham_so_trang(),
        **du_lieu,
    )


@ketoan_ton_bon_bp.route("/ketoan/ton-bon/xem/<int:id>")
def xem(id):
    try:
        bon = lay_chi_tiet_bon(id)
    except mysql.connector.Error:
        current_app.logger.exception("Lỗi tải chi tiết tồn bồn kế toán")
        return "Không thể tải chi tiết bồn chứa.", 503

    if bon is None:
        return "Không tìm thấy bồn chứa.", 404

    return render_template(
        "quanly/tonbon/xem.html",
        **_tham_so_trang(),
        bon=bon,
    )
