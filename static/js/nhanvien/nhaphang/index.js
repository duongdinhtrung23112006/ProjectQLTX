(function () {

    function khoiTaoNhapHang() {

        const oTimKiem =
            document.getElementById("timKiemPhieuNhap");

        const danhSach =
            document.getElementById("danhSachPhieuNhap");

        const hopXacNhan =
            document.getElementById("hop-xac-nhan");

        const maPhieuXoa =
            document.getElementById("ma-phieu-nhap-xoa");

        const formXoa =
            document.getElementById("form-xoa");

        const nutDong =
            document.getElementById("dong-hop-xac-nhan");


        if (!oTimKiem || !danhSach) {
            return;
        }


        // ==========================================
        // TÌM KIẾM
        // ==========================================

        oTimKiem.addEventListener("input", function () {

            const tuKhoa =
                this.value.toLowerCase().trim();

            const cacDong =
                danhSach.querySelectorAll("tr");

            cacDong.forEach(function (dong) {

                const noiDung =
                    dong.textContent.toLowerCase();

                dong.style.display =
                    noiDung.includes(tuKhoa)
                        ? ""
                        : "none";

            });

        });


        // ==========================================
        // MỞ HỘP XÁC NHẬN
        // ==========================================

        danhSach.addEventListener(
            "click",
            function (event) {

                const nutXoa =
                    event.target.closest(".nut-xoa");

                if (!nutXoa) {
                    return;
                }

                const id =
                    nutXoa.dataset.id;

                const ma =
                    nutXoa.dataset.ma;

                maPhieuXoa.textContent = ma;

                formXoa.action =
                    `/nhanvien/nhap-hang/xoa/${id}`;

                hopXacNhan.classList.remove("an");

            }
        );


        // ==========================================
        // ĐÓNG
        // ==========================================

        nutDong.addEventListener(
            "click",
            function () {

                hopXacNhan.classList.add("an");

            }
        );


        hopXacNhan.addEventListener(
            "click",
            function (event) {

                if (event.target === hopXacNhan) {

                    hopXacNhan.classList.add("an");

                }

            }
        );

    }


    khoiTaoNhapHang();

})();