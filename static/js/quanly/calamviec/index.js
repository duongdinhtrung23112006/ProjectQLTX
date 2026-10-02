const oTimKiem = document.getElementById(
    "timKiemCaLamViec"
);

const danhSach = document.getElementById(
    "danhSachCaLamViec"
);


// =========================
// TÌM KIẾM
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
                 * "Chưa có ca làm việc..."
                 */

                if (dong.cells.length < 8) {
                    return;
                }


                const maCa =
                    dong.cells[0]
                        .textContent
                        .trim()
                        .toLowerCase();


                const tenCa =
                    dong.cells[1]
                        .textContent
                        .trim()
                        .toLowerCase();


                const ngayLamViec =
                    dong.cells[2]
                        .textContent
                        .trim()
                        .toLowerCase();


                const nhanVien =
                    dong.cells[5]
                        .textContent
                        .trim()
                        .toLowerCase();


                const phuHop =
                    maCa.includes(tuKhoa) ||
                    tenCa.includes(tuKhoa) ||
                    ngayLamViec.includes(tuKhoa) ||
                    nhanVien.includes(tuKhoa);


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

sapXepTheoNgayLamViec();