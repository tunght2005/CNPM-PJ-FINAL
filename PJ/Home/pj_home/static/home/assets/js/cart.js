document.addEventListener("DOMContentLoaded", () => {
    const cart = document.querySelector(".cart");
    const subtotalElement = document.querySelector(".subtotal");
    const totalElement = document.querySelector(".total");

    const updateTotal = () => {
        const itemPrices = Array.from(document.querySelectorAll(".item-price p"));
        const subtotal = itemPrices.reduce((total, priceElement) => {
            return total + parseInt(priceElement.textContent.replace(/[^0-9]/g, ""), 10);
        }, 0);
        subtotalElement.textContent = `${subtotal.toLocaleString()}₫`;  
        totalElement.textContent = `${subtotal.toLocaleString()}₫`;
    };

    cart.addEventListener("click", (e) => {
        if (e.target.classList.contains("btn-remove")) {
            e.target.closest(".cart-item").remove();
            updateTotal();
        }
    });

    cart.addEventListener("click", (e) => {
        const quantityInput = e.target.closest(".quantity").querySelector(".quantity-input");
        let quantity = parseInt(quantityInput.value, 10);

        if (e.target.classList.contains("btn-increase")) {
            quantityInput.value = quantity + 1;
        } else if (e.target.classList.contains("btn-decrease") && quantity > 1) {
            quantityInput.value = quantity - 1;
        }
        updateTotal();
    });

    updateTotal();
});
