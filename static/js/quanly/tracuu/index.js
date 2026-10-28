document.addEventListener("DOMContentLoaded", () => {
    // 1. Hiệu ứng Chạy số đếm (Number Counter Animation) cho các thẻ thống kê
    const soLieuElements = document.querySelectorAll(".tra-cuu-the strong");
    
    soLieuElements.forEach(el => {
        const textGoc = el.innerText.trim();
        // Lọc lấy các con số (hỗ trợ định dạng thập phân, dấu phẩy)
        const soSach = parseFloat(textGoc.replace(/[^0-9.-]+/g, ""));
        
        if (isNaN(soSach) || soSach === 0) return;

        let hienTai = 0;
        const thoiGianChay = 900; // 0.9 giây
        const buocNhanh = 25; 
        const soBuoc = thoiGianChay / buocNhanh;
        const tangMoiBuoc = soSach / soBuoc;

        const boDem = setInterval(() => {
            hienTai += tangMoiBuoc;
            if (hienTai >= soSach) {
                hienTai = soSach;
                clearInterval(boDem);
            }
            // Giữ lại ký hiệu tiền tệ hoặc đơn vị đo phía sau (ví dụ: ₫, L,...)
            const phanDu = textGoc.replace(/[0-9,.-]+/g, "");
            el.innerText = Math.round(hienTai).toLocaleString('en-US') + " " + phanDu;
        }, buocNhanh);
    });

    // 2. Hiệu ứng trượt lên (Slide-up & Fade-in) mượt mà khi cuộn chuột
    const cacKhung = document.querySelectorAll(".tra-cuu-the, .tra-cuu-bo-loc, .tra-cuu-khu-vuc");
    
    cacKhung.forEach(khung => {
        khung.style.opacity = "0";
        khung.style.transform = "translateY(20px)";
        khung.style.transition = "opacity 0.5s ease-out, transform 0.5s ease-out";
    });

    const kiemTraCuonChuot = () => {
        cacKhung.forEach(khung => {
            const viTriKhung = khung.getBoundingClientRect().top;
            const chieuCaoManHinh = window.innerHeight * 0.92;
            if (viTriKhung < chieuCaoManHinh) {
                khung.style.opacity = "1";
                khung.style.transform = "translateY(0)";
            }
        });
    };

    window.addEventListener("scroll", kiemTraCuonChuot);
    kiemTraCuonChuot(); // Chạy ngay lần đầu load trang

    // 3. Hiệu ứng gợn sóng (Ripple Effect) khi bấm nút Tra cứu
    const nutTraCuu = document.querySelector(".tra-cuu-hanh-dong button");
    if (nutTraCuu) {
        nutTraCuu.addEventListener("click", function (e) {
            const x = e.clientX - e.target.getBoundingClientRect().left;
            const y = e.clientY - e.target.getBoundingClientRect().top;

            const gionSong = document.createElement("span");
            gionSong.style.position = "absolute";
            gionSong.style.left = x + "px";
            gionSong.style.top = y + "px";
            gionSong.style.width = "0px";
            gionSong.style.height = "0px";
            gionSong.style.background = "rgba(255, 255, 255, 0.4)";
            gionSong.style.borderRadius = "50%";
            gionSong.style.transform = "translate(-50%, -50%)";
            gionSong.style.transition = "width 0.4s ease-out, height 0.4s ease-out, opacity 0.4s ease-out";
            gionSong.style.pointerEvents = "none";
            
            this.style.position = "relative";
            this.style.overflow = "hidden";
            this.appendChild(gionSong);

            setTimeout(() => {
                gionSong.style.width = "180px";
                gionSong.style.height = "180px";
                gionSong.style.opacity = "0";
            }, 10);

            setTimeout(() => {
                gionSong.remove();
            }, 400);
        });
    }

    // 4. Hiệu ứng Loading nhẹ mờ dần khi submit form bộ lọc
    const formBoLoc = document.querySelector(".tra-cuu-bo-loc");
    if (formBoLoc) {
        formBoLoc.addEventListener("submit", () => {
            const khuVucBang = document.querySelectorAll(".tra-cuu-khu-vuc");
            khuVucBang.forEach(khuVuc => {
                khuVuc.style.opacity = "0.4";
                khuVuc.style.transition = "opacity 0.2s ease";
            });
        });
    }

    // 5. Hiệu ứng nổi bật dòng bảng (Row Highlight Effect) khi di chuột qua
    const cacDongBang = document.querySelectorAll(".tra-cuu-cuon-bang tbody tr");
    cacDongBang.forEach(dong => {
        dong.addEventListener("mouseenter", () => {
            dong.style.transition = "background-color 0.15s ease";
            dong.style.backgroundColor = "#e0f2fe"; // Màu xanh da trời nhạt nổi bật
        });
        dong.addEventListener("mouseleave", () => {
            dong.style.backgroundColor = "";
        });
    });
});