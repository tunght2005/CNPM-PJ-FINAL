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

// Mở modal khi click vào "Điều Kiện"
// Mở modal khi click vào "Điều Kiện"
var conditionLinks = document.querySelectorAll('.condition-link');
conditionLinks.forEach(function(link) {
    link.onclick = function() {
        var modalId = link.getAttribute('data-modal'); // Lấy id của modal cần mở
        var modal = document.getElementById(modalId);
        modal.style.display = "block";
    }
});

// Đóng modal khi click vào nút x
function closeModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = "none";
}

// Đóng modal khi người dùng click ngoài cửa sổ modal
window.onclick = function(event) {
    conditionLinks.forEach(function(link) {
        var modal = document.getElementById(link.getAttribute('data-modal'));
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
}
