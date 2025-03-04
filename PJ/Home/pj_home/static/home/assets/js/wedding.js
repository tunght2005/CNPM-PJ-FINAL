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
  window.location.href = 'pj_home'; // Đảm bảo rằng đây là đường dẫn chính xác
});

// Sự kiện khi nhấn vào "Trang Sức Cưới"
jewelryPageButton.addEventListener('click', (e) => {
  // Ngăn không cho trang tải lại (nếu muốn làm gì đó trước khi chuyển)
  e.preventDefault();
  
  // Chuyển hướng đến trang Trang Sức Cưới
  window.location.href = 'wedding_page'; // Đảm bảo rằng đây là đường dẫn chính xác
});

var arrTSC = [
  { loaiTS: 'Nhẫn', hinh: '/static/home/assets/img/image/images.jpg', TenSP: 'Nhẫn vàng 18k D&C 1010CGHSK298', GT: 'Sang trọng và quý phái', MT: 'Hẹn Hò', KC: 'Không Đính Kim Cương', CL: 'Vàng 18K', Gia: '17,999,000đ' },
  { loaiTS: 'Vòng Tay', hinh: '/static/home/assets/img/image/images(4).jpg', TenSP: 'Vòng tay vàng 18k BTK901', GT: 'Kỷ Niệm', MT: 'Kỷ Niệm', KC: 'Đính Kim Cương', CL: 'Vàng 18K', Gia: '25,499,000đ' },
  { loaiTS: 'Dây Chuyền', hinh: '/static/home/assets/img/image/images(10).jpg', TenSP: 'Dây chuyền vàng 24k DC102', GT: 'Kết Hôn', MT: 'Kết Hôn', KC: 'Không Đính Kim Cương', CL: 'Vàng 24K', Gia: '30,999,000đ' },
  { loaiTS: 'Bông Tai', hinh: '/static/home/assets/img/image/image(7).jpg', TenSP: 'Bông tai vàng 18k BT105', GT: 'Phong cách hiện đại', MT: 'Hẹn Hò', KC: 'Đính Đá Màu', CL: 'Vàng 18K', Gia: '12,999,000đ' },
  { loaiTS: 'Kiềng', hinh: '/static/home/assets/img/image/image(13).jpg', TenSP: 'Kiềng vàng 24k KG204', GT: 'Cầu Hôn', MT: 'Cầu Hôn', KC: 'Không Đính Kim Cương', CL: 'Vàng 24K', Gia: '45,999,000đ' },
  { loaiTS: 'Nhẫn', hinh: '/static/home/assets/img/image/images(2).jpg', TenSP: 'Nhẫn cưới vàng 18k NC101', GT: 'Tinh tế và đẳng cấp', MT: 'Kết Hôn', KC: 'Đính Kim Cương', CL: 'Vàng 18K', Gia: '22,999,000đ' },
  { loaiTS: 'Vòng Tay', hinh: '/static/home/assets/img/image/image(5).jpg', TenSP: 'Vòng tay bạc BTK902', GT: 'Đơn giản và thanh thoát', MT: 'Hẹn Hò', KC: 'Đính Đá Màu', CL: 'Vàng 18K', Gia: '15,499,000đ' },
  { loaiTS: 'Dây Chuyền', hinh: '/static/home/assets/img/image/images(11).jpg', TenSP: 'Dây chuyền vàng 18k DC103', GT: 'Kỷ Niệm', MT: 'Kỷ Niệm', KC: 'Đính Kim Cương', CL: 'Vàng 18K', Gia: '35,999,000đ' },
  { loaiTS: 'Bông Tai', hinh: '/static/home/assets/img/image/image(8).jpg', TenSP: 'Bông tai vàng 24k BT106', GT: 'Cầu Hôn', MT: 'Cầu Hôn', KC: 'Không Đính Kim Cương', CL: 'Vàng 24K', Gia: '18,999,000đ' },
  { loaiTS: 'Kiềng', hinh: '/static/home/assets/img/image/image(14).jpg', TenSP: 'Kiềng vàng 18k KG205', GT: 'Hẹn Hò', MT: 'Hẹn Hò', KC: 'Đính Kim Cương', CL: 'Vàng 18K', Gia: '50,999,000đ' },
  { loaiTS: 'Nhẫn', hinh: '/static/home/assets/img/image/images(3).jpg', TenSP: 'Nhẫn bạc D&C 1010', GT: 'Kỷ Niệm', MT: 'Kỷ Niệm', KC: 'Không Đính Kim Cương', CL: 'Vàng 18K', Gia: '9,999,000đ' },
  { loaiTS: 'Vòng Tay', hinh: '/static/home/assets/img/image/th1.jpg', TenSP: 'Vòng tay vàng 18k BTK903', GT: 'Cầu Hôn', MT: 'Cầu Hôn', KC: 'Đính Kim Cương', CL: 'Vàng 18K', Gia: '28,499,000đ' },
  { loaiTS: 'Dây Chuyền', hinh: '/static/home/assets/img/image/image(12).jpg', TenSP: 'Dây chuyền vàng 18k DC104', GT: 'Kết Hôn', MT: 'Kết Hôn', KC: 'Đính Đá Màu', CL: 'Vàng 18K', Gia: '20,999,000đ' },
  { loaiTS: 'Bông Tai', hinh: '/static/home/assets/img/image/image(9).jpg', TenSP: 'Bông tai vàng 24k BT107', GT: 'Kỷ Niệm', MT: 'Kỷ Niệm', KC: 'Đính Kim Cương', CL: 'Vàng 24K', Gia: '25,999,000đ' },
  { loaiTS: 'Kiềng', hinh: '/static/home/assets/img/image/image(15).jpg', TenSP: 'Kiềng vàng 18k KG206', GT: 'Kỷ Niệm', MT: 'Kỷ Niệm', KC: 'Không Đính Kim Cương', CL: 'Vàng 18K', Gia: '40,999,000đ' }
];




// Hàm hiển thị sản phẩm
function HienTSC(loaiTS = '', mucTieu = '', KC = '', CL = '') {
  var list1 = document.getElementById("list1");
  list1.innerHTML = ''; // Xóa danh sách cũ

  arrTSC.forEach(function (sanPham) {
    if (
      (loaiTS === '' || sanPham.loaiTS === loaiTS) &&
      (mucTieu === '' || sanPham.MT === mucTieu) &&
      (KC === '' || sanPham.KC === KC) &&
      (CL === '' || sanPham.CL === CL)
    ) {
      list1.innerHTML += `
        <div class="TSC">
          <img src="${sanPham.hinh}" alt="${sanPham.TenSP}" />
          <h3>${sanPham.TenSP}</h3>
          <h4>${sanPham.GT}</h4>
        </div>
      `;
    }
  });
}

// Hàm xử lý khi người dùng nhấn vào menu
function ChonTSCMenu(loai, giaTri) {
  // Xác định loại dữ liệu lọc (loaiTS, MT, KC, CL)
  switch (loai) {
    case 'loaiTS':
      HienTSC(giaTri, '', '', '');
      break;
    case 'MT':
      HienTSC('', giaTri, '', '');
      break;
    case 'KC':
      HienTSC('', '', giaTri, '');
      break;
    case 'CL':
      HienTSC('', '', '', giaTri);
      break;
    default:
      HienTSC(); // Hiển thị toàn bộ sản phẩm nếu không có lọc
  }
}

// Hiển thị toàn bộ sản phẩm mặc định
HienTSC();
function toggleMainPanel() {
  const mainPanel = document.getElementById("shipping-details");
  
  // Khi click vào "Chính Sách Giao Hàng", toggle hiển thị các mục bên trong
  mainPanel.style.display = (mainPanel.style.display === "block") ? "none" : "block";
}

// Hàm này mở/đóng phần nội dung của các mục
function togglePanel(element) {
  const panel = element.nextElementSibling; // Lấy phần nội dung kế bên tiêu đề
  
  // Đóng tất cả các panel khác
  const allPanels = document.querySelectorAll(".panel");
  allPanels.forEach(function(p) {
    if (p !== panel) {
      p.classList.remove("show");
    }
  });

  // Toggle hiển thị phần nội dung của mục được click
  panel.classList.toggle("show");
}