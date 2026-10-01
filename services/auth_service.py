from functools import wraps

from flask import session, redirect, url_for


def yeu_cau_dang_nhap(ham):

    @wraps(ham)
    def kiem_tra_dang_nhap(*args, **kwargs):

        # Kiểm tra xem người dùng đã đăng nhập chưa
        if "tai_khoan_id" not in session:

            # Chưa đăng nhập → chuyển về trang đăng nhập
            return redirect(
                url_for("dang_nhap.dang_nhap")
            )

        # Đã đăng nhập → cho phép chạy chức năng
        return ham(*args, **kwargs)

    return kiem_tra_dang_nhap