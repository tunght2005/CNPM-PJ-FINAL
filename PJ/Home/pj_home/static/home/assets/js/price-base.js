
  document.addEventListener("DOMContentLoaded", function () {
    // Khởi tạo giỏ hàng và giao diện
    updateCartCount();
    initCartButtons();
    initStorageObserver();
  });

  // Hàm xử lý chung cho cả 2 nút
  function handleCartAction(productId, actionType) {
    const productPrice = parseFloat(
      document.querySelector(".product-price").textContent.replace(/\D/g, "")
    ) || 0;
    
    const cart = JSON.parse(localStorage.getItem("cart")) || [];
    const product = {
      product_id: productId,
      quantity: 1,
      price: productPrice,
      name: this.dataset.pname,
      image: this.dataset.image
    };

    const existingItem = cart.find(item => item.product_id === productId);
    
    if (existingItem) {
      existingItem.quantity++;
    } else {
      cart.push(product);
    }

    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartCount();

    if (actionType === 'buy-now') {
      window.location.href = "/cart/";
    } else {
      showNotification("Sản phẩm đã được thêm vào giỏ hàng!");
    }
  }

  // Khởi tạo event listeners
  function initCartButtons() {
    document.querySelectorAll(".add-to-cart, .buy-now").forEach(button => {
      button.addEventListener("click", function() {
        handleCartAction.call(this, this.dataset.id, 
          this.classList.contains("buy-now") ? 'buy-now' : 'add-to-cart'
        );
      });
    });
  }

  // Cập nhật số lượng giỏ hàng
  function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem("cart")) || [];
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    document.querySelector(".number-cart").textContent = totalItems;
  }

  // Theo dõi thay đổi từ các tab khác
  function initStorageObserver() {
    window.addEventListener('storage', (e) => {
      if (e.key === 'cart') updateCartCount();
    });
  }
