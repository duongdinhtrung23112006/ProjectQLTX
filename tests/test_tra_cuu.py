from datetime import date
import unittest
from unittest.mock import patch

from app import app
from services import tra_cuu


class FakeLookupCursor:
    def __init__(self):
        self.queries = []
        self.current_query = ""
        self.current_params = ()

    def execute(self, query, params=()):
        self.current_query = " ".join(query.split())
        self.current_params = params
        self.queries.append((self.current_query, params))

    def fetchall(self):
        query = self.current_query
        if query.startswith("SELECT id, ma_ca"):
            return [{
                "id": 4,
                "ma_ca": "CA04",
                "ten_ca": "Ca sáng",
                "ngay_lam_viec": date(2026, 10, 28),
            }]
        if query.startswith("SELECT id, ma_nv"):
            return [{"id": 5, "ma_nv": "NV05", "ho_ten": "Nguyễn An"}]
        if query.startswith("SELECT id, ma_nhien_lieu"):
            return [{
                "id": 6,
                "ma_nhien_lieu": "NL06",
                "ten_nhien_lieu": "Xăng",
                "don_vi": "Lít",
            }]
        if query.startswith("SELECT id, ma_bon"):
            return [{"id": 7, "ma_bon": "BON07", "ten_bon": "Bồn 7"}]
        if "GROUP BY nl.don_vi" in query:
            return [{"don_vi": "Lít", "so_luong": 500}]
        if "AS ma_giao_dich" in query and "FROM ban_hang bh" in query:
            return [{
                "id": 1,
                "ma_giao_dich": "BH001",
                "ngay": date(2026, 10, 28),
                "gio": "09:15",
                "so_luong": 50,
                "don_gia": 23000,
                "thanh_tien": 1150000,
                "trang_thai": "Đã duyệt",
                "ma_ca": "CA04",
                "ten_ca": "Ca sáng",
                "ma_nv": "NV05",
                "ho_ten": "Nguyễn An",
                "ten_nhien_lieu": "Xăng",
                "don_vi": "Lít",
                "ma_bon": "BON07",
                "ten_bon": "Bồn 7",
            }]
        if "AS ma_giao_dich" in query and "FROM nhap_hang nh" in query:
            return [{
                "id": 2,
                "ma_giao_dich": "NH002",
                "ngay": date(2026, 10, 27),
                "gio": None,
                "so_luong": 300,
                "don_gia": None,
                "thanh_tien": None,
                "trang_thai": "Đã duyệt",
                "ma_ca": None,
                "ten_ca": None,
                "ma_nv": "NV05",
                "ho_ten": "Nguyễn An",
                "ten_nhien_lieu": "Xăng",
                "don_vi": "Lít",
                "ma_bon": "BON07",
                "ten_bon": "Bồn 7",
            }]
        return []

    def fetchone(self):
        query = self.current_query
        if "COUNT(*) AS tong_so" in query:
            return {"tong_so": 1}
        if "AS tong_tien" in query:
            return {"tong_tien": 1150000}
        if "WHERE bh.id = %s" in query:
            return {
                "id": 1,
                "ma_giao_dich": "BH001",
                "ngay": date(2026, 10, 28),
                "gio": "09:15",
                "so_luong": 50,
                "don_gia": 23000,
                "thanh_tien": 1150000,
                "ghi_chu": "Ghi chú",
                "trang_thai": "Đã duyệt",
                "ma_ca": "CA04",
                "ten_ca": "Ca sáng",
                "ma_nv": "NV05",
                "ho_ten": "Nguyễn An",
                "ma_nhien_lieu": "NL06",
                "ten_nhien_lieu": "Xăng",
                "don_vi": "Lít",
                "ma_bon": "BON07",
                "ten_bon": "Bồn 7",
            }
        if "WHERE nh.id = %s" in query:
            return {
                "id": 2,
                "ma_giao_dich": "NH002",
                "ngay": date(2026, 10, 27),
                "gio": None,
                "so_luong": 300,
                "don_gia": None,
                "thanh_tien": None,
                "ghi_chu": None,
                "trang_thai": "Đã duyệt",
                "ma_ca": None,
                "ten_ca": None,
                "ma_nv": "NV05",
                "ho_ten": "Nguyễn An",
                "ma_nhien_lieu": "NL06",
                "ten_nhien_lieu": "Xăng",
                "don_vi": "Lít",
                "ma_bon": "BON07",
                "ten_bon": "Bồn 7",
            }
        return {}

    def close(self):
        pass


class FakeLookupDatabase:
    def __init__(self):
        self.cursor_instance = FakeLookupCursor()
        self.closed = False

    def cursor(self, dictionary=False):
        return self.cursor_instance

    def close(self):
        self.closed = True


class TraCuuTests(unittest.TestCase):
    def setUp(self):
        self.database = FakeLookupDatabase()
        self.patcher = patch.object(
            tra_cuu,
            "ket_noi",
            return_value=self.database,
        )
        self.patcher.start()
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def tearDown(self):
        self.patcher.stop()

    def dang_nhap(self, vai_tro):
        with self.client.session_transaction() as session:
            session["tai_khoan_id"] = 1
            session["vai_tro"] = vai_tro

    def test_quan_ly_va_ke_toan_xem_duoc_trang_tra_cuu(self):
        for vai_tro, duong_dan, css in (
            ("Quản lý", "/quanly/tra-cuu", "cssquanly/tra_cuu/index.css"),
            ("Kế toán", "/ketoan/tra-cuu", "cssketoan/tra_cuu/index.css"),
        ):
            self.dang_nhap(vai_tro)
            response = self.client.get(duong_dan)
            noi_dung = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn("Tra cứu số liệu", noi_dung)
            self.assertIn(css, noi_dung)
            self.assertIn("BH001", noi_dung)
            self.assertIn("NH002", noi_dung)

    def test_nhan_vien_va_nguoi_chua_dang_nhap_khong_duoc_truy_cap(self):
        self.dang_nhap("Nhân viên ca")
        for duong_dan in (
            "/quanly/tra-cuu",
            "/ketoan/tra-cuu",
            "/quanly/tra-cuu/xem/ban_hang/1",
            "/ketoan/tra-cuu/xem/nhap_hang/1",
        ):
            self.assertEqual(self.client.get(duong_dan).status_code, 403)

        with self.client.session_transaction() as session:
            session.clear()
        self.assertEqual(self.client.get("/quanly/tra-cuu").status_code, 302)
        self.assertEqual(self.client.get("/ketoan/tra-cuu").status_code, 302)

    def test_bo_loc_ket_hop_duoc_truyen_bang_tham_so_va_co_phan_trang(self):
        self.dang_nhap("Quản lý")
        response = self.client.get(
            "/quanly/tra-cuu?q=BH001&tu_ngay=2026-10-01&den_ngay=2026-10-28"
            "&ca_id=4&nhan_vien_id=5&nhien_lieu_id=6&bon_id=7"
            "&trang_thai=Đã+duyệt"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("/quanly/tra-cuu/xem/ban_hang/1", response.get_data(as_text=True))
        sale_query = next(
            query
            for query, _ in self.database.cursor_instance.queries
            if "FROM ban_hang bh" in query and "AS ma_giao_dich" in query
        )
        self.assertIn("bh.ngay_ban >= %s", sale_query)
        self.assertIn("bh.ca_lam_viec_id = %s", sale_query)
        self.assertIn("bh.nhan_vien_id = %s", sale_query)
        self.assertIn("bh.nhien_lieu_id = %s", sale_query)
        self.assertIn("bh.bon_id = %s", sale_query)
        import_query = next(
            query
            for query, _ in self.database.cursor_instance.queries
            if "FROM nhap_hang nh" in query and "AS ma_giao_dich" in query
        )
        self.assertIn("nh.ngay_tao >= %s", import_query)
        self.assertNotIn("ca_lam_viec_id", import_query)

    def test_so_lieu_thuc_te_loc_da_duyet_va_tach_nhom_theo_don_vi(self):
        self.dang_nhap("Kế toán")
        self.assertEqual(self.client.get("/ketoan/tra-cuu").status_code, 200)
        queries = [
            query
            for query, _ in self.database.cursor_instance.queries
            if "GROUP BY nl.don_vi" in query
        ]
        self.assertEqual(len(queries), 2)
        self.assertTrue(all("trang_thai = %s" in query for query in queries))
        self.assertTrue(all("GROUP BY nl.don_vi" in query for query in queries))

    def test_giao_dich_cho_duyet_duoc_loc_nhung_khong_tinh_vao_so_lieu_thuc_te(self):
        self.dang_nhap("Quản lý")
        response = self.client.get(
            "/quanly/tra-cuu?loai=ban_hang&trang_thai=Ch%E1%BB%9D%20duy%E1%BB%87t"
        )
        self.assertEqual(response.status_code, 200)
        query_stats = next(
            (query, params)
            for query, params in self.database.cursor_instance.queries
            if "GROUP BY nl.don_vi" in query
        )
        query_list = next(
            (query, params)
            for query, params in self.database.cursor_instance.queries
            if "AS ma_giao_dich" in query and "FROM ban_hang bh" in query
        )
        self.assertEqual(query_stats[1], ("Chờ duyệt", "Đã duyệt"))
        self.assertEqual(query_list[1], ("Chờ duyệt", 20, 0))

    def test_khoang_ngay_dao_nguoc_hien_thi_thong_bao(self):
        self.dang_nhap("Kế toán")
        response = self.client.get(
            "/ketoan/tra-cuu?tu_ngay=2026-10-28&den_ngay=2026-10-01"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Ngày bắt đầu không được sau ngày kết thúc",
            response.get_data(as_text=True),
        )

    def test_ngay_khong_hop_le_hien_thi_loi_va_khong_truy_van_giao_dich(self):
        self.dang_nhap("Quản lý")
        response = self.client.get("/quanly/tra-cuu?tu_ngay=khong-phai-ngay")
        noi_dung = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Ngày tra cứu không hợp lệ", noi_dung)
        self.assertFalse(
            any(
                "FROM ban_hang" in query or "FROM nhap_hang" in query
                for query, _ in self.database.cursor_instance.queries
            )
        )

    def test_chi_tiet_ban_hang_va_nhap_hang_chi_doc(self):
        self.dang_nhap("Quản lý")
        sale = self.client.get("/quanly/tra-cuu/xem/ban_hang/1")
        imported = self.client.get("/quanly/tra-cuu/xem/nhap_hang/2")
        self.assertEqual(sale.status_code, 200)
        self.assertIn("1,150,000.00", sale.get_data(as_text=True))
        self.assertEqual(imported.status_code, 200)
        self.assertIn("Không được lưu trong dữ liệu nhập hàng", imported.get_data(as_text=True))
        self.assertTrue(self.database.closed)
        self.assertTrue(
            all(
                query.startswith("SELECT")
                for query, _ in self.database.cursor_instance.queries
            )
        )


if __name__ == "__main__":
    unittest.main()
