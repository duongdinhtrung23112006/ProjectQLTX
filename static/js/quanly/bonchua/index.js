const oTimKiem = document.getElementById(
    "timKiemBonChua"
);

const danhSach = document.getElementById(
    "danhSachBonChua"
);

// =========================
// TÌM KIẾM
// =========================

oTimKiem.addEventListener(
    "input",
    function () {

        const tuKhoa = oTimKiem.value
            .trim()
            .toLowerCase();


        const cacDong = danhSach.querySelectorAll(
            "tr"
        );


        cacDong.forEach(function (dong) {

            if (dong.cells.length < 3) {
                return;
            }


            const maBon =
                dong.cells[0]
                    .textContent
                    .trim()
                    .toLowerCase();


            const tenBon =
                dong.cells[1]
                    .textContent
                    .trim()
                    .toLowerCase();


            const nhienLieu =
                dong.cells[2]
                    .textContent
                    .trim()
                    .toLowerCase();


            const phuHop =
                maBon.includes(tuKhoa) ||
                tenBon.includes(tuKhoa) ||
                nhienLieu.includes(tuKhoa);


            dong.style.display =
                phuHop ? "" : "none";

        });

    }
);


// =========================
// CHẠY SẮP XẾP KHI MỞ TRANG
// =========================

sapXepTheoMaBon();