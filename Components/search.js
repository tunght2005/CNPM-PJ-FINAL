const searchMenu = document.querySelector("#search-menu");
const wrapSearch = document.querySelector(".search");
const searchCancel = document.querySelector("#search-btn-cancel");
const searchMain = document.querySelector(".search-main");
const searchSub = document.querySelector(".search-sub");
const searchBar = document.querySelector("#search-input");
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
