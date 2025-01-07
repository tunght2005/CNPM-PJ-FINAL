// Lấy các phần tử DOM
const sizeGuideBtn = document.getElementById("static");
const sizeGuidePopup = document.getElementById("size-guide-popup");
const closePopupBtn = document.getElementById("close-popup");

// Hiển thị popup khi nhấn vào "Cách đo dây cổ"
sizeGuideBtn.addEventListener("click", () => {
  sizeGuidePopup.style.display = "flex";
});

// Ẩn popup khi nhấn vào nút đóng
closePopupBtn.addEventListener("click", () => {
  sizeGuidePopup.style.display = "none";
});

// Ẩn popup khi click bên ngoài nội dung
window.addEventListener("click", (e) => {
  if (e.target === sizeGuidePopup) {
    sizeGuidePopup.style.display = "none";
  }
});
