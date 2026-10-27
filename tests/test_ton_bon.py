from copy import deepcopy
import unittest
from unittest.mock import patch

from app import app
from services import ton_bon


class FakeInventoryCursor:
    def __init__(self, database):
        self.database = database
        self.result = None
        self.queries = []

    def execute(self, query, params=()):
        self.queries.append((" ".join(query.split()), params))
        if "WHERE bc.id = %s" in query:
            self.result = next(
                (
                    deepcopy(bon)
                    for bon in self.database.bons
                    if bon["id"] == params[0]
                ),
                None,
            )
        else:
            self.result = None

    def fetchall(self):
        return deepcopy(self.database.bons)

    def fetchone(self):
        return deepcopy(self.result)

    def close(self):
        pass


class FakeInventoryDatabase:
    def __init__(self):
        self.bons = [
            {
                "id": 1,
                "ma_bon": "BON01",
                "ten_bon": "Bồn xăng A",
                "nhien_lieu_id": 10,
                "suc_chua": 1000,
                "ton_hien_tai": 200,
                "trang_thai": "Đang hoạt động",
                "ma_nhien_lieu": "NL01",
                "ten_nhien_lieu": "Xăng A",
                "don_vi": "lít",
            },
            {
                "id": 2,
                "ma_bon": "BON02",
                "ten_bon": "Bồn dầu B",
                "nhien_lieu_id": 20,
                "suc_chua": 500,
                "ton_hien_tai": 600,
                "trang_thai": "Ngừng hoạt động",
                "ma_nhien_lieu": "NL02",
                "ten_nhien_lieu": "Dầu B",
                "don_vi": "lít",
            },
            {
                "id": 3,
                "ma_bon": "BON03",
                "ten_bon": "Bồn sức chứa 0",
                "nhien_lieu_id": 10,
                "suc_chua": 0,
                "ton_hien_tai": 0,
                "trang_thai": "Đang hoạt động",
                "ma_nhien_lieu": "NL01",
                "ten_nhien_lieu": "Xăng A",
                "don_vi": "lít",
            },
        ]
        self.cursor_instances = []
        self.closed = False

    def cursor(self, dictionary=False):
        cursor = FakeInventoryCursor(self)
        self.cursor_instances.append(cursor)
        return cursor

    def close(self):
        self.closed = True


class TonBonTests(unittest.TestCase):
    def setUp(self):
        self.database = FakeInventoryDatabase()
        self.patcher = patch.object(
            ton_bon,
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

    def test_quan_ly_va_nhan_vien_xem_cung_du_lieu_va_giao_dien(self):
        noi_dung = []
        for vai_tro, duong_dan in (
            ("Quản lý", "/quanly/ton-bon"),
            ("Nhân viên ca", "/nhanvien/ton-bon"),
        ):
            self.dang_nhap(vai_tro)
            response = self.client.get(duong_dan)
            self.assertEqual(response.status_code, 200)
            noi_dung.append(response.get_data(as_text=True))

        for van_ban in (
            "Tổng sức chứa",
            "Tổng nhiên liệu tồn",
            "Tỷ lệ lấp đầy tổng thể",
            "Bồn xăng A",
            "Bồn dầu B",
            "Dung tích còn trống",
            "Xem chi tiết",
        ):
            self.assertIn(van_ban, noi_dung[0])
            self.assertIn(van_ban, noi_dung[1])

        self.assertIn('action="/quanly/ton-bon"', noi_dung[0])
        self.assertIn('action="/nhanvien/ton-bon"', noi_dung[1])
        self.assertIn("53.3%", noi_dung[0])
        self.assertIn("1,500", noi_dung[0])
        self.assertIn("800", noi_dung[0])
        self.assertIn("2 bồn có dữ liệu bất thường", noi_dung[0])

    def test_tinh_ton_trong_va_ty_le_tung_bon(self):
        du_lieu = ton_bon.lay_du_lieu_ton_bon()
        bon = du_lieu["danh_sach_bon"][0]

        self.assertEqual(bon["dung_tich_con"], 800)
        self.assertEqual(bon["ty_le_lap_day"], 20)
        self.assertTrue(bon["bon_gan_het"])
        self.assertEqual(du_lieu["thong_ke"]["tong_so_bon"], 3)
        self.assertEqual(du_lieu["thong_ke"]["tong_suc_chua"], 1500)
        self.assertEqual(du_lieu["thong_ke"]["tong_ton_hien_tai"], 800)
        self.assertAlmostEqual(
            du_lieu["thong_ke"]["ty_le_lap_day"],
            800 / 1500 * 100,
        )

    def test_loc_tim_kiem_nhien_lieu_va_trang_thai(self):
        du_lieu = ton_bon.lay_du_lieu_ton_bon(
            tu_khoa="dầu",
            nhien_lieu_id="20",
            trang_thai="Ngừng hoạt động",
        )

        self.assertEqual(
            [bon["id"] for bon in du_lieu["danh_sach_bon"]],
            [2],
        )
        self.assertEqual(du_lieu["filters"]["q"], "dầu")

    def test_suc_chua_bang_khong_va_ton_vuot_suc_chua_khong_lam_trang_loi(self):
        self.dang_nhap("Quản lý")

        response = self.client.get("/quanly/ton-bon")
        chi_tiet = self.client.get("/quanly/ton-bon/xem/3")
        bat_thuong = self.client.get("/quanly/ton-bon/xem/2")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(chi_tiet.status_code, 200)
        self.assertIn("Không xác định", chi_tiet.get_data(as_text=True))
        self.assertIn("Dữ liệu tồn bồn bất thường", chi_tiet.get_data(as_text=True))
        self.assertIn("Dữ liệu tồn bồn bất thường", bat_thuong.get_data(as_text=True))

    def test_phan_quyen_bao_ve_cac_route_quan_ly_va_nhan_vien(self):
        self.dang_nhap("Nhân viên ca")
        self.assertEqual(self.client.get("/quanly/ton-bon").status_code, 403)
        self.assertEqual(
            self.client.get("/quanly/ton-bon/xem/1").status_code,
            403,
        )

        self.dang_nhap("Quản lý")
        self.assertEqual(self.client.get("/nhanvien/ton-bon").status_code, 403)
        self.assertEqual(
            self.client.get("/nhanvien/ton-bon/xem/1").status_code,
            403,
        )

    def test_chua_dang_nhap_bi_chuyen_den_dang_nhap(self):
        response = self.client.get("/quanly/ton-bon")

        self.assertEqual(response.status_code, 302)
        self.assertIn("/dang-nhap", response.headers["Location"])

    def test_chi_tiet_bon_ton_tai_va_khong_ton_tai(self):
        self.dang_nhap("Nhân viên ca")

        co_du_lieu = self.client.get("/nhanvien/ton-bon/xem/1")
        khong_co_du_lieu = self.client.get("/nhanvien/ton-bon/xem/999")

        self.assertEqual(co_du_lieu.status_code, 200)
        self.assertIn("BON01", co_du_lieu.get_data(as_text=True))
        self.assertEqual(khong_co_du_lieu.status_code, 404)

    def test_chuc_nang_chi_doc_khong_co_route_thay_doi_va_chi_select(self):
        self.dang_nhap("Nhân viên ca")
        response = self.client.post("/nhanvien/ton-bon")

        self.assertEqual(response.status_code, 405)
        self.client.get("/nhanvien/ton-bon")

        for cursor in self.database.cursor_instances:
            self.assertTrue(
                all(query.startswith("SELECT") for query, _ in cursor.queries)
            )
        self.assertTrue(self.database.closed)

    def test_ke_toan_tiep_tuc_xem_ton_bon_tai_menu_hien_co(self):
        self.dang_nhap("Kế toán")

        response = self.client.get("/ketoan/ton-bon")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Tổng sức chứa", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
