const oTimKiem = document.getElementById(
    "timKiemCaLamViec"
);

const danhSach = document.getElementById(
    "danhSachCaLamViec"
);


// =========================
// SẮP XẾP THEO NGÀY LÀM VIỆC
// =========================

function sapXepTheoNgayLamViec() {

    const cacDong = Array.from(
        danhSach.querySelectorAll("tr")
    );


    cacDong.sort(function (dongA, dongB) {

        const ngayA =
            dongA.cells[2]
                .textContent
                .trim();

        const ngayB =
            dongB.cells[2]
                .textContent
                .trim();


        /*
         * Ngày đang có dạng:
         *
         * dd/mm/yyyy
         *
         * Chuyển thành:
         *
         * yyyy-mm-dd
         *
         * để JavaScript so sánh chính xác.
         */

        const phanA = ngayA.split("/");
        const phanB = ngayB.split("/");


        if (
            phanA.length !== 3 ||
            phanB.length !== 3
        ) {
            return 0;
        }


        const ngayChuanA =
            new Date(
                phanA[2],
                phanA[1] - 1,
                phanA[0]
            );


        const ngayChuanB =
            new Date(
                phanB[2],
                phanB[1] - 1,
                phanB[0]
            );


        return ngayChuanA - ngayChuanB;

    });


    cacDong.forEach(function (dong) {

        danhSach.appendChild(dong);

    });

}


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