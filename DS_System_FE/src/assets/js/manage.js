document.addEventListener("DOMContentLoaded", function () {
  const tabs = document.querySelectorAll(".tab");
  const orderItems = document.querySelectorAll(".order-item");

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
});
