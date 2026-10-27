(function () {
    const danhSach = document.querySelector(".khung-bang-ban-hang");
    const hopXacNhan = document.getElementById("hop-xac-nhan");
    const maPhieuXoa = document.getElementById("ma-phieu-ban-xoa");
    const formXoa = document.getElementById("form-xoa");
    const nutDong = document.getElementById("dong-hop-xac-nhan");

    if (!danhSach || !hopXacNhan || !maPhieuXoa || !formXoa || !nutDong) {
        return;
    }

    danhSach.addEventListener("click", function (event) {
        const nutXoa = event.target.closest(".nut-xoa");

        if (!nutXoa) {
            return;
        }

        maPhieuXoa.textContent = nutXoa.dataset.ma;
        formXoa.action = "/nhanvien/ban-hang/xoa/" + nutXoa.dataset.id;
        hopXacNhan.classList.add("hien-thi");
    });

    function dongHopXacNhan() {
        hopXacNhan.classList.remove("hien-thi");
        formXoa.removeAttribute("action");
    }

    nutDong.addEventListener("click", dongHopXacNhan);

    hopXacNhan.addEventListener("click", function (event) {
        if (event.target === hopXacNhan) {
            dongHopXacNhan();
        }
    });

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && hopXacNhan.classList.contains("hien-thi")) {
            dongHopXacNhan();
        }
    });
})();
