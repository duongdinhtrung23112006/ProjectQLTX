from datetime import date
from decimal import Decimal
import unittest
from unittest.mock import patch

from app import app
from services import thong_ke


class FakeStatisticsCursor:
    def __init__(self):
        self.queries = []
        self.query = ""
        self.params = ()

    def execute(self, query, params=()):
        self.query = " ".join(query.split())
        self.params = params
        self.queries.append((self.query, params))

    def fetchone(self):
        if "COUNT(*) AS so_giao_dich" in self.query:
            if "FROM ban_hang bh" in self.query:
                return {
                    "so_giao_dich": 2,
                    "tong_so_luong": 120,
                    "tong_tien": Decimal("2760000.00"),
                }
            return {"so_giao_dich": 3, "tong_so_luong": 400}
        if "AS so_cho_duyet" in self.query:
            return {"so_cho_duyet": 1 if "FROM ban_hang" in self.query else 2}
        return {}

    def fetchall(self):
        if "GROUP BY nl.don_vi" in self.query:
            if "FROM ban_hang bh" in self.query:
                return [{"don_vi": "Lít", "so_luong": Decimal("120")}]
            return [{"don_vi": "Lít", "so_luong": Decimal("400")}]
        if "DATE_FORMAT(bh.ngay_ban" in self.query and "GROUP BY ky, nl.don_vi" in self.query:
            return [{
                "ky": date.today().strftime("%Y-%m-%d"),
                "don_vi": "Lít",
                "so_luong": Decimal("120"),
            }]
        if "DATE_FORMAT(bh.ngay_ban" in self.query:
            return [
                {"ky": date.today().strftime("%Y-%m-%d"), "doanh_thu": Decimal("2760000.00")}
            ]
        if "DATE_FORMAT(nh.ngay_tao" in self.query:
            return [
                {
                    "ky": date.today().strftime("%Y-%m-%d"),
                    "don_vi": "Lít",
                    "so_luong": Decimal("400"),
                }
            ]
        if "GROUP BY nl.id, nl.ten_nhien_lieu" in self.query:
            return [{
                "ten_nhien_lieu": "Xăng",
                "don_vi": "Lít",
                "so_luong": Decimal("120"),
            }]
        if "AS ma_giao_dich" in self.query:
            return []
        return []

    def close(self):
        pass


class FakeStatisticsDatabase:
    def __init__(self):
        self.cursor_instance = FakeStatisticsCursor()
        self.closed = False

    def cursor(self, dictionary=False):
        return self.cursor_instance

    def close(self):
        self.closed = True


def du_lieu_mau():
    return {
        "khoang": {
            "khoang": "7_ngay",
            "tu_ngay": "2026-10-22",
            "den_ngay": "2026-10-28",
            "nhan_khoang": "7 ngày gần nhất",
            "loi_loc": None,
            "ngay_hien_tai": date(2026, 10, 28),
        },
        "kpi": {
            "doanh_thu": Decimal("2760000.00"),
            "luong_ban": [{"don_vi": "Lít", "so_luong": 120}],
            "luong_nhap": [{"don_vi": "Lít", "so_luong": 400}],
            "so_giao_dich_ban": 2,
            "so_giao_dich_nhap": 3,
            "cho_duyet_ban": 1,
            "cho_duyet_nhap": 2,
            "tong_cho_duyet": 3,
        },
        "bieu_do": {
            "doanh_thu": [],
            "co_cau_nhien_lieu": [],
            "so_sanh_san_luong": [],
            "dinh_dang": "%Y-%m-%d",
        },
        "bon_chua": [],
        "thong_ke_bon": {
            "tong_so": 0,
            "dang_hoat_dong": 0,
            "ngung_hoat_dong": 0,
            "ty_le_su_dung": None,
            "don_vi": "",
        },
        "giao_dich_gan_day": [],
        "canh_bao": [],
        "nguong_bon_gan_het": 20,
    }


class ThongKeTests(unittest.TestCase):
    def setUp(self):
        self.database = FakeStatisticsDatabase()
        self.patcher_db = patch.object(
            thong_ke,
            "ket_noi",
            return_value=self.database,
        )
        self.patcher_tanks = patch.object(
            thong_ke,
            "lay_du_lieu_ton_bon",
            return_value={"danh_sach_bon": []},
        )
        self.patcher_db.start()
        self.patcher_tanks.start()
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def tearDown(self):
        self.patcher_db.stop()
        self.patcher_tanks.stop()

    def dang_nhap(self, vai_tro):
        with self.client.session_transaction() as session:
            session["tai_khoan_id"] = 1
            session["vai_tro"] = vai_tro

    def test_khoang_thoi_gian_duoc_tinh_chinh_xac(self):
        hom_nay = date(2026, 10, 28)
        khoang_7_ngay = thong_ke._lay_khoang_thoi_gian(
            {"khoang": "7_ngay"},
            hom_nay,
        )
        khoang_thang = thong_ke._lay_khoang_thoi_gian(
            {"khoang": "thang_nay"},
            hom_nay,
        )
        khoang_tuy_chinh = thong_ke._lay_khoang_thoi_gian(
            {
                "khoang": "tuy_chinh",
                "tu_ngay": "2026-10-01",
                "den_ngay": "2026-10-20",
            },
            hom_nay,
        )
        khoang_sai = thong_ke._lay_khoang_thoi_gian(
            {
                "khoang": "tuy_chinh",
                "tu_ngay": "2026-10-21",
                "den_ngay": "2026-10-20",
            },
            hom_nay,
        )

        self.assertEqual(khoang_7_ngay["tu_ngay"], "2026-10-22")
        self.assertEqual(khoang_thang["tu_ngay"], "2026-10-01")
        self.assertEqual(khoang_tuy_chinh["den_ngay"], "2026-10-20")
        self.assertIsNotNone(khoang_sai["loi_loc"])

    def test_thong_ke_tinh_rieng_theo_loai_va_chi_dem_da_duyet(self):
        ket_qua = thong_ke.lay_du_lieu_thong_ke({"khoang": "hom_nay"})

        self.assertEqual(ket_qua["kpi"]["doanh_thu"], Decimal("2760000.00"))
        self.assertEqual(ket_qua["kpi"]["so_giao_dich_ban"], 2)
        self.assertEqual(ket_qua["kpi"]["so_giao_dich_nhap"], 3)
        self.assertEqual(ket_qua["kpi"]["tong_cho_duyet"], 3)
        thong_ke_queries = [
            (query, params)
            for query, params in self.database.cursor_instance.queries
            if "COUNT(*) AS so_giao_dich" in query
        ]
        self.assertEqual(len(thong_ke_queries), 2)
        self.assertTrue(all(params[0] == "Đã duyệt" for _, params in thong_ke_queries))
        self.assertTrue(
            all(
                query.startswith("SELECT")
                for query, _ in self.database.cursor_instance.queries
            )
        )
        self.assertTrue(self.database.closed)

    def test_quan_ly_va_ke_toan_duoc_truy_cap_dashboard(self):
        with patch(
            "routes.quanly.thong_ke.lay_du_lieu_thong_ke",
            return_value=du_lieu_mau(),
        ), patch(
            "routes.ketoan.thong_ke.lay_du_lieu_thong_ke",
            return_value=du_lieu_mau(),
        ):
            for vai_tro, duong_dan, stylesheet in (
                (
                    "Quản lý",
                    "/quanly/thong-ke",
                    "cssquanly/thongke/index.css",
                ),
                (
                    "Kế toán",
                    "/ketoan/thong-ke",
                    "cssketoan/thongke/index.css",
                ),
            ):
                self.dang_nhap(vai_tro)
                response = self.client.get(duong_dan)
                noi_dung = response.get_data(as_text=True)
                self.assertEqual(response.status_code, 200)
                self.assertIn("Tổng quan hệ thống", noi_dung)
                self.assertIn(stylesheet, noi_dung)
                self.assertIn("2,760,000", noi_dung)

    def test_khong_co_quyen_truy_cap_dashboard_hoac_chi_tiet(self):
        self.dang_nhap("Nhân viên ca")
        for duong_dan in (
            "/quanly/thong-ke",
            "/ketoan/thong-ke",
            "/quanly/thong-ke/xem/ban_hang/1",
            "/ketoan/thong-ke/xem/nhap_hang/1",
        ):
            self.assertEqual(self.client.get(duong_dan).status_code, 403)

        with self.client.session_transaction() as session:
            session.clear()
        self.assertEqual(self.client.get("/quanly/thong-ke").status_code, 302)
        self.assertEqual(self.client.get("/ketoan/thong-ke").status_code, 302)

    def test_duong_dan_tuong_thich_thong_ke_chuyen_huong_dung_vai_tro(self):
        self.dang_nhap("Kế toán")
        response = self.client.get("/thong-ke")
        self.assertEqual(response.status_code, 302)
        self.assertIn("/ketoan/thong-ke", response.headers["Location"])

    def test_chi_tiet_giao_dich_la_chi_doc(self):
        self.dang_nhap("Quản lý")
        with patch(
            "routes.quanly.thong_ke.lay_chi_tiet_giao_dich",
            return_value={
                "loai": "nhap_hang",
                "ma_giao_dich": "NH001",
                "ngay": date(2026, 10, 28),
                "gio": None,
                "so_luong": 100,
                "don_gia": None,
                "thanh_tien": None,
                "ghi_chu": None,
                "trang_thai": "Đã duyệt",
                "ma_ca": None,
                "ten_ca": None,
                "ma_nv": "NV01",
                "ho_ten": "Nguyễn An",
                "ma_nhien_lieu": "NL01",
                "ten_nhien_lieu": "Xăng",
                "don_vi": "Lít",
                "ma_bon": "BON01",
                "ten_bon": "Bồn 1",
            },
        ):
            response = self.client.get(
                "/quanly/thong-ke/xem/nhap_hang/1?khoang=hom_nay"
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn("NH001", response.get_data(as_text=True))
        self.assertIn("Không có trong dữ liệu nghiệp vụ", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
