from flask import Flask, redirect, render_template, session, url_for

# Import các blueprint từ các module khác nhau của quản lý
from routes.quanly.bon_chua import bon_chua_bp
from routes.quanly.ca_lam_viec import ca_lam_viec_bp
from routes.quanly.nhan_vien import nhan_vien_bp
from routes.quanly.trang_chu import quanly_trang_chu_bp
from routes.quanly.nhien_lieu import nhien_lieu_bp
from routes.quanly.nhap_hang import nhap_hang_bp
from routes.quanly.ban_hang import quanly_ban_hang_bp
from routes.quanly.ton_bon import quanly_ton_bon_bp
from routes.quanly.tra_cuu import quanly_tra_cuu_bp
from routes.quanly.thong_ke import quanly_thong_ke_bp

# Import các blueprint từ các module khác nhau của nhân viên
from routes.nhanvien.trang_chu import nhanvien_trang_chu_bp
from routes.nhanvien.bon_chua import nhanvien_bon_chua_bp
from routes.nhanvien.nhien_lieu import nhanvien_nhien_lieu_bp
from routes.nhanvien.nhap_hang import nhanvien_nhap_hang_bp
from routes.nhanvien.ban_hang import nhanvien_ban_hang_bp
from routes.nhanvien.ton_bon import nhanvien_ton_bon_bp

# Import các blueprint từ các module khác nhau của kế toán
from routes.ketoan.trang_chu import ketoan_trang_chu_bp
from routes.ketoan.ton_bon import ketoan_ton_bon_bp
from routes.ketoan.tra_cuu import ketoan_tra_cuu_bp
from routes.ketoan.thong_ke import ketoan_thong_ke_bp

# Import các dịch vụ cần thiết
from services.auth_service import (
    chuan_hoa_vai_tro,
    yeu_cau_dang_nhap,
    yeu_cau_vai_tro,
)

# Import các blueprint từ các module khác nhau của xác thực
from routes.auth.dang_nhap import dang_nhap_bp

# from services.quan_ly_ca import khoi_dong_tu_dong_dong_ca
# Tạm thời tắt chức năng tự động đóng ca làm việc để tránh lỗi chạy song song 2 thread.


app = Flask(__name__)

# Khóa bí mật dùng cho session và các chức năng bảo mật của Flask
app.secret_key = "tram_xang_secret_key"

# Đăng kí blueprint cho quản lý
app.register_blueprint(dang_nhap_bp)
app.register_blueprint(quanly_trang_chu_bp)
app.register_blueprint(bon_chua_bp)
app.register_blueprint(nhan_vien_bp)
app.register_blueprint(nhien_lieu_bp)
app.register_blueprint(nhap_hang_bp)
app.register_blueprint(quanly_ban_hang_bp)
app.register_blueprint(quanly_ton_bon_bp)
app.register_blueprint(quanly_tra_cuu_bp)
app.register_blueprint(quanly_thong_ke_bp)

# Đăng ký blueprint cho trang chủ của nhân viên
app.register_blueprint(nhanvien_trang_chu_bp)
app.register_blueprint(nhanvien_bon_chua_bp)
app.register_blueprint(nhanvien_nhien_lieu_bp)
app.register_blueprint(nhanvien_nhap_hang_bp)
app.register_blueprint(nhanvien_ban_hang_bp)
app.register_blueprint(nhanvien_ton_bon_bp)

# Đăng ký blueprint cho trang chủ của kế toán
app.register_blueprint(ketoan_trang_chu_bp)
app.register_blueprint(ketoan_ton_bon_bp)
app.register_blueprint(ketoan_tra_cuu_bp)
app.register_blueprint(ketoan_thong_ke_bp)



app.register_blueprint(ca_lam_viec_bp)


# khoi_dong_tu_dong_dong_ca()
# Tạm thời tắt chức năng tự động đóng ca làm việc.


@app.route("/thong-ke")
@yeu_cau_vai_tro("Quản lý", "Kế toán")
def thong_ke():
    if chuan_hoa_vai_tro(session.get("vai_tro")) == "Kế toán":
        return redirect(url_for("ketoan_thong_ke.danh_sach"))
    return redirect(url_for("quanly_thong_ke.danh_sach"))


@app.route("/ai")
@yeu_cau_dang_nhap
def ai():
    return render_template(
        "quanly/ai.html",
        trang_hien_tai="Trợ lý AI"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)