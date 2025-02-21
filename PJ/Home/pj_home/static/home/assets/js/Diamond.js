document.addEventListener("DOMContentLoaded", () => {
    const storeTitles = document.querySelectorAll(".store-title");
    const storesContainer = document.querySelector(".vertical-stores-container");
    const stateSelector = document.getElementById("elm_stores_state");
    const districtSelector = document.getElementById("elm_stores_district_hidden");

    // Hiển thị mặc định một số cửa hàng
    const defaultStoreIds = ["store_title1386", "store_title1387","store_title1388","store_title1389","store_title1390","store_title1391","store_title1392","store_title1393","store_title1394"]; // ID của các cửa hàng mặc định
    storeTitles.forEach((title) => {
        const storeContentId = title.getAttribute("id").replace("store_title", "store_content");
        const storeContent = document.getElementById(storeContentId);

        if (defaultStoreIds.includes(title.getAttribute("id"))) {
            storeContent.style.display = "none";
            title.classList.add("show-info");
        } else {
            storeContent.style.display = "none";
        }

        title.addEventListener("click", () => {
            // Đóng tất cả các cửa hàng khác
            document.querySelectorAll(".store-item").forEach((item) => {
                if (item !== storeContent) {
                    item.style.display = "none";
                }
            });

            // Đổi trạng thái hiện/ẩn của cửa hàng hiện tại
            if (storeContent.style.display === "block") {
                storeContent.style.display = "none";
                title.classList.remove("show-info");
            } else {
                storeContent.style.display = "block";
                title.classList.add("show-info");
            }
        });
    });

    // Xử lý khi thay đổi Tỉnh/Thành phố
    stateSelector.addEventListener("change", () => {
        const selectedState = stateSelector.value;
        console.log("Selected State:", selectedState);  // Kiểm tra giá trị
        districtSelector.innerHTML = '<option value="null">- Chọn Quận/Huyện -</option>'; // Reset quận/huyện
        storesContainer.innerHTML = ""; // Xóa cửa hàng

        if (selectedState === "null") {
            // Hiển thị tất cả cửa hàng nếu chọn null ở tỉnh/thành phố
            storeTitles.forEach((title) => {
                const storeContentId = title.getAttribute("id").replace("store_title", "store_content");
                const storeContent = document.getElementById(storeContentId);
    
                storesContainer.appendChild(title.closest(".-information"));
                title.classList.remove("show-info");
              
            });
            return;
        }

        // Lọc quận/huyện phù hợp
        if (selectedState === "001") { // TP Hồ Chí Minh
            districtSelector.innerHTML += `
                <option value="Quan7">Quận 7</option>
                <option value="CuChi">Củ Chi</option>
                <option value="BinhThanh">Bình Thạnh</option>
            `;
        } else if (selectedState === "027") { // Hà Nội
            districtSelector.innerHTML += `
                <option value="HaDong">Hà Đông</option>
                <option value="DongDa">Đống Đa</option>
                <option value="HoanKiem">Hoàn Kiếm</option>
            `;
        } else if (selectedState === "021") { // Đà Nẵng
            districtSelector.innerHTML += `
                <option value="HaiChau">Hải Châu</option>
                <option value="ThanhKhe">Thanh Khê</option>
                <option value="Đà Nẵng">Đà Nẵng</option>
            `;
        }

        // Hiển thị các cửa hàng của tỉnh/thành phố
        storeTitles.forEach((title) => {
            const storeContentId = title.getAttribute("id").replace("store_title", "store_content");
            const storeContent = document.getElementById(storeContentId);
            const storeState = title.closest('.-information').dataset.state; // Lấy giá trị data-state từ phần tử cha

            if (storeState === selectedState) {
                storesContainer.appendChild(title.closest(".-information"));
                title.classList.remove("show-info");
            }
        });
    });

    // Xử lý khi thay đổi Quận/Huyện
    districtSelector.addEventListener("change", () => {
        const selectedDistrict = districtSelector.value;
        console.log("Selected District:", selectedDistrict); // Kiểm tra giá trị quận/huyện đã chọn
        storesContainer.innerHTML = ""; // Xóa cửa hàng

        storeTitles.forEach((title) => {
            const storeContentId = title.getAttribute("id").replace("store_title", "store_content");
            const storeContent = document.getElementById(storeContentId);
            const storeDistrict = title.closest('.-information').dataset.district;  // Lấy giá trị data-district từ phần tử cha

            // Kiểm tra nếu quận/huyện đã chọn là "null", thì hiển thị tất cả cửa hàng
            // Hoặc nếu quận/huyện của cửa hàng trùng với giá trị đã chọn
            if ( storeDistrict === selectedDistrict) {
                storesContainer.appendChild(title.closest(".-information"));
                title.classList.remove("show-info");
                storeContent.style.display = "none";
            }
        });
    });
});
