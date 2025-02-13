document.addEventListener("DOMContentLoaded", function () {
  const tabs = document.querySelectorAll(".tab");
  const orderItems = document.querySelectorAll(".order-item");
  const searchInput = document.getElementById("searchInput");
  const searchBtn = document.getElementById("searchBtn");

  // Chức năng chuyển tab
  tabs.forEach((tab) => {
    tab.addEventListener("click", function () {
      const tabCategory = tab.getAttribute("data-tab");

      // Xóa trạng thái active khỏi tất cả tab
      tabs.forEach((t) => t.classList.remove("active"));
      tab.classList.add("active");

      // Ẩn tất cả đơn hàng
      orderItems.forEach((item) => {
        if (
          tabCategory === "all" ||
          item.getAttribute("data-category") === tabCategory
        ) {
          item.classList.add("active");
        } else {
          item.classList.remove("active");
        }
      });
    });
  });

  // Kích hoạt tab "Tất cả đơn" mặc định
  document.querySelector(".tab[data-tab='all']").click();

  // Lọc đơn hàng theo từ khóa
  searchBtn.addEventListener("click", function () {
    const searchText = searchInput.value.toLowerCase().trim();

    orderItems.forEach((item) => {
      const orderText = item.textContent.toLowerCase();
      if (orderText.includes(searchText)) {
        item.classList.add("active"); // Hiển thị đơn hàng nếu có kết quả tìm kiếm
      } else {
        item.classList.remove("active"); // Ẩn đơn hàng nếu không có kết quả tìm kiếm
      }
    });
  });

  // Tự động lọc khi người dùng nhập vào input tìm kiếm
  searchInput.addEventListener("input", function () {
    const searchText = searchInput.value.toLowerCase().trim();

    orderItems.forEach((item) => {
      const orderText = item.textContent.toLowerCase();
      if (orderText.includes(searchText)) {
        item.classList.add("active");
      } else {
        item.classList.remove("active");
      }
    });
  });
});
