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

// slideshow

const slider = document.querySelector('.slider .qc');
const images = document.querySelectorAll('.slider .qc img');
const dots = document.querySelectorAll('.dots .dot');
const totalImages = images.length;

let currentIndex = 0;
let intervalId;

function updateSlider() {
  slider.style.transform = `translateX(-${currentIndex * 100}%)`;
  dots.forEach(dot => dot.classList.remove('active'));
  dots[currentIndex].classList.add('active');
}

function showNextImage() {
  currentIndex++;
  if (currentIndex >= totalImages) {
    currentIndex = 0;
  }
  updateSlider();
}

function goToImage(index) {
  currentIndex = index;
  updateSlider();
}

dots.forEach(dot => {
  dot.addEventListener('click', (event) => {
    const index = parseInt(event.target.getAttribute('data-index'));
    goToImage(index);
    resetAutoSlide();
  });
});

function startAutoSlide() {
  intervalId = setInterval(showNextImage, 3000);
}

function resetAutoSlide() {
  clearInterval(intervalId);
  startAutoSlide();
}

updateSlider();
startAutoSlide();
// Câu hỏi thường gặp
document.addEventListener("DOMContentLoaded", () => {
  const faqTitles = document.querySelectorAll(".faq-title");
  const subFaqTitles = document.querySelectorAll(".sub-faq-title");

  faqTitles.forEach(title => {
      title.addEventListener("click", () => {
          const content = title.nextElementSibling;
          content.style.display = content.style.display === "block" ? "none" : "block";

          faqTitles.forEach(otherTitle => {
              if (otherTitle !== title) {
                  otherTitle.nextElementSibling.style.display = "none";
              }
          });
      });
  });

  subFaqTitles.forEach(subTitle => {
      subTitle.addEventListener("click", () => {
          const subContent = subTitle.nextElementSibling;
          subContent.style.display = subContent.style.display === "block" ? "none" : "block";
      });
  });
});

// Lọc sản phẩm theo thương hiệu
function filterProducts() {
  const selectedBrand = document.getElementById('brandFilter').value;
  const selectedMaterial = document.getElementById('materialFilter').value;
  const selectedShape = document.getElementById('shapeFilter').value;
  const products = document.querySelectorAll('#productList .danhmuchinhanh');

  products.forEach((product) => {
    const matchesBrand = selectedBrand === 'Thương hiệu' || product.dataset.brand === selectedBrand;
    const matchesMaterial = selectedMaterial === undefined || selectedMaterial === 'Chất liệu dây' || product.dataset.material === selectedMaterial;
    const matchesShape = selectedShape === 'Hình dạng mặt' || product.dataset.shape === selectedShape;

    if (matchesBrand && matchesMaterial && matchesShape) {
      product.style.display = 'block';
    } else {
      product.style.display = 'none';
    }
  });
}

// Xử lý sự kiện thay đổi của bộ lọc thương hiệu
document.getElementById('brandFilter').addEventListener('change', filterProducts);
document.getElementById('materialFilter').addEventListener('change', filterProducts);
document.getElementById('shapeFilter').addEventListener('change', filterProducts);

// Thêm sự kiện cho nút hủy lọc
document.getElementById('clearFilter').addEventListener('click', () => {
  // Đặt lại bộ lọc về giá trị mặc định
  document.getElementById('brandFilter').value = 'Thương hiệu';
  document.getElementById('materialFilter').value = 'Chất liệu dây';
  document.getElementById('shapeFilter').value = 'Hình dạng mặt';

  // Hiển thị tất cả các sản phẩm khi hủy lọc
  const products = document.querySelectorAll('#productList .danhmuchinhanh');
  products.forEach(product => {
    product.style.display = 'block';
  });
});




// bộ lọc sắp xếp
document.getElementById('filterSelect').addEventListener('change', function () {
  const filterValue = this.value;
  const productList = document.getElementById('productList');
  const products = Array.from(productList.children);

  if (filterValue === 'Thapcao') {
    
    products.sort((a, b) => getPrice(a) - getPrice(b));
  } else if (filterValue === 'Caothap') {
    
    products.sort((a, b) => getPrice(b) - getPrice(a));
  } else if (filterValue === 'New') {
   
    products.sort((a, b) => a.dataset.order - b.dataset.order);
  } else if (filterValue === 'Popular') {
    
    products.sort((a, b) => getPopularity(b) - getPopularity(a));
  }

  products.forEach((product) => productList.appendChild(product));
});

function getPrice(product) {
  const priceText = product.querySelector('p').textContent;
  return parseFloat(priceText.replace(/[^\d]/g, ''));
}

function getPopularity(product) {
  return parseInt(product.dataset.popularity || 0);
}
