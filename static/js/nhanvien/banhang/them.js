(function () {
    "use strict";

    const nhienLieuSelect = document.getElementById("nhien_lieu_id");
    const bonSelect = document.getElementById("bon_id");
    const soLuongInput = document.getElementById("so_luong");
    const donGiaDiv = document.getElementById("donGiaHienTai");
    const donViSpan = document.getElementById("donViNhienLieu");
    const thanhTienDiv = document.getElementById("thanhTienDuKien");

    if (!nhienLieuSelect || !bonSelect || !soLuongInput || !donGiaDiv || !thanhTienDiv) {
        return;
    }

    function capNhatGiaVaLocBon() {
        const luaChonNhienLieu = nhienLieuSelect.options[nhienLieuSelect.selectedIndex];
        const gia = Number(luaChonNhienLieu.dataset.donGia);
        const soLuong = Number(soLuongInput.value);
        const coGia = luaChonNhienLieu.value && Number.isFinite(gia);

        // 1. Cập nhật hiển thị đơn giá
        donGiaDiv.textContent = coGia
            ? gia.toLocaleString("vi-VN", { maximumFractionDigits: 2 }) + " đ / " + (luaChonNhienLieu.dataset.donVi || "đơn vị")
            : "Chọn nhiên liệu";

        // 2. Tính tiền dự kiến ngay lập tức (khi gõ số lượng dù là 1 lít)
        if (coGia && Number.isFinite(soLuong) && soLuong > 0) {
            const thanhTien = gia * soLuong;
            thanhTienDiv.textContent = thanhTien.toLocaleString("vi-VN", { maximumFractionDigits: 2 }) + " đ";
        } else {
            thanhTienDiv.textContent = "0 đ";
        }

        // 3. Cập nhật nhãn đơn vị ở ô số lượng
        if (donViSpan) {
            donViSpan.textContent = luaChonNhienLieu.dataset.donVi || "lít";
        }

        // 4. Lọc tự động bồn chứa theo nhiên liệu được chọn
        const nhienLieuIdHienTai = nhienLieuSelect.value;

        Array.from(bonSelect.options).forEach(function (luaChonBon) {
            if (!luaChonBon.value) return; // Bỏ qua option mặc định

            const bonNhienLieuId = luaChonBon.dataset.nhienLieuId;
            const khop = !nhienLieuIdHienTai || bonNhienLieuId === nhienLieuIdHienTai;

            luaChonBon.hidden = !khop;
            luaChonBon.style.display = khop ? "" : "none";
        });

        // Nếu bồn đang chọn không thuộc nhiên liệu mới -> tự động reset về trống
        const bonDaChon = bonSelect.options[bonSelect.selectedIndex];
        if (bonSelect.value && bonDaChon && bonDaChon.dataset.nhienLieuId !== nhienLieuIdHienTai) {
            bonSelect.value = "";
        }
    }

    // Lắng nghe các sự kiện thay đổi dữ liệu
    nhienLieuSelect.addEventListener("change", capNhatGiaVaLocBon);
    soLuongInput.addEventListener("input", capNhatGiaVaLocBon);
    soLuongInput.addEventListener("keyup", capNhatGiaVaLocBon);
    soLuongInput.addEventListener("change", capNhatGiaVaLocBon);

    // Chạy ngay khi load trang (đề phòng trường hợp load lại form có dữ liệu cũ)
    capNhatGiaVaLocBon();
})();