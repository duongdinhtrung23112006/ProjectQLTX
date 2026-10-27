from copy import deepcopy
from datetime import date
from decimal import Decimal
from pathlib import Path
import unittest
from unittest.mock import patch

import mysql.connector

from app import app
from routes.nhanvien import ban_hang


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
        self.result = None
        self.results = []
        self.rowcount = 0
        state = self.database.state

        if "FROM tai_khoan tk" in self.last_query:
            if self.last_params == (1,):
                self.result = {
                    "nhan_vien_id": 7,
                    "ma_nv": "NV007",
                    "ho_ten": "Nhân viên kiểm thử",
                }
        elif "FROM ca_lam_viec" in self.last_query:
            self.results = deepcopy(state["ca_lam_viec"])
        elif (
            "FROM nhien_lieu" in self.last_query
            and "WHERE trang_thai = 'Đang bán'" in self.last_query
        ):
            self.results = deepcopy(state["nhien_lieu"])
        elif "FROM bon_chua bc" in self.last_query:
            self.results = deepcopy(state["bon_chua"])
        elif "COUNT(*) AS tong_so_phieu" in self.last_query:
            employee_id = self.last_params[0]
            phieu_cua_nhan_vien = [
                phieu
                for phieu in state["ban_hang"]
                if phieu["nhan_vien_id"] == employee_id
            ]
            self.result = {
                "tong_so_phieu": len(phieu_cua_nhan_vien),
                "tong_so_luong_ban": sum(
                    phieu["so_luong"]
                    for phieu in phieu_cua_nhan_vien
                    if phieu["trang_thai"] == "Đã duyệt"
                ),
                "so_phieu_cho_duyet": sum(
                    phieu["trang_thai"] == "Chờ duyệt"
                    for phieu in phieu_cua_nhan_vien
                ),
            }
        elif "SELECT trang_thai FROM ban_hang" in self.last_query:
            self.result = self._find_sale(
                self.last_params[0],
                self.last_params[1],
            )
            if self.result and state.get("duyet_khi_khoa"):
                self.result["trang_thai"] = "Đã duyệt"
                state["duyet_khi_khoa"] = False
            if self.result:
                self.result = {"trang_thai": self.result["trang_thai"]}
        elif "SELECT * FROM ban_hang" in self.last_query:
            self.result = self._find_sale(
                self.last_params[0],
                self.last_params[1],
            )
        elif "FROM ban_hang bh" in self.last_query:
            if "WHERE bh.id = %s" in self.last_query:
                phieu = self._find_sale(
                    self.last_params[0],
                    self.last_params[1],
                )
                self.result = self._detail(phieu) if phieu else None
            else:
                self.results = self._filter_sales()
        elif self.last_query.startswith("INSERT INTO ban_hang"):
            if state.get("ma_ban_trung_lap", 0):
                state["ma_ban_trung_lap"] -= 1
                raise mysql.connector.IntegrityError(
                    msg="Duplicate entry",
                    errno=1062,
                )
            ma_ban = self.last_params[0]
            self.database.last_insert = {
                "ma_ban": ma_ban,
                "ngay_ban": date.today(),
                "gio_ban": "13:00:00",
                "ca_lam_viec_id": self.last_params[1],
                "nhan_vien_id": self.last_params[2],
                "nhien_lieu_id": self.last_params[3],
                "bon_id": self.last_params[4],
                "so_luong": self.last_params[5],
                "don_gia": self.last_params[6],
                "thanh_tien": self.last_params[7],
                "ghi_chu": self.last_params[8],
                "trang_thai": "Chờ duyệt",
                "id": 80 + len(state["ban_hang"]),
            }
            state["ban_hang"].append(self.database.last_insert)
            self.rowcount = 1
        elif self.last_query.startswith("UPDATE ban_hang"):
            phieu = self._find_sale(self.last_params[7], self.last_params[8])
            if phieu and phieu["trang_thai"] == "Chờ duyệt":
                (
                    phieu["ca_lam_viec_id"],
                    phieu["nhien_lieu_id"],
                    phieu["bon_id"],
                    phieu["so_luong"],
                    phieu["don_gia"],
                    phieu["thanh_tien"],
                    phieu["ghi_chu"],
                ) = self.last_params[:7]
                self.rowcount = 1
        elif self.last_query.startswith("DELETE FROM ban_hang"):
            phieu = self._find_sale(self.last_params[0], self.last_params[1])
            if phieu and phieu["trang_thai"] == "Chờ duyệt":
                state["ban_hang"].remove(phieu)
                self.rowcount = 1

    def _find_sale(self, sale_id, employee_id):
        return next(
            (
                phieu
                for phieu in self.database.state["ban_hang"]
                if phieu["id"] == sale_id
                and phieu["nhan_vien_id"] == employee_id
            ),
            None,
        )

    def _detail(self, phieu):
        if phieu is None:
            return None
        detail = deepcopy(phieu)
        detail.update(
            {
                "ma_ca": "SANG",
                "ten_ca": "Ca Sáng",
                "ma_nv": "NV007",
                "ho_ten": "Nhân viên kiểm thử",
                "ma_nhien_lieu": "NL001",
                "ten_nhien_lieu": "Xăng A",
                "don_vi": "lít",
                "ma_bon": "BON01",
                "ten_bon": "Bồn số 1",
                "ton_hien_tai": 5,
            }
        )
        return detail

    def _filter_sales(self):
        params = list(self.last_params)
        employee_id = params.pop(0)
        query = self.last_query
        keyword = params.pop(0) if "LIKE %s" in query else None
        if keyword is not None:
            params = params[3:]
        status = None
        if "bh.trang_thai = %s" in query:
            status = params.pop(0)
        start = params.pop(0) if "bh.ngay_ban >= %s" in query else None
        end = params.pop(0) if "bh.ngay_ban <= %s" in query else None

        rows = [
            deepcopy(row)
            for row in self.database.state["ban_hang"]
            if row["nhan_vien_id"] == employee_id
        ]
        if keyword:
            text = keyword.strip("%").lower()
            rows = [
                row
                for row in rows
                if text in row["ma_ban"].lower()
            ]
        if status:
            rows = [row for row in rows if row["trang_thai"] == status]
        if start:
            rows = [row for row in rows if row["ngay_ban"] >= start]
        if end:
            rows = [row for row in rows if row["ngay_ban"] <= end]

        for row in rows:
            row.update(
                {
                    "ten_ca": "Ca Sáng",
                    "ma_nv": "NV007",
                    "ho_ten": "Nhân viên kiểm thử",
                    "ten_nhien_lieu": "Xăng A",
                    "don_vi": "lít",
                    "ma_bon": "BON01",
                    "ten_bon": "Bồn số 1",
                }
            )
        return rows

    def fetchone(self):
        return deepcopy(self.result)

    def fetchall(self):
        return deepcopy(self.results)

    def close(self):
        pass


class FakeSalesDatabase:
    def __init__(self):
        self.state = {
            "ton_hien_tai": 5,
            "ca_lam_viec": [
                {
                    "id": 11,
                    "ma_ca": "SANG",
                    "ten_ca": "Ca Sáng",
                    "ngay_lam_viec": date.today(),
                }
            ],
            "nhien_lieu": [
                {
                    "id": 3,
                    "ma_nhien_lieu": "NL001",
                    "ten_nhien_lieu": "Xăng A",
                    "don_vi": "lít",
                    "don_gia": Decimal("23000.00"),
                }
            ],
            "bon_chua": [
                {
                    "id": 21,
                    "ma_bon": "BON01",
                    "ten_bon": "Bồn số 1",
                    "nhien_lieu_id": 3,
                    "ton_hien_tai": 5,
                    "ten_nhien_lieu": "Xăng A",
                    "don_vi": "lít",
                },
                {
                    "id": 22,
                    "ma_bon": "BON02",
                    "ten_bon": "Bồn số 2",
                    "nhien_lieu_id": 99,
                    "ton_hien_tai": 50,
                    "ten_nhien_lieu": "Dầu B",
                    "don_vi": "lít",
                },
            ],
            "ban_hang": [],
        }
        self.last_insert = None
        self.last_cursor = None

    def cursor(self, dictionary=False):
        self.last_cursor = FakeSalesCursor(self)
        return self.last_cursor

    def start_transaction(self):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass

    def close(self):
        pass


def tao_phieu(trang_thai="Chờ duyệt", employee_id=7):
    return {
        "id": 51,
        "ma_ban": "BH260101000000ABCDEF",
        "ngay_ban": date.today(),
        "gio_ban": "13:00:00",
        "ca_lam_viec_id": 11,
        "nhan_vien_id": employee_id,
        "nhien_lieu_id": 3,
        "bon_id": 21,
        "so_luong": 2,
        "don_gia": Decimal("23000.00"),
        "thanh_tien": Decimal("46000.00"),
        "ghi_chu": None,
        "trang_thai": trang_thai,
    }


class NhanVienBanHangTests(unittest.TestCase):
    def setUp(self):
        self.database = FakeSalesDatabase()
        self.connection = self.database
        self.patcher = patch.object(
            ban_hang,
            "ket_noi",
            return_value=self.connection,
        )
        self.patcher.start()
        app.config.update(TESTING=True)
        self.client = app.test_client()
        with self.client.session_transaction() as session:
            session["tai_khoan_id"] = 1
            session["vai_tro"] = "Nhân viên ca"

    def tearDown(self):
        self.patcher.stop()

    def tao_payload(self, **ghi_de):
        payload = {
            "ca_lam_viec_id": "11",
            "nhien_lieu_id": "3",
            "bon_id": "21",
            "so_luong": "2",
            "ghi_chu": "",
        }
        payload.update(ghi_de)
        return payload

    def test_tao_phieu_cho_duyet_khong_tru_ton_va_tinh_gia_may_chu(self):
        ton_truoc = self.database.state["ton_hien_tai"]

        response = self.client.post(
            "/nhanvien/ban-hang/them",
            data=self.tao_payload(
                nhan_vien_id="999",
                don_gia="1",
                thanh_tien="1",
                trang_thai="Đã duyệt",
                ngay_ban="2000-01-01",
            ),
        )

        self.assertEqual(response.status_code, 302)
        phieu = self.database.last_insert
        self.assertIsNotNone(phieu)
        self.assertEqual(phieu["nhan_vien_id"], 7)
        self.assertEqual(phieu["don_gia"], Decimal("23000.00"))
        self.assertEqual(phieu["thanh_tien"], Decimal("46000.00"))
        self.assertEqual(phieu["trang_thai"], "Chờ duyệt")
        self.assertEqual(phieu["ca_lam_viec_id"], 11)
        self.assertEqual(self.database.state["ton_hien_tai"], ton_truoc)
        self.assertTrue(phieu["ma_ban"].startswith("BH"))

    def test_ma_ban_trung_duoc_sinh_lai(self):
        self.database.state["ma_ban_trung_lap"] = 1
        with patch.object(
            ban_hang,
            "tao_ma_ban",
            side_effect=["BH260101000000AAAAAA", "BH260101000001BBBBBB"],
        ):
            response = self.client.post(
                "/nhanvien/ban-hang/them",
                data=self.tao_payload(),
            )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            self.database.last_insert["ma_ban"],
            "BH260101000001BBBBBB",
        )

    def test_ton_tham_khao_thap_chi_canh_bao_khong_chan_tao_phieu(self):
        ca = self.database.state["ca_lam_viec"]
        fuels = self.database.state["nhien_lieu"]
        tanks = self.database.state["bon_chua"]

        errors, _, warning = ban_hang.kiem_tra_form(
            self.tao_payload(so_luong="8"),
            ca,
            fuels,
            tanks,
        )

        self.assertEqual(errors, {})
        self.assertIn("chưa trừ tồn", warning)
        response = self.client.post(
            "/nhanvien/ban-hang/them",
            data=self.tao_payload(so_luong="8"),
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(self.database.state["ban_hang"]), 1)
        self.assertEqual(self.database.state["ton_hien_tai"], 5)

    def test_tu_choi_du_lieu_sai_va_bon_khong_khop(self):
        for payload in (
            self.tao_payload(so_luong="0"),
            self.tao_payload(so_luong="-1"),
            self.tao_payload(so_luong="1.5"),
            self.tao_payload(so_luong="9" * 5000),
            self.tao_payload(ca_lam_viec_id="999"),
            self.tao_payload(bon_id="22"),
            self.tao_payload(nhien_lieu_id="999"),
        ):
            with self.subTest(payload=payload):
                response = self.client.post(
                    "/nhanvien/ban-hang/them",
                    data=payload,
                )
                self.assertEqual(response.status_code, 200)
                self.assertEqual(self.database.state["ban_hang"], [])

    def test_sua_phieu_cho_duyet_tinh_lai_tien_va_giu_nguyen_ton(self):
        self.database.state["ban_hang"].append(tao_phieu())
        ton_truoc = self.database.state["ton_hien_tai"]

        response = self.client.post(
            "/nhanvien/ban-hang/sua/51",
            data=self.tao_payload(
                so_luong="3",
                nhan_vien_id="999",
                don_gia="2",
                thanh_tien="2",
                trang_thai="Đã duyệt",
            ),
        )

        self.assertEqual(response.status_code, 302)
        phieu = self.database.state["ban_hang"][0]
        self.assertEqual(phieu["so_luong"], 3)
        self.assertEqual(phieu["don_gia"], Decimal("23000.00"))
        self.assertEqual(phieu["thanh_tien"], Decimal("69000.00"))
        self.assertEqual(phieu["trang_thai"], "Chờ duyệt")
        self.assertEqual(self.database.state["ton_hien_tai"], ton_truoc)

    def test_sua_khong_doi_gia_tri_van_duoc_chap_nhan(self):
        self.database.state["ban_hang"].append(tao_phieu())
        response = self.client.post(
            "/nhanvien/ban-hang/sua/51",
            data=self.tao_payload(
                so_luong="2",
                ghi_chu="",
            ),
        )
        self.assertEqual(response.status_code, 302)

    def test_tu_choi_sua_neu_phieu_vua_duoc_duyet(self):
        self.database.state["ban_hang"].append(tao_phieu())
        self.database.state["duyet_khi_khoa"] = True

        response = self.client.post(
            "/nhanvien/ban-hang/sua/51",
            data=self.tao_payload(so_luong="3"),
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            self.database.state["ban_hang"][0]["trang_thai"],
            "Đã duyệt",
        )

    def test_xoa_phieu_cho_duyet_khong_thay_doi_ton_va_chi_nhan_post(self):
        self.database.state["ban_hang"].append(tao_phieu())
        ton_truoc = self.database.state["ton_hien_tai"]

        get_response = self.client.get("/nhanvien/ban-hang/xoa/51")
        post_response = self.client.post("/nhanvien/ban-hang/xoa/51")

        self.assertEqual(get_response.status_code, 405)
        self.assertEqual(post_response.status_code, 302)
        self.assertEqual(self.database.state["ban_hang"], [])
        self.assertEqual(self.database.state["ton_hien_tai"], ton_truoc)

    def test_phieu_da_duyet_chi_xem_duoc(self):
        self.database.state["ban_hang"].append(tao_phieu("Đã duyệt"))

        self.assertEqual(
            self.client.get("/nhanvien/ban-hang/xem/51").status_code,
            200,
        )
        self.assertEqual(
            self.client.get("/nhanvien/ban-hang/sua/51").status_code,
            403,
        )
        self.assertEqual(
            self.client.post(
                "/nhanvien/ban-hang/sua/51",
                data=self.tao_payload(),
            ).status_code,
            403,
        )
        self.assertEqual(
            self.client.post("/nhanvien/ban-hang/xoa/51").status_code,
            403,
        )
        self.assertEqual(
            self.database.state["ban_hang"][0]["trang_thai"],
            "Đã duyệt",
        )

    def test_chi_truy_cap_phieu_cua_nhan_vien_hien_tai(self):
        self.database.state["ban_hang"].append(
            tao_phieu(employee_id=8)
        )

        self.assertEqual(
            self.client.get("/nhanvien/ban-hang/xem/51").status_code,
            404,
        )
        self.assertEqual(
            self.client.post("/nhanvien/ban-hang/xoa/51").status_code,
            404,
        )

    def test_tim_kiem_loc_trang_thai_va_ngay(self):
        self.database.state["ban_hang"].extend(
            [
                tao_phieu(),
                {
                    **tao_phieu("Đã duyệt"),
                    "id": 52,
                    "ma_ban": "BH-APPROVED",
                },
            ]
        )

        response = self.client.get(
            "/nhanvien/ban-hang",
            query_string={
                "q": "BH' OR 1=1 --",
                "trang_thai": "Chờ duyệt",
                "tu_ngay": date.today().isoformat(),
                "den_ngay": date.today().isoformat(),
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Kh\xc3\xb4ng t\xc3\xacm th\xe1\xba\xa5y phi\xe1\xba\xbfu", response.data)
        query = self.database.last_cursor.last_query
        params = self.database.last_cursor.last_params
        self.assertIn("bh.ma_ban LIKE %s", query)
        self.assertIn("bh.trang_thai = %s", query)
        self.assertIn("bh.ngay_ban >= %s", query)
        self.assertIn("bh.ngay_ban <= %s", query)
        self.assertIn("%BH' OR 1=1 --%", params)

    def test_loc_phieu_cho_duyet_tra_dung_ket_qua(self):
        self.database.state["ban_hang"].extend(
            [
                tao_phieu(),
                {
                    **tao_phieu("Đã duyệt"),
                    "id": 52,
                    "ma_ban": "BH-APPROVED",
                },
            ]
        )

        response = self.client.get(
            "/nhanvien/ban-hang",
            query_string={
                "q": "BH260101000000ABCDEF",
                "trang_thai": "Chờ duyệt",
                "tu_ngay": date.today().isoformat(),
                "den_ngay": date.today().isoformat(),
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"BH260101000000ABCDEF", response.data)
        self.assertNotIn(b"BH-APPROVED", response.data)

    def test_thong_ke_gom_tat_ca_phieu_va_chi_tinh_luong_da_duyet(self):
        self.database.state["ban_hang"].extend(
            [
                {**tao_phieu(), "so_luong": 500},
                {
                    **tao_phieu("Đã duyệt"),
                    "id": 52,
                    "ma_ban": "BH-APPROVED",
                    "so_luong": 2000,
                },
            ]
        )

        response = self.client.get(
            "/nhanvien/ban-hang",
            query_string={"trang_thai": "Chờ duyệt"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"T\xe1\xbb\x95ng s\xe1\xbb\x91 phi\xe1\xba\xbfu b\xc3\xa1n", response.data)
        self.assertIn(b">2<", response.data)
        self.assertIn(b">2,000 l\xc3\xadt<", response.data)
        self.assertIn(b">1<", response.data)

    def test_them_sua_xem_render_cac_template_tach_rieng(self):
        self.database.state["ban_hang"].append(tao_phieu())

        them = self.client.get("/nhanvien/ban-hang/them")
        sua = self.client.get("/nhanvien/ban-hang/sua/51")
        xem = self.client.get("/nhanvien/ban-hang/xem/51")

        self.assertEqual(them.status_code, 200)
        self.assertIn(b"cssnhanvien/banhang/them.css", them.data)
        self.assertIn(b"js/nhanvien/banhang/them.js", them.data)
        self.assertEqual(sua.status_code, 200)
        self.assertIn(b"cssnhanvien/banhang/sua.css", sua.data)
        self.assertIn(b"js/nhanvien/banhang/sua.js", sua.data)
        self.assertEqual(xem.status_code, 200)
        self.assertIn(b"cssnhanvien/banhang/xem.css", xem.data)

    def test_danh_sach_hien_thi_hop_xac_nhan_xoa_dung_mau(self):
        self.database.state["ban_hang"].append(tao_phieu())

        response = self.client.get("/nhanvien/ban-hang")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"cssnhanvien/banhang/xoa.css", response.data)
        self.assertIn(b'id="hop-xac-nhan" class="lop-phu"', response.data)
        self.assertIn("XÓA PHIẾU BÁN?".encode(), response.data)
        self.assertIn(b"ma-phieu-ban-xoa", response.data)
        self.assertIn(b'id="form-xoa" method="POST"', response.data)
        script = Path("static/js/nhanvien/banhang/index.js").read_text(
            encoding="utf-8"
        )
        self.assertIn('"/nhanvien/ban-hang/xoa/"', script)
        self.assertIn(b'type="button"', response.data)
        self.assertIn(b"nut-dong-y-xoa", response.data)

    def test_chua_dang_nhap_hoac_sai_vai_tro_khong_truy_cap_duoc(self):
        with self.client.session_transaction() as session:
            session.clear()
        self.assertEqual(
            self.client.get("/nhanvien/ban-hang").status_code,
            302,
        )

        with self.client.session_transaction() as session:
            session["tai_khoan_id"] = 1
            session["vai_tro"] = "Quản lý"
        self.assertEqual(
            self.client.get("/nhanvien/ban-hang").status_code,
            403,
        )

    def test_loi_ket_noi_database_duoc_tra_loi_ro_rang(self):
        with patch.object(
            ban_hang,
            "ket_noi",
            side_effect=mysql.connector.Error("database unavailable"),
        ):
            response = self.client.get("/nhanvien/ban-hang")

        self.assertEqual(response.status_code, 503)
        self.assertIn(b"Kh\xc3\xb4ng th\xe1\xbb\x83 k\xe1\xba\xbft n\xe1\xbb\x91i", response.data)


if __name__ == "__main__":
    unittest.main()
