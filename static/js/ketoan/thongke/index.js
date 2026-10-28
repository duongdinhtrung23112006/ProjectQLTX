(() => {
    // 1. Logic cũ của bạn: Xử lý bật/tắt trường tùy chỉnh ngày tháng
    const selectKhoang = document.getElementById("tk-khoang");
    const truongNgay = document.querySelectorAll(".tk-ngay-tuy-chinh");

    if (selectKhoang && truongNgay.length) {
        const capNhatTruongNgay = () => {
            const tuyChinh = selectKhoang.value === "tuy_chinh";
            truongNgay.forEach((truong) => {
                if (truong instanceof HTMLInputElement) {
                    truong.disabled = !tuyChinh;
                    truong.required = tuyChinh;
                }
            });
        };

        selectKhoang.addEventListener("change", capNhatTruongNgay);
        capNhatTruongNgay();
    }

    // 2. Hiệu ứng Chạy số đếm (Number Counter Animation) cho các thẻ KPI & số liệu
    const soLieuElements = document.querySelectorAll(".tk-the-kpi strong, .tk-bon-so-lieu strong");
    
    const chaySoDem = (el) => {
        const textGoc = el.innerText.trim();
        // Lọc lấy các ký tự số (hỗ trợ cả dấu phẩy, dấu chấm)
        const soSach = parseFloat(textGoc.replace(/[^0-9.-]+/g, ""));
        
        if (isNaN(soSach) || soSach === 0) return;

        let hienTai = 0;
        const thoiGianChay = 1000; // 1 giây
        const buocNnhay = 25; // Tần số khung hình
        const soBuoc = thoiGianChay / buocNnhay;
        const tangMoiBuoc = soSach / soBuoc;

        const boDem = setInterval(() => {
            hienTai += tangMoiBuoc;
            if (hienTai >= soSach) {
                hienTai = soSach;
                clearInterval(boDem);
            }
            // Giữ nguyên định dạng tiền tệ hoặc chữ phía sau nếu có (ví dụ: ₫, L,...)
            const phanDu = textGoc.replace(/[0-9,.-]+/g, "");
            el.innerText = Math.round(hienTai).toLocaleString('en-US') + " " + phanDu;
        }, buocNnhay);
    };

    // Kích hoạt chạy số khi trang tải xong
    soLieuElements.forEach(el => chaySoDem(el));

    // 3. Hiệu ứng trượt lên (Slide-up) mượt mà cho các khối khi cuộn chuột
    const cacKhung = document.querySelectorAll(".tk-the-kpi, .tk-khung-bieu-do, .tk-the-bon, .tk-giao-dich");
    
    // Thêm class chuẩn bị ẩn
    cacKhung.forEach(khung => {
        khung.style.opacity = "0";
        khung.style.transform = "translateY(25px)";
        khung.style.transition = "opacity 0.6s ease-out, transform 0.6s ease-out";
    });

    const kiemTraCuonChuot = () => {
        cacKhung.forEach(khung => {
            const viTriKhung = khung.getBoundingClientRect().top;
            const chieuCaoManHinh = window.innerHeight * 0.9;
            if (viTriKhung < chieuCaoManHinh) {
                khung.style.opacity = "1";
                khung.style.transform = "translateY(0)";
            }
        });
    };

    window.addEventListener("scroll", kiemTraCuonChuot);
    // Chạy luôn 1 lần đầu để load các khối ở màn hình đầu tiên
    kiemTraCuonChuot();

    // 4. Hiệu ứng gợn sóng (Ripple) khi bấm nút
    const cacNut = document.querySelectorAll("button, .tk-nut-phu");
    cacNut.forEach(nut => {
        nut.addEventListener("click", function (e) {
            const x = e.clientX - e.target.offsetLeft;
            const y = e.clientY - e.target.offsetTop;

            const gionSong = document.createElement("span");
            gionSong.style.position = "absolute";
            gionSong.style.left = x + "px";
            gionSong.style.top = y + "px";
            gionSong.style.width = "0px";
            gionSong.style.height = "0px";
            gionSong.style.background = "rgba(255, 255, 255, 0.5)";
            gionSong.style.borderRadius = "50%";
            gionSong.style.transform = "translate(-50%, -50%)";
            gionSong.style.transition = "width 0.4s ease-out, height 0.4s ease-out, opacity 0.4s ease-out";
            gionSong.style.pointerEvents = "none";
            
            this.style.position = "relative";
            this.style.overflow = "hidden";
            this.appendChild(gionSong);

            setTimeout(() => {
                gionSong.style.width = "200px";
                gionSong.style.height = "200px";
                gionSong.style.opacity = "0";
            }, 10);

            setTimeout(() => {
                gionSong.remove();
            }, 400);
        });
    });

    // 5. Hiệu ứng Loading nhẹ khi submit form lọc dữ liệu
    const formBoLoc = document.querySelector(".tk-bo-loc");
    if (formBoLoc) {
        formBoLoc.addEventListener("submit", () => {
            const bangDuLieu = document.querySelector(".tk-giao-dich, .tk-luoi-bieu-do");
            if (bangDuLieu) {
                bangDuLieu.style.opacity = "0.5";
                bangDuLieu.style.transition = "opacity 0.2s ease";
            }
        });
    }
})();