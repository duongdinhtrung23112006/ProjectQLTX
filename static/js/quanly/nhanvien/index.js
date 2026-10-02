const oTimKiem = document.getElementById(
    "timKiemNhanVien"
);

const danhSach = document.getElementById(
    "danhSachNhanVien"
);

// =========================
// TÌM KIẾM NHÂN VIÊN
// =========================

oTimKiem.addEventListener(
    "input",
    function () {

        const tuKhoa =
            oTimKiem.value
                .trim()
                .toLowerCase();


        const cacDong =
            danhSach.querySelectorAll("tr");


        cacDong.forEach(
            function (dong) {

                /*
                 * Bỏ qua dòng
                 * "Chưa có nhân viên..."
                 */

                if (dong.cells.length < 7) {
                    return;
                }


                /*
                 * Cột 0:
                 * Mã nhân viên
                 */

                const maNhanVien =
                    dong.cells[0]
                        .textContent
                        .trim()
                        .toLowerCase();


                /*
                 * Cột 1:
                 * Họ và tên
                 */

                const hoTen =
                    dong.cells[1]
                        .textContent
                        .trim()
                        .toLowerCase();


                /*
                 * Cột 3:
                 * Chức vụ
                 */

                const chucVu =
                    dong.cells[3]
                        .textContent
                        .trim()
                        .toLowerCase();


                /*
                 * Kiểm tra từ khóa
                 * có xuất hiện ở một
                 * trong ba trường hay không.
                 */

                const phuHop =
                    maNhanVien.includes(tuKhoa) ||
                    hoTen.includes(tuKhoa) ||
                    chucVu.includes(tuKhoa);


                /*
                 * Hiện / ẩn dòng.
                 */

                dong.style.display =
                    phuHop
                        ? ""
                        : "none";

            }
        );

    }
);


// =========================
// SẮP XẾP KHI MỞ TRANG
// =========================

sapXepTheoNgayVaoLam();