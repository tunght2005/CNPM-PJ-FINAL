const searchMenu = document.querySelector("#search-menu");
const wrapSearch = document.querySelector(".search");
const searchCancel = document.querySelector("#search-btn-cancel");
const searchMain = document.querySelector(".search-main");
const searchSub = document.querySelector(".search-sub");
const searchBar = document.querySelector("#search-input");
const subMenu = document.querySelector(".sub-menu-1");
const subMenu2 = document.querySelector(".sub-menu-2");
const subMenu3 = document.querySelector(".sub-menu-3");
const subMenu4 = document.querySelector(".sub-menu-4");
const subMenu5 = document.querySelector(".sub-menu-5");
const menuItem1 = document.querySelector("#item-1");
const menuItem2 = document.querySelector("#item-2");
const menuItem3 = document.querySelector("#item-3");
const menuItem4 = document.querySelector("#item-4");
const menuItem5 = document.querySelector("#item-5");

// Sự kiện khi nhấn vào nút search-menu
searchMenu.addEventListener("click", () => {
  wrapSearch.classList.add("active");
});
searchCancel.addEventListener("click", () => {
  wrapSearch.classList.remove("active");
});
searchBar.addEventListener("input", () => {
  if (searchBar.value.trim() !== "") {
    searchMain.classList.add("hidden");
    searchSub.classList.add("active");
  } else {
    searchMain.classList.remove("hidden");
    searchSub.classList.remove("active");
  }
});

// Menu Sub 1
menuItem1.addEventListener("mouseenter", () => {
  subMenu.classList.add("active");
});

menuItem1.addEventListener("mouseleave", () => {
  setTimeout(() => {
    if (!subMenu.matches(":hover") && !menuItem1.matches(":hover")) {
      subMenu.classList.remove("active");
    }
  }, 200);
});

subMenu.addEventListener("mouseleave", () => {
  setTimeout(() => {
    if (!menuItem1.matches(":hover")) {
      subMenu.classList.remove("active");
    }
  }, 200);
});
// Menu Sub 2
menuItem2.addEventListener("mouseenter", () => {
  subMenu2.classList.add("active");
});

menuItem2.addEventListener("mouseleave", () => {
  setTimeout(() => {
    if (!subMenu2.matches(":hover") && !menuItem2.matches(":hover")) {
      subMenu2.classList.remove("active");
    }
  }, 200);
});

subMenu2.addEventListener("mouseleave", () => {
  setTimeout(() => {
    if (!menuItem2.matches(":hover")) {
      subMenu2.classList.remove("active");
    }
  }, 200);
});
//Menu Sub 3
menuItem3.addEventListener("mouseenter", () => {
  subMenu3.classList.add("active");
});

menuItem3.addEventListener("mouseleave", () => {
  setTimeout(() => {
    if (!subMenu3.matches(":hover") && !menuItem3.matches(":hover")) {
      subMenu3.classList.remove("active");
    }
  }, 200);
});

subMenu3.addEventListener("mouseleave", () => {
  setTimeout(() => {
    if (!menuItem3.matches(":hover")) {
      subMenu3.classList.remove("active");
    }
  }, 200);
});
//Menu Sub 4
menuItem4.addEventListener("mouseenter", () => {
  subMenu4.classList.add("active");
});

menuItem4.addEventListener("mouseleave", () => {
  setTimeout(() => {
    if (!subMenu4.matches(":hover") && !menuItem4.matches(":hover")) {
      subMenu4.classList.remove("active");
    }
  }, 200);
});

subMenu4.addEventListener("mouseleave", () => {
  setTimeout(() => {
    if (!menuItem4.matches(":hover")) {
      subMenu4.classList.remove("active");
    }
  }, 200);
});
//Menu Sub 5
menuItem5.addEventListener("mouseenter", () => {
  subMenu5.classList.add("active");
});

menuItem5.addEventListener("mouseleave", () => {
  setTimeout(() => {
    if (!subMenu5.matches(":hover") && !menuItem5.matches(":hover")) {
      subMenu5.classList.remove("active");
    }
  }, 200);
});

subMenu5.addEventListener("mouseleave", () => {
  setTimeout(() => {
    if (!menuItem5.matches(":hover")) {
      subMenu5.classList.remove("active");
    }
  }, 200);
});

let currentSlide = 0; // Slide hiện tại

function moveSlide(direction) {
  const images = document.querySelectorAll('.carousel-image');
  const totalSlides = images.length;

  currentSlide += direction;

  // Kiểm tra nếu currentSlide vượt quá phạm vi, quay lại đầu hoặc cuối
  if (currentSlide < 0) {
    currentSlide = totalSlides - 1;
  } else if (currentSlide >= totalSlides) {
    currentSlide = 0;
  }

  // Điều chỉnh vị trí của carousel
  const carousel = document.querySelector('.carousel');
  carousel.style.transform = `translateX(-${currentSlide * 100}%)`;
}



document.addEventListener('DOMContentLoaded', function () {
  // Chọn phần tử trang chủ
  const homeButton = document.querySelector('#homeButton');

  // Kiểm tra nếu phần tử tồn tại
  if (homeButton) {
    // Thêm sự kiện khi nhấn vào trang chủ
    homeButton.addEventListener('click', function(event) {
      event.preventDefault();  // Ngừng hành động mặc định (di chuyển đến trang khác)
      
      // Chuyển hướng về trang chủ
      window.location.href = 'index.html';  // Điều hướng đến trang chủ
    });
  }
});
// Lấy phần tử nút "Trang Chủ" và "Trang Sức Cưới"
const homeButton = document.getElementById('homeButton');
const jewelryPageButton = document.getElementById('jewelryPageButton');

// Sự kiện khi nhấn vào "Trang Chủ"
homeButton.addEventListener('click', (e) => {
  // Ngăn không cho trang tải lại (nếu muốn làm gì đó trước khi chuyển)
  e.preventDefault();
  
  // Chuyển hướng đến trang chủ
  window.location.href = 'index.html'; // Đảm bảo rằng đây là đường dẫn chính xác
});

// Sự kiện khi nhấn vào "Trang Sức Cưới"
jewelryPageButton.addEventListener('click', (e) => {
  // Ngăn không cho trang tải lại (nếu muốn làm gì đó trước khi chuyển)
  e.preventDefault();
  
  // Chuyển hướng đến trang Trang Sức Cưới
  window.location.href = 'webding.html'; // Đảm bảo rằng đây là đường dẫn chính xác
});

// Dữ liệu sản phẩm
var arrTSC = [
  { TenSP: 'Nhẫn vàng 18k D&C 1010CGHSK298', hinh: 'image/images.jpg', loaiTS: 'Nhẫn', MT: 'Hẹn Hò', KC: 'Không Đính Kim Cương', CL: 'Vàng 18K', GT: '17,999,000đ' },
  { TenSP: 'Vòng tay vàng 18k BTK901', hinh: 'image/images(4).jpg', loaiTS: 'Vòng Tay', MT: 'Kỷ Niệm', KC: 'Đính Kim Cương', CL: 'Vàng 18K', GT: '25,499,000đ' },
  { TenSP: 'Dây chuyền vàng 24k DC102', hinh: 'image/images(10).jpg', loaiTS: 'Dây Chuyền', MT: 'Kết Hôn', KC: 'Không Đính Kim Cương', CL: 'Vàng 24K', GT: '30,999,000đ' },
  { TenSP: 'Bông tai vàng 18k BT105', hinh: 'image/image(7).jpg', loaiTS: 'Bông Tai', MT: 'Hẹn Hò', KC: 'Đính Đá Màu', CL: 'Vàng 18K', GT: '12,999,000đ' },
  { TenSP: 'Kiềng vàng 24k KG204', hinh: 'image/image(13).jpg', loaiTS: 'Kiềng', MT: 'Cầu Hôn', KC: 'Không Đính Kim Cương', CL: 'Vàng 24K', GT: '45,999,000đ' },
  { TenSP: 'Nhẫn cưới vàng 18k NC101', hinh: 'image/images(2).jpg', loaiTS: 'Nhẫn', MT: 'Kết Hôn', KC: 'Đính Kim Cương', CL: 'Vàng 18K', GT: '22,999,000đ' },
  { TenSP: 'Vòng tay bạc BTK902', hinh: 'image/image(5).jpg', loaiTS: 'Vòng Tay', MT: 'Hẹn Hò', KC: 'Đính Đá Màu', CL: 'Vàng 18K', GT: '15,499,000đ' },
  { TenSP: 'Dây chuyền vàng 18k DC103', hinh: 'image/images(11).jpg', loaiTS: 'Dây Chuyền', MT: 'Kỷ Niệm', KC: 'Đính Kim Cương', CL: 'Vàng 18K', GT: '35,999,000đ' },
  { TenSP: 'Bông tai vàng 24k BT106', hinh: 'image/image(8).jpg', loaiTS: 'Bông Tai', MT: 'Cầu Hôn', KC: 'Không Đính Kim Cương', CL: 'Vàng 24K', GT: '18,999,000đ' },
  { TenSP: 'Kiềng vàng 18k KG205', hinh: 'image/image(14).jpg', loaiTS: 'Kiềng', MT: 'Hẹn Hò', KC: 'Đính Kim Cương', CL: 'Vàng 18K', GT: '50,999,000đ' },
  { TenSP: 'Nhẫn bạc D&C 1010', hinh: 'image/images(3).jpg', loaiTS: 'Nhẫn', MT: 'Kỷ Niệm', KC: 'Không Đính Kim Cương', CL: 'Vàng 18K', GT: '9,999,000đ' },
  { TenSP: 'Vòng tay vàng 18k BTK903', hinh: 'image/th1.jpg', loaiTS: 'Vòng Tay', MT: 'Cầu Hôn', KC: 'Đính Kim Cương', CL: 'Vàng 18K', GT: '28,499,000đ' },
  { TenSP: 'Dây chuyền vàng 18k DC104', hinh: 'image/image(12).jpg', loaiTS: 'Dây Chuyền', MT: 'Kết Hôn', KC: 'Đính Đá Màu', CL: 'Vàng 18K', GT: '20,999,000đ' },
  { TenSP: 'Bông tai vàng 24k BT107', hinh: 'image/image(9).jpg', loaiTS: 'Bông Tai', MT: 'Kỷ Niệm', KC: 'Đính Kim Cương', CL: 'Vàng 24K', GT: '25,999,000đ' },
  { TenSP: 'Kiềng vàng 18k KG206', hinh: 'image/image(15).jpg', loaiTS: 'Kiềng', MT: 'Kỷ Niệm', KC: 'Không Đính Kim Cương', CL: 'Vàng 18K', GT: '40,999,000đ' }
];

// Hàm hiển thị sản phẩm
function HienTSC(loaiSanPhamChon, mucTieuChon, dinhKCChon, chatLieuChon) {
  var list1 = document.getElementById("list1");
  list1.innerHTML = '';

  for (i = 0; i < arrTSC.length; i++) {
    // Kiểm tra xem sản phẩm có thỏa mãn các điều kiện lọc không
    if (
      (loaiSanPhamChon.length === 0 || loaiSanPhamChon.includes(arrTSC[i].loaiTS)) &&
      (mucTieuChon.length === 0 || mucTieuChon.includes(arrTSC[i].MT)) &&
      (dinhKCChon.length === 0 || dinhKCChon.includes(arrTSC[i].KC)) &&
      (chatLieuChon.length === 0 || chatLieuChon.includes(arrTSC[i].CL))
    ) {
      list1.innerHTML += `
        <div class="TSC">
          <img src="${arrTSC[i].hinh}" />
          <h3>${arrTSC[i].TenSP}</h3>
          <h4>${arrTSC[i].GT}</h4>
        </div>
      `;
    }
  }
}

// Hàm xử lý khi người dùng chọn các checkbox
function ChonTSC() {
  var loaiSanPhamChon = [];
  var mucTieuChon = [];
  var dinhKCChon = [];
  var chatLieuChon = [];

  var loaiTS = document.getElementsByClassName("loaiTS");
  var MT = document.getElementsByClassName("MT");
  var KC = document.getElementsByClassName("KC");
  var CL = document.getElementsByClassName("CL");

  // Lấy các giá trị được chọn trong mỗi nhóm checkbox
  for (i = 0; i < loaiTS.length; i++) {
    if (loaiTS[i].checked) loaiSanPhamChon.push(loaiTS[i].value);
  }
  for (i = 0; i < MT.length; i++) {
    if (MT[i].checked) mucTieuChon.push(MT[i].value);
  }
  for (i = 0; i < KC.length; i++) {
    if (KC[i].checked) dinhKCChon.push(KC[i].value);
  }
  for (i = 0; i < CL.length; i++) {
    if (CL[i].checked) chatLieuChon.push(CL[i].value);
  }

  // Gọi hàm HienTSC với các giá trị đã chọn
  HienTSC(loaiSanPhamChon, mucTieuChon, dinhKCChon, chatLieuChon);
}

// Gọi lần đầu tiên để hiển thị tất cả sản phẩm
HienTSC([], [], [], []);