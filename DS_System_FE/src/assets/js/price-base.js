// Giả lập backend truyền giá gốc sang frontend
const basePriceFromBackend = 10458000; // Giá từ backend

// Gán giá gốc vào thẻ HTML
document
  .getElementById("base-price")
  .setAttribute("data-base-price", basePriceFromBackend);
document.getElementById("base-price").textContent =
  basePriceFromBackend.toLocaleString("vi-VN");

// Lấy giá gốc từ thuộc tính data-base-price
const basePrice = parseFloat(
  document.getElementById("base-price").getAttribute("data-base-price")
);

// Lấy tất cả các nút chọn size
const sizeButtons = document.querySelectorAll(".size-btn");
// Lấy phần tử hiển thị giá
const productPrice = document.querySelector(".product-price");

// Thêm sự kiện click cho từng nút
sizeButtons.forEach((button) => {
  button.addEventListener("click", () => {
    // Lấy phần trăm tăng từ thuộc tính data-percent
    const percentIncrease = parseFloat(button.getAttribute("data-percent"));

    // Tính giá mới
    const newPrice = basePrice * (1 + percentIncrease / 100);

    // Cập nhật giá hiển thị và định dạng tiền tệ
    productPrice.innerHTML = `
      ${Math.round(newPrice).toLocaleString("vi-VN")} <span>VNĐ</span>
    `;
  });
});
// Lấy tất cả các nút chọn size
const sizeButton = document.querySelectorAll(".size-btn");

// Thêm sự kiện click cho từng nút
sizeButton.forEach((button) => {
  button.addEventListener("click", () => {
    // Xóa lớp active khỏi tất cả các nút
    sizeButton.forEach((btn) => btn.classList.remove("active"));
    // Thêm lớp active cho nút được nhấn
    button.classList.add("active");
  });
});
