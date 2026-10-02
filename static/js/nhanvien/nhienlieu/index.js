const oTimKiem = document.getElementById(
    "timKiemNhienLieu"
);

const danhSach = document.getElementById(
    "danhSachNhienLieu"
);


// =========================
// TÌM KIẾM
// =========================

if (oTimKiem && danhSach) {

    oTimKiem.addEventListener(
        "input",
        function () {

            const tuKhoa = oTimKiem.value
                .trim()
                .toLowerCase();

            const cacDong =
                danhSach.querySelectorAll("tr");

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

}