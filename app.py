from flask import Flask, render_template

from routes.quanly.bon_chua import bon_chua_bp
from routes.quanly.ca_lam_viec import ca_lam_viec_bp
from routes.quanly.nhan_vien import nhan_vien_bp
from routes.quanly.trang_chu import trang_chu_bp

from services.auth_service import yeu_cau_dang_nhap

from routes.auth.dang_nhap import dang_nhap_bp

# from services.quan_ly_ca import khoi_dong_tu_dong_dong_ca
# Tạm thời tắt chức năng tự động đóng ca làm việc để tránh lỗi chạy song song 2 thread.


app = Flask(__name__)

# Khóa bí mật dùng cho session và các chức năng bảo mật của Flask
app.secret_key = "tram_xang_secret_key"

app.register_blueprint(dang_nhap_bp)

app.register_blueprint(trang_chu_bp)


app.register_blueprint(bon_chua_bp)

app.register_blueprint(nhan_vien_bp)


@app.route("/nhien-lieu")
@yeu_cau_dang_nhap
def nhien_lieu():
    return render_template(
        "quanly/nhien_lieu.html",
        trang_hien_tai="Nhiên liệu"
    )


@app.route("/nhap-hang")
@yeu_cau_dang_nhap
def nhap_hang():
    return render_template(
        "quanly/nhap_hang.html",
        trang_hien_tai="Nhập hàng"
    )


@app.route("/ban-hang")
@yeu_cau_dang_nhap
def ban_hang():
    return render_template(
        "quanly/ban_hang.html",
        trang_hien_tai="Bán hàng"
    )


app.register_blueprint(ca_lam_viec_bp)


# khoi_dong_tu_dong_dong_ca()
# Tạm thời tắt chức năng tự động đóng ca làm việc.


@app.route("/thong-ke")
@yeu_cau_dang_nhap
def thong_ke():
    return render_template(
        "quanly/thong_ke.html",
        trang_hien_tai="Thống kê"
    )


@app.route("/ton-bon")
@yeu_cau_dang_nhap
def ton_bon():
    return render_template(
        "quanly/ton_bon.html",
        trang_hien_tai="Tồn bồn"
    )


@app.route("/tra-cuu")
@yeu_cau_dang_nhap
def tra_cuu():
    return render_template(
        "quanly/tra_cuu.html",
        trang_hien_tai="Tra cứu"
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)