from functools import wraps
import unicodedata
from flask import session, redirect, url_for, abort


def chuan_hoa_vai_tro(vai_tro):
    if not isinstance(vai_tro, str):
        return ""

    return unicodedata.normalize("NFC", vai_tro).strip()


def yeu_cau_dang_nhap(ham):
    @wraps(ham)
    def kiem_tra_dang_nhap(*args, **kwargs):
        # Chưa đăng nhập
        if "tai_khoan_id" not in session:
            return redirect(
                url_for("dang_nhap.dang_nhap")
            )

        # Đã đăng nhập
        return ham(*args, **kwargs)

    return kiem_tra_dang_nhap


def yeu_cau_vai_tro(*vai_tro_duoc_phep):
    def decorator(ham):
        @wraps(ham)
        def kiem_tra_vai_tro(*args, **kwargs):

            # Chưa đăng nhập
            if "tai_khoan_id" not in session:
                return redirect(
                    url_for("dang_nhap.dang_nhap")
                )

            # Lấy vai trò của tài khoản đang đăng nhập
            vai_tro_hien_tai = chuan_hoa_vai_tro(
                session.get("vai_tro")
            )
            vai_tro_cho_phep = {
                chuan_hoa_vai_tro(vai_tro)
                for vai_tro in vai_tro_duoc_phep
            }

            # Không có quyền
            if vai_tro_hien_tai not in vai_tro_cho_phep:
                abort(403)

            # Có quyền
            return ham(*args, **kwargs)

        return kiem_tra_vai_tro

    return decorator