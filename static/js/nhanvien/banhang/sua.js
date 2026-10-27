(function () {
    const nhienLieuSelect = document.getElementById("nhien_lieu_id");
    const bonSelect = document.getElementById("bon_id");
    const soLuongInput = document.getElementById("so_luong");
    const donGia = document.getElementById("donGiaHienTai");
    const donVi = document.getElementById("donViNhienLieu");
    const thanhTien = document.getElementById("thanhTienDuKien");

    if (!nhienLieuSelect || !bonSelect || !soLuongInput || !donGia || !thanhTien) {
        return;
    }

    function capNhatGiaTri() {
        const luaChonNhienLieu =
            nhienLieuSelect.options[nhienLieuSelect.selectedIndex];
        const gia = Number(luaChonNhienLieu.dataset.donGia);
        const soLuong = Number(soLuongInput.value);
        const coGia = luaChonNhienLieu.value && Number.isFinite(gia);

        donGia.textContent = coGia
            ? gia.toLocaleString("vi-VN", { maximumFractionDigits: 2 }) + " / đơn vị"
            : "Chọn nhiên liệu";
        thanhTien.textContent = coGia && Number.isFinite(soLuong) && soLuong > 0
            ? (gia * soLuong).toLocaleString("vi-VN", { maximumFractionDigits: 2 })
            : "0";
        if (donVi) {
            donVi.textContent = luaChonNhienLieu.dataset.donVi || "đơn vị";
        }

        Array.from(bonSelect.options).forEach(function (luaChonBon) {
            const khopNhienLieu =
                !luaChonBon.value ||
                !nhienLieuSelect.value ||
                luaChonBon.dataset.nhienLieuId === nhienLieuSelect.value;
            luaChonBon.hidden = !khopNhienLieu;
        });

        const bonDaChon = bonSelect.options[bonSelect.selectedIndex];
        if (
            bonSelect.value &&
            bonDaChon.dataset.nhienLieuId !== nhienLieuSelect.value
        ) {
            bonSelect.value = "";
        }
    }

    nhienLieuSelect.addEventListener("change", capNhatGiaTri);
    soLuongInput.addEventListener("input", capNhatGiaTri);
    capNhatGiaTri();
})();
