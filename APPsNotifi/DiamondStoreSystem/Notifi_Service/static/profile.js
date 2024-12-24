// Thông báo
document.addEventListener("DOMContentLoaded", function () {
  const deleteButtons = document.querySelectorAll(".button.delete");
  const markReadButtons = document.querySelectorAll(".button:not(.delete)");
  const notification = document.getElementById("notification");

  function showNotification(message, color = "#28a745") {
    notification.textContent = message;
    notification.style.backgroundColor = color;
    notification.style.display = "block";
    setTimeout(() => {
      notification.style.display = "none";
    }, 3000);
  }

  deleteButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const row = button.closest("tr");
      row.remove();
      showNotification("Đơn hàng đã được xóa.", "#dc3545");
    });
  });

  markReadButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const row = button.closest("tr");
      row.classList.add("active");
      button.textContent = "Đã Đọc";
      button.style.backgroundColor = "#6c757d";
      button.style.pointerEvents = "none";
      showNotification("Đơn hàng đã được đánh dấu là đã đọc.");
    });
  });
});
