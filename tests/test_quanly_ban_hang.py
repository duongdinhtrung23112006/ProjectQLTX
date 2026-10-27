from copy import deepcopy
from datetime import date
from decimal import Decimal
import unittest
from unittest.mock import patch

from app import app
from routes.quanly import ban_hang


def tao_phieu(trang_thai, phieu_id=1, so_luong=2):
    return {
        "id": phieu_id,
        "ma_ban": f"BH{phieu_id:06d}",
        "ngay_ban": date.today(),
        "gio_ban": "13:00:00",
        "ca_lam_viec_id": 11,
        "nhan_vien_id": phieu_id + 6,
        "nhien_lieu_id": 3,
        "bon_id": 21,
        "so_luong": so_luong,
        "don_gia": Decimal("23000.00"),
        "thanh_tien": Decimal("46000.00"),
        "ghi_chu": "Kiểm thử",
        "trang_thai": trang_thai,
    }


class FakeSalesCursor:
    def __init__(self, database):
        self.database = database
        self.result = None
        self.results = []
        self.rowcount = 0
        self.last_query = ""
        self.last_params = ()

    def execute(self, query, params=()):
        self.last_query = " ".join(query.split())
        self.last_params = params or ()
        self.database.executed_queries.append(self.last_query)
        self.result = None
        self.results = []
        self.rowcount = 0
        state = self.database.state

        if "COUNT(*) AS tong_so_phieu" in self.last_query:
            self.result = {
                "tong_so_phieu": len(state["ban_hang"]),
                "tong_so_luong_ban": sum(
                    phieu["so_luong"]
                    for phieu in state["ban_hang"]
                    if phieu["trang_thai"] == "Đã duyệt"
                ),
                "so_phieu_cho_duyet": sum(
                    phieu["trang_thai"] == "Chờ duyệt"
                    for phieu in state["ban_hang"]
                ),
            }
        elif self.last_query.startswith("SELECT") and "FROM ban_hang bh" in self.last_query:
            phieu = self._find_sale(self.last_params[0]) if self.last_params else None
            if "WHERE bh.id = %s" in self.last_query:
                self.result = self._detail(phieu) if phieu else None
            else:
                self.results = self._filter_sales()
        elif self.last_query.startswith("SELECT") and "FROM ban_hang" in self.last_query:
            self.result = self._find_sale(self.last_params[0])
        elif "FROM bon_chua" in self.last_query:
            bon = state["bon_chua"]
            if bon["id"] == self.last_params[0]:
                self.result = deepcopy(bon)
        elif "FROM nhien_lieu" in self.last_query:
            nhien_lieu = state["nhien_lieu"]
            if nhien_lieu["id"] == self.last_params[0]:
                self.result = deepcopy(nhien_lieu)
        elif self.last_query.startswith("UPDATE bon_chua"):
            bon = state["bon_chua"]
            so_luong, bon_id = self.last_params[:2]
            if bon["id"] == bon_id:
                if "ton_hien_tai = ton_hien_tai -" in self.last_query:
                    if bon["ton_hien_tai"] >= so_luong:
                        bon["ton_hien_tai"] -= so_luong
                        self.rowcount = 1
                elif bon["ton_hien_tai"] + so_luong <= bon["suc_chua"]:
                    bon["ton_hien_tai"] += so_luong
                    self.rowcount = 1
        elif self.last_query.startswith("UPDATE ban_hang"):
            phieu = self._find_sale(self.last_params[0])
            if phieu and phieu["trang_thai"] == "Chờ duyệt":
                if "SET trang_thai = 'Đã duyệt'" in self.last_query:
                    phieu["trang_thai"] = "Đã duyệt"
                    self.rowcount = 1
                elif "SET trang_thai = 'Đã từ chối'" in self.last_query:
                    phieu["trang_thai"] = "Đã từ chối"
                    self.rowcount = 1
        elif self.last_query.startswith("DELETE FROM ban_hang"):
            phieu = self._find_sale(self.last_params[0])
            if phieu and phieu["trang_thai"] == self.last_params[1]:
                state["ban_hang"].remove(phieu)
                self.rowcount = 1

    def _find_sale(self, phieu_id):
        return next(
            (
                phieu
                for phieu in self.database.state["ban_hang"]
                if phieu["id"] == phieu_id
            ),
            None,
        )

    def _detail(self, phieu):
        if phieu is None:
            return None
        detail = deepcopy(phieu)
        detail.update(
            {
                "ma_ca": "CA01",
                "ten_ca": "Ca sáng",
                "ma_nv": f"NV{phieu['nhan_vien_id']:03d}",
                "ho_ten": "Nhân viên kiểm thử",
                "ma_nhien_lieu": "NL001",
                "ten_nhien_lieu": "Xăng A",
                "don_vi": "lít",
                "ma_bon": "BON01",
                "ten_bon": "Bồn số 1",
                "ton_hien_tai": self.database.state["bon_chua"]["ton_hien_tai"],
            }
        )
        return detail

    def _filter_sales(self):
        query = self.last_query
        params = list(self.last_params)
        keyword = None
        if "bh.ma_ban LIKE %s" in query:
            keyword = params.pop(0).strip("%").lower()
            params = params[5:]
        status = params.pop(0) if "bh.trang_thai = %s" in query else None
        start = params.pop(0) if "bh.ngay_ban >= %s" in query else None
        end = params.pop(0) if "bh.ngay_ban <= %s" in query else None

        sales = self.database.state["ban_hang"]
        if keyword:
            sales = [
                phieu for phieu in sales
                if keyword in phieu["ma_ban"].lower()
            ]
        if status:
            sales = [
                phieu for phieu in sales
                if phieu["trang_thai"] == status
            ]
        if start:
            sales = [
                phieu for phieu in sales
                if phieu["ngay_ban"] >= start
            ]
        if end:
            sales = [
                phieu for phieu in sales
                if phieu["ngay_ban"] <= end
            ]

        return [self._detail(phieu) for phieu in sales]

    def fetchone(self):
        return deepcopy(self.result)

    def fetchall(self):
        return deepcopy(self.results)

    def close(self):
        pass


class FakeSalesDatabase:
    def __init__(self):
        self.state = {
            "bon_chua": {
                "id": 21,
                "nhien_lieu_id": 3,
                "suc_chua": 100,
                "ton_hien_tai": 5,
                "trang_thai": "Đang hoạt động",
            },
            "nhien_lieu": {"id": 3, "trang_thai": "Đang bán"},
            "ban_hang": [
                tao_phieu("Chờ duyệt", 1),
                tao_phieu("Đã duyệt", 2),
                tao_phieu("Đã từ chối", 3),
            ],
        }
        self.snapshot = None
        self.commit_count = 0
        self.rollback_count = 0
        self.executed_queries = []

    def cursor(self, dictionary=False):
        return FakeSalesCursor(self)

    def start_transaction(self):
        self.snapshot = deepcopy(self.state)

    def commit(self):
        self.snapshot = None
        self.commit_count += 1

    def rollback(self):
        if self.snapshot is not None:
            self.state = self.snapshot
            self.snapshot = None
        self.rollback_count += 1

    def close(self):
        pass


class QuanLyBanHangTests(unittest.TestCase):
    def setUp(self):
        self.database = FakeSalesDatabase()
        self.patcher = patch.object(
            ban_hang,
            "ket_noi",
            return_value=self.database,
        )
        self.patcher.start()
        app.config.update(TESTING=True)
        self.client = app.test_client()
        with self.client.session_transaction() as session:
            session["tai_khoan_id"] = 1
            session["vai_tro"] = "Quản lý"

    def tearDown(self):
        self.patcher.stop()

    def test_quan_ly_xem_tat_ca_phieu_va_nut_theo_trang_thai(self):
        response = self.client.get("/ban-hang")
        noi_dung = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("BH000001", noi_dung)
        self.assertIn("BH000002", noi_dung)
        self.assertIn("BH000003", noi_dung)
        self.assertEqual(noi_dung.count("Duyệt</button>"), 1)
        self.assertEqual(noi_dung.count("Từ chối</button>"), 1)
        self.assertEqual(noi_dung.count("Xem</a>"), 3)
        self.assertEqual(noi_dung.count("Xóa</button>"), 3)

    def test_chi_quan_ly_truy_cap_route_quan_ly(self):
        with self.client.session_transaction() as session:
            session["vai_tro"] = "Nhân viên ca"

        response = self.client.post("/quanly/ban-hang/duyet/1")

        self.assertEqual(response.status_code, 403)
        self.assertEqual(self.database.commit_count, 0)

    def test_thao_tac_thay_doi_du_lieu_chi_nhan_post(self):
        response = self.client.get("/quanly/ban-hang/duyet/1")

        self.assertEqual(response.status_code, 405)
        self.assertEqual(self.database.commit_count, 0)

    def test_duyet_tru_ton_va_chuyen_trang_thai_trong_giao_dich(self):
        response = self.client.post("/quanly/ban-hang/duyet/1")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.database.state["bon_chua"]["ton_hien_tai"], 3)
        self.assertEqual(
            self.database.state["ban_hang"][0]["trang_thai"],
            "Đã duyệt",
        )
        self.assertEqual(self.database.commit_count, 1)

    def test_duyet_khi_ton_khong_du_roll_back(self):
        self.database.state["bon_chua"]["ton_hien_tai"] = 1

        self.client.post("/quanly/ban-hang/duyet/1")

        self.assertEqual(self.database.state["bon_chua"]["ton_hien_tai"], 1)
        self.assertEqual(
            self.database.state["ban_hang"][0]["trang_thai"],
            "Chờ duyệt",
        )
        self.assertEqual(self.database.commit_count, 0)
        self.assertGreater(self.database.rollback_count, 0)

    def test_hai_phieu_tranh_ton_khong_ban_vuot_ton(self):
        self.database.state["ban_hang"].append(
            tao_phieu("Chờ duyệt", 4, so_luong=4)
        )

        self.client.post("/quanly/ban-hang/duyet/1")
        self.client.post("/quanly/ban-hang/duyet/4")

        self.assertEqual(self.database.state["bon_chua"]["ton_hien_tai"], 3)
        self.assertEqual(
            self.database.state["ban_hang"][0]["trang_thai"],
            "Đã duyệt",
        )
        self.assertEqual(
            self.database.state["ban_hang"][3]["trang_thai"],
            "Chờ duyệt",
        )
        self.assertTrue(
            any(
                "FROM ban_hang" in query and "FOR UPDATE" in query
                for query in self.database.executed_queries
            )
        )
        self.assertTrue(
            any(
                "FROM bon_chua" in query and "FOR UPDATE" in query
                for query in self.database.executed_queries
            )
        )
        self.assertTrue(
            any(
                "ton_hien_tai >= %s" in query
                for query in self.database.executed_queries
            )
        )

    def test_khong_the_duyet_lai_phieu_da_duyet(self):
        self.client.post("/quanly/ban-hang/duyet/2")

        self.assertEqual(self.database.state["bon_chua"]["ton_hien_tai"], 5)
        self.assertEqual(self.database.commit_count, 0)

    def test_khong_duyet_phieu_co_thanh_tien_khong_khop(self):
        self.database.state["ban_hang"][0]["thanh_tien"] = Decimal("1.00")

        self.client.post("/quanly/ban-hang/duyet/1")

        self.assertEqual(self.database.state["bon_chua"]["ton_hien_tai"], 5)
        self.assertEqual(
            self.database.state["ban_hang"][0]["trang_thai"],
            "Chờ duyệt",
        )
        self.assertEqual(self.database.commit_count, 0)

    def test_tu_choi_khong_thay_doi_ton_va_khong_tu_choi_lai(self):
        self.client.post("/quanly/ban-hang/tu-choi/1")

        self.assertEqual(
            self.database.state["ban_hang"][0]["trang_thai"],
            "Đã từ chối",
        )
        self.assertEqual(self.database.state["bon_chua"]["ton_hien_tai"], 5)
        self.assertEqual(self.database.commit_count, 1)

        self.client.post("/quanly/ban-hang/tu-choi/3")
        self.assertEqual(self.database.commit_count, 1)

    def test_xoa_phieu_da_duyet_hoan_tra_ton_cung_giao_dich(self):
        self.database.state["bon_chua"]["ton_hien_tai"] = 3

        self.client.post("/quanly/ban-hang/xoa/2")

        self.assertEqual(self.database.state["bon_chua"]["ton_hien_tai"], 5)
        self.assertNotIn(
            2,
            [phieu["id"] for phieu in self.database.state["ban_hang"]],
        )
        self.assertEqual(self.database.commit_count, 1)

    def test_xoa_phieu_chua_duyet_va_tu_choi_khong_doi_ton(self):
        self.client.post("/quanly/ban-hang/xoa/1")
        self.client.post("/quanly/ban-hang/xoa/3")

        self.assertEqual(self.database.state["bon_chua"]["ton_hien_tai"], 5)
        self.assertEqual(self.database.state["ban_hang"], [tao_phieu("Đã duyệt", 2)])
        self.assertEqual(self.database.commit_count, 2)

    def test_khong_xoa_phieu_duyet_neu_hoan_ton_vuot_suc_chua(self):
        self.database.state["bon_chua"]["ton_hien_tai"] = 100

        self.client.post("/quanly/ban-hang/xoa/2")

        self.assertEqual(self.database.state["bon_chua"]["ton_hien_tai"], 100)
        self.assertEqual(len(self.database.state["ban_hang"]), 3)
        self.assertEqual(self.database.commit_count, 0)

    def test_xem_chi_tiet_hien_thi_thong_tin_ban(self):
        response = self.client.get("/quanly/ban-hang/xem/1")
        noi_dung = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        for thong_tin in (
            "BH000001",
            "Ca sáng",
            "Nhân viên kiểm thử",
            "Xăng A",
            "Bồn số 1",
            "Ghi chú",
            "Chờ duyệt",
        ):
            self.assertIn(thong_tin, noi_dung)

    def test_loc_danh_sach_theo_trang_thai_da_tu_choi(self):
        response = self.client.get(
            "/quanly/ban-hang?trang_thai=%C4%90%C3%A3+t%E1%BB%AB+ch%E1%BB%91i"
        )
        noi_dung = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("BH000003", noi_dung)
        self.assertNotIn("BH000001", noi_dung)
        self.assertNotIn("BH000002", noi_dung)


if __name__ == "__main__":
    unittest.main()
