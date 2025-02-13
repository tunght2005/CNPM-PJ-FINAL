// document.addEventListener("DOMContentLoaded", () => {
//     const cart = document.querySelector(".cart");
//     const subtotalElement = document.querySelector(".subtotal");
//     const totalElement = document.querySelector(".total");

//     const updateTotal = () => {
//         const itemPrices = Array.from(document.querySelectorAll(".item-price p"));
//         const subtotal = itemPrices.reduce((total, priceElement) => {
//             return total + parseInt(priceElement.textContent.replace(/[^0-9]/g, ""), 10);
//         }, 0);
//         subtotalElement.textContent = `${subtotal.toLocaleString()}₫`;  
//         totalElement.textContent = `${subtotal.toLocaleString()}₫`;
//     };

//     cart.addEventListener("click", (e) => {
//         if (e.target.classList.contains("btn-remove")) {
//             e.target.closest(".cart-item").remove();
//             updateTotal();
//         }
//     });

//     cart.addEventListener("click", (e) => {
//         const quantityInput = e.target.closest(".quantity").querySelector(".quantity-input");
//         let quantity = parseInt(quantityInput.value, 10);

//         if (e.target.classList.contains("btn-increase")) {
//             quantityInput.value = quantity + 1;
//         } else if (e.target.classList.contains("btn-decrease") && quantity > 1) {
//             quantityInput.value = quantity - 1;
//         }
//         updateTotal();
//     });

//     updateTotal();
// });
var updateBtns = document.getElementsByClassName('update-cart')

for ( i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action', action)
        console.log('USER:', user)
        if (user === 'AnonymousUser'){
            console.log('User is not logined')
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is logined, sending data...')
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}