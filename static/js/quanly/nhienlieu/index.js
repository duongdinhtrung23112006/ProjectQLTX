const oTimKiem = document.getElementById(
    "timKiemNhienLieu"
);

const danhSach = document.getElementById(
    "danhSachNhienLieu"
);


// =========================
// SẮP XẾP THEO MÃ NHIÊN LIỆU
// =========================

function sapXepTheoMaNhienLieu() {

    const cacDong = Array.from(
        danhSach.querySelectorAll("tr")
    );


    cacDong.sort(function (dongA, dongB) {

        const maA = dongA.cells[0]
            .textContent
            .trim();

        const maB = dongB.cells[0]
            .textContent
            .trim();


        return maA.localeCompare(
            maB,
            undefined,
            {
                numeric: true,
                sensitivity: "base"
            }
        );

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

        const tuKhoa = oTimKiem.value
            .trim()
            .toLowerCase();


        const cacDong = danhSach.querySelectorAll(
            "tr"
        );


        cacDong.forEach(function (dong) {

            if (dong.cells.length < 2) {
                return;
            }


            const maNhienLieu =
                dong.cells[0]
                    .textContent
                    .trim()
                    .toLowerCase();


            const tenNhienLieu =
                dong.cells[1]
                    .textContent
                    .trim()
                    .toLowerCase();


            const phuHop =
                maNhienLieu.includes(tuKhoa) ||
                tenNhienLieu.includes(tuKhoa);


            dong.style.display =
                phuHop ? "" : "none";

        });

    }
);


// =========================
// SẮP XẾP KHI MỞ TRANG
// =========================

sapXepTheoMaNhienLieu();