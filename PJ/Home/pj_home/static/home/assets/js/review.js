const openFormBtn = document.getElementById("open-review-form");
const reviewForm = document.getElementById("review-form");
const reviewFormElement = document.getElementById("reviewForm");
const notification = document.getElementById("notification");
const closeNotification = document.getElementById("close-notification");
const totalReviews = document.getElementById("total-reviews");
const averageRating = document.querySelector(".average-rating");

let reviewCount = 0;
let totalStars = 0;

// Hiển thị form khi nhấn "Viết đánh giá"
openFormBtn.addEventListener("click", () => {
  reviewForm.style.display = "block"; // Hiển thị form
  notification.style.display = "none"; // Ẩn thông báo nếu đang hiển thị
});

reviewFormElement.addEventListener("submit", (e) => {
  e.preventDefault();
  notification.style.display = "flex"; // Hiển thị thông báo

  // Lấy dữ liệu từ form
  const username = document.getElementById("username").value;
  const rating = parseInt(document.getElementById("rating").value);
  const comment = document.getElementById("comment").value;

  console.log("Tên:", username, "Số sao:", rating, "Bình luận:", comment);

  // Cập nhật số lượng đánh giá và tính trung bình sao
  reviewCount++;
  totalStars += rating;
  const average = (totalStars / reviewCount).toFixed(1);

  totalReviews.textContent = reviewCount;
  averageRating.textContent = average;

  // Ẩn form sau khi submit
  reviewForm.style.display = "none";
  reviewFormElement.reset();
});

closeNotification.addEventListener("click", () => {
  notification.style.display = "none"; // Ẩn thông báo
});
