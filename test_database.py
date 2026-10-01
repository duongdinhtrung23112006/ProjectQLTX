from services.database import ket_noi

ket_noi_db = ket_noi()

if ket_noi_db.is_connected():
    print("Kết nối MySQL thành công!")

ket_noi_db.close()