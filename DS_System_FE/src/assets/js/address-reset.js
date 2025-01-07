document.getElementById("add-address").addEventListener("click", function () {
  const addressList = document.getElementById("address-list");

  const newCard = document.createElement("div");
  newCard.className = "address-card";
  newCard.innerHTML = `
              <div class="address-info">
                  <strong>Tên mới</strong>
                  <p>Địa chỉ: Địa chỉ mới thêm vào</p>
                  <p>Điện thoại: 0123456789</p>
              </div>
              <a href="#" class="edit-link">Chỉnh sửa</a>
          `;

  addressList.appendChild(newCard);
});

let currentCard = null;

document
  .getElementById("address-list")
  .addEventListener("click", function (event) {
    if (event.target.classList.contains("edit-link")) {
      const addressInfo =
        event.target.parentElement.querySelector(".address-info");
      currentCard = addressInfo;

      document.getElementById("edit-name").value =
        addressInfo.querySelector("strong").textContent;
      document.getElementById("edit-address").value = addressInfo
        .querySelector("p:nth-of-type(1)")
        .textContent.replace("Địa chỉ: ", "");
      document.getElementById("edit-phone").value = addressInfo
        .querySelector("p:nth-of-type(2)")
        .textContent.replace("Điện thoại: ", "");

      document.getElementById("edit-modal").style.display = "flex";
    }
  });

document.getElementById("save-btn").addEventListener("click", function () {
  if (currentCard) {
    currentCard.querySelector("strong").textContent =
      document.getElementById("edit-name").value;
    currentCard.querySelector("p:nth-of-type(1)").textContent = `Địa chỉ: ${
      document.getElementById("edit-address").value
    }`;
    currentCard.querySelector("p:nth-of-type(2)").textContent = `Điện thoại: ${
      document.getElementById("edit-phone").value
    }`;
  }

  document.getElementById("edit-modal").style.display = "none";
});

document.getElementById("cancel-btn").addEventListener("click", function () {
  document.getElementById("edit-modal").style.display = "none";
});
