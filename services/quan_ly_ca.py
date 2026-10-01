#File này dùng để tư động đóng ca làm việc khi hết giờ, 
# tránh tình trạng nhân viên quên đóng ca làm việc.

import threading
import time
from datetime import datetime

from services.database import ket_noi


SHIFT_RULES = {
    "Ca Sáng": "12:00:00",
    "Ca Chiều": "18:00:00",
    "Ca Tối": "23:59:00"
}


def tu_dong_dong_ca():
    while True:
        try:
            thoi_gian_hien_tai = datetime.now()
            ngay_hien_tai = thoi_gian_hien_tai.date()
            gio_hien_tai = thoi_gian_hien_tai.time()

            db = ket_noi()
            cursor = db.cursor(dictionary=True)

            cursor.execute("""
                SELECT id, ten_ca
                FROM ca_lam_viec
                WHERE ngay_lam_viec = %s
                  AND trang_thai = 'Đang hoạt động'
            """, (ngay_hien_tai,))

            danh_sach_ca = cursor.fetchall()

            for ca in danh_sach_ca:
                gio_ket_thuc = datetime.strptime(
                    SHIFT_RULES[ca["ten_ca"]],
                    "%H:%M:%S"
                ).time()

                if gio_hien_tai >= gio_ket_thuc:
                    cursor.execute("""
                        UPDATE ca_lam_viec
                        SET trang_thai = 'Đã đóng'
                        WHERE id = %s
                    """, (ca["id"],))

            db.commit()

            cursor.close()
            db.close()

        except Exception as e:
            print(f"Lỗi tự động đóng ca: {e}")

        time.sleep(60)


def khoi_dong_tu_dong_dong_ca():
    luong = threading.Thread(
        target=tu_dong_dong_ca,
        daemon=True
    )

    luong.start()