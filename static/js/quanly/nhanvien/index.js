const oTimKiem = document.getElementById(
    "timKiemNhanVien"
);

const danhSach = document.getElementById(
    "danhSachNhanVien"
);


// =========================
// SẮP XẾP THEO NGÀY VÀO LÀM
// =========================

function sapXepTheoNgayVaoLam() {

    const cacDong = Array.from(
        danhSach.querySelectorAll("tr")
    );


    cacDong.sort(function (dongA, dongB) {

        /*
         * Bỏ qua dòng:
         *
         * "Chưa có nhân viên nào..."
         */

        if (
            dongA.cells.length < 7 ||
            dongB.cells.length < 7
        ) {
            return 0;
        }


        const ngayA =
            dongA.cells[4]
                .textContent
                .trim();


        const ngayB =
            dongB.cells[4]
                .textContent
                .trim();


        /*
         * Nếu không có ngày
         * thì đưa xuống cuối.
         */

        if (ngayA === "—" && ngayB === "—") {
            return 0;
        }

        if (ngayA === "—") {
            return 1;
        }

        if (ngayB === "—") {
            return -1;
        }


        /*
         * Ngày đang có dạng:
         *
         * dd/mm/yyyy
         *
         * Chuyển thành Date
         * để so sánh chính xác.
         */

        const phanA = ngayA.split("/");
        const phanB = ngayB.split("/");


        if (
            phanA.length !== 3 ||
            phanB.length !== 3
        ) {
            return 0;
        }


        const ngayChuanA = new Date(
            phanA[2],
            phanA[1] - 1,
            phanA[0]
        );


        const ngayChuanB = new Date(
            phanB[2],
            phanB[1] - 1,
            phanB[0]
        );


        /*
         * Cũ → mới
         */

        return ngayChuanA - ngayChuanB;

    });


    /*
     * Đưa các dòng đã sắp xếp
     * trở lại tbody.
     */

    cacDong.forEach(function (dong) {

        danhSach.appendChild(dong);

    });

}


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