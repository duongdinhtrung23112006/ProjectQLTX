function moHopXacNhan(
    id,
    maNhap
) {

    document.getElementById(
        "ma-phieu-nhap-xoa"
    ).textContent =
        maNhap;


    document.getElementById(
        "form-xoa"
    ).action =
        "/quanly/nhap-hang/xoa/" + id;


    document.getElementById(
        "hop-xac-nhan"
    ).classList.add(
        "hien-thi"
    );
}


function dongHopXacNhan() {

    document.getElementById(
        "hop-xac-nhan"
    ).classList.remove(
        "hien-thi"
    );

}