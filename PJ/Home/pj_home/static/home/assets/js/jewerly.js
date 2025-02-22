const listImage = document.querySelector('.list-images')
const imgs= document.querySelectorAll('.list-images img')
const length = imgs.length
const width = imgs[0].offsetWidth
const btnLeft = document.querySelector('.btn-left')
const btnRight = document.querySelector('.btn-right')
let current = 0

const handleChangeSlide = () => {
    current++
    if (current >= length ){
        current = 0
       listImage.style.transition  = 'none'
       listImage.style.transform = `translateX(0)`
       document.querySelector('.active1').classList.remove('active1')
       document.querySelector('.index-item-' + current).classList.add('active1')
       setTimeout(() =>{
        listImage.style.transition  = 'transform 0.5s ease-in-out'
       },50)
    }else {
    listImage.style.transform = `translateX(${-width *current}px)`
    document.querySelector('.active1').classList.remove('active1')
    document.querySelector('.index-item-' + current).classList.add('active1')
    }
}
let handleEventChangeSlide = setInterval(handleChangeSlide,3000)

btnRight.addEventListener('click', () =>{
    clearInterval(handleEventChangeSlide)
    handleChangeSlide()
    handleEventChangeSlide = setInterval(handleChangeSlide,3000)
})

btnLeft.addEventListener('click', () =>{
    clearInterval(handleEventChangeSlide)
    current--
    if (current < 0){
        current = length -1
       listImage.style.transform = `translateX(${-width * current}px)`
       document.querySelector('.active1').classList.remove('active1')
       document.querySelector('.index-item-' + current).classList.add('active1')
       setTimeout(() =>{
        listImage.style.transition  = 'transform 0.5s ease-in-out'
       },50)
    }else {
    listImage.style.transform = `translateX(${-width *current}px)`
    document.querySelector('.active1').classList.remove('active1')
    document.querySelector('.index-item-' + current).classList.add('active1')
    }
    handleEventChangeSlide = setInterval(handleChangeSlide,3000)
})

const products = [
    {
      id: 1,
      category: "Nhẫn",
      material: "Bạc",
      commodityLine: "Trang Sức Không Đính Đá",
      fengShui: "Best Seller",
      name: "Nhẫn bạc mạ vàng",
      description: "Nhẫn Nam Moissanite Bạc Mạ Vàng MN34",
      price: "9.249.000đ",
      image: "https://trangsucdaquy.vn/wp-content/uploads/2022/11/Nhan-Nam-Moissanite-Bac-Ma-Vang-2.jpg"
    },
    {
      id: 2,
      category: "Nhẫn",
      material: "Bạc",
      commodityLine: "Trang Sức Không Đính Đá",
      fengShui: "Hàng Đặt Trước",
      name: "Nhẫn bạc",
      description: "Nhẫn Bạc 925 Bản Rộng Đính Mặt Trai Boho Pearl - VSR01",
      price: "10.200.000đ",
      image: "https://bizweb.dktcdn.net/100/461/213/products/vsr01-thong-so.png?v=1687596993253"
    },
    {
        id: 3,
      category: "Nhẫn",
      material: "Bạc",
      commodityLine: "Trang Sức Đính Kim Cương",
      fengShui: "Hàng Đặt Trước",
      name: "Nhẫn Bạc",
      description: "Nhẫn bạc nữ đính kim cương Moissanite bạc xi bạch kim 4 ly kiểm định GRA LAVESTA KC90",
      price: "6.000.000đ",
      image: "https://pos.nvncdn.com/211f76-106986/ps/20240304_aa3EXHJke8.jpeg"
    },
    {
        id: 4,
      category: "Nhẫn",
      material: "Vàng",
      commodityLine: "Trang Sức Không Đính Đá",
      fengShui: "Hàng Đặt Trước",
      name: "Nhẫn Vàng",
      description: "Nhẫn vàng 24K",
      price: "7.000.000đ",
      image: "https://cdn.pnj.io/images/detailed/177/sp-gn0000y001957-nhan-vang-24k-pnj-01.png"
    },
    {
        id: 5,
      category: "Nhẫn",
      material: "Vàng",
      commodityLine: "Trang Sức Không Đính Đá",
      fengShui: "Best Seller",
      name: "Nhẫn Vàng",
      description: "Nhẫn Vàng 24K PRIMA GOLD - Rosanna hoa hồng quyến rũ - Prima",
      price: "20.100.000đ",
      image: "https://prima.com.vn/wp-content/uploads/2023/04/111R3046_01.png"
    },
    { id: 6, 
        category: "Nhẫn",
        material: "Vàng",
      commodityLine: "Trang Sức Đính Kim Cương",
      fengShui: "Best Seller",
      name: "Nhẫn Vàng",
      description: "Nhẫn vàng nữ đẹp - NNU76",
      price: "3.000.000đ",
      image: "https://mdjluxury.vn/wp-content/uploads/2019/10/NNU76-1.jpg"
    },
    {
        id: 7,
      category: "Bông Tai",
      material: "Bạc",
      commodityLine: "Trang Sức Đính Kim Cương",
      fengShui: "Hàng Đặt Trước",
      name: "Bông Tai",
      description: "Bông tai bạc Ý S925 nữ mạ bạch kim đính đá CZ hình trái tim LILI_991582",
      price: "4.300.000đ",
      image: "https://lili.vn/wp-content/uploads/2021/12/Bong-tai-bac-Y-S925-nu-ma-bach-kim-dinh-da-CZ-hinh-trai-tim-LILI_991582_10-400x400.jpg"
    },
    {
        id: 8,
      category: "Bông Tai",
      material: "Bạc",
      commodityLine: "Trang Sức Đính Kim Cương",
      fengShui: "Trang Sức Theo Cung Và Mệnh",
      name: "Bông Tai",
      description: "Bông tai bạc nữ dạng nụ đính đá CZ cỏ 3 lá LILI_449342",
      price: "2.600.000đ",
      image: "https://lili.vn/wp-content/uploads/2021/12/Bong-tai-bac-nu-dang-nu-dinh-da-CZ-co-3-la-LILI_449342_1.jpg"
    },
    {
        id: 9,
      category: "Bông Tai",
      material: "Bạc",
      commodityLine: "Trang Sức Không Đính Đá",
      fengShui: "Best Seller",
      name: "Bông Tai",
      description: "Bông Tai Bạc Nữ S925 JENSY Nơ Dễ Thương 'BELLUS ARCUS' BTARM00183",
      price: "7.300.000đ",
      image: "https://product.hstatic.net/200000356839/product/btarm00183-07_11eb3304b6824e108f6803ea6c078a4e_master.png"
    },
    {
        id: 10,
      category: "Bông Tai",
      material: "Vàng",
      commodityLine: "Trang Sức Không Đính Đá",
      fengShui: "Trang Sức Theo Cung Và Mệnh",
      name: "Bông Tai",
      description: "Bông tai Vàng 18K đính đá ECZ",
      price: "8.700.000đ",
      image: "https://cdn.pnj.io/images/detailed/197/sp-gbxmxmy006681-bong-tai-vang-18k-dinh-da-ecz-pnj-1.png"
    },
    {
        id: 11,
      category: "Bông Tai",
      material: "Vàng",
      commodityLine: "Trang Sức Đính Kim Cương",
      fengShui: "Hàng Đặt Trước",
      name: "Bông Tai",
      description: "Bông Tai Vàng Vàng K10 Đính 1 Viên Kim Cương - ESTELLE Jewelry",
      price: "7.600.000đ",
      image: "https://estelle.vn/wp-content/uploads/2024/01/0212-2853-0018_1.jpg"
    },
    {
        id: 12,
      category: "Bông Tai",
      material: "Vàng",
      commodityLine: "Trang Sức Không Đá",
      fengShui: "Best Seller",
      name: "Bông Tai",
      description: "Bông Tai Vàng Vàng 610 - BB86",
      price: "5.800.000đ",
      image: "https://apj.vn/wp-content/uploads/2020/01/BB86.jpg"
    },
    {
        id: 13,
      category: "Vòng",
      material: "Vàng",
      commodityLine: "Trang Sức Không Đá ",
      fengShui: "Trang Sức Theo Cung Và Mệnh",
      name: "Vòng",
      description: "Lắc tay vàng 18k",
      price: "8.340.000đ",
      image: "https://cdn.pnj.io/images/detailed/159/gv0000c000153-vong-vang-18k-pnj-1.png"
    },
    {
        id: 14,
      category: "Vòng",
      material: "Vàng",
      commodityLine: "Trang Sức Không Đá",
      fengShui: "Best Seller",
      name: "Vòng",
      description: "Vòng Tay Vàng Vàng 610",
      price: "6.500.000đ",
      image: "https://apj.vn/wp-content/uploads/2022/04/MTV0074.jpg"
    },
    {
        id: 15,
      category: "Vòng",
      material: "Vàng",
      commodityLine: "Trang Sức Không Đính Đá",
      fengShui: "Trang Sức Theo Cung Và Mệnh",
      name: "Vòng",
      description: "Vòng ba khúc vàng ta 24k",
      price: "5.600.000đ",
      image: "https://lh3.googleusercontent.com/proxy/ZXGhpDL4QLKbZCuFccYPy82dEcofieQ2gHU7P4vvD1Ol-I9d-hI84oRFsAuvfO76VIddJrS6XSa1bbTn--Zk14HIgUEm45TkycpkdQxreADw2aQuHB9k8eOoYlG9d3m6brN0xPcHimtqX5cPd2qEgPA5uGFNabL5cmVKwA"
    },
    {
        id: 16,
      category: "Vòng",
      material: "Bạc",
      commodityLine: "Trang Sức Đính Kim Cương",
      fengShui: "Best Seller",
      name: "Vòng",
      description: "Vòng Pandora Timeless Bạc Đính Đá Trong Suốt",
      price: "6.100.000đ",
      image: "https://product.hstatic.net/200000103143/product/39e8_a8bf2991d54442629c5026ec656f79e5_87696a2d36e84efea06f4d206411d1a4_63f4cda970d24cc5b137c189dcb6f42f_master.jpg"
    },
    {
        id: 17,
      category: "Vòng",
      material: "Bạc",
      commodityLine: "Trang Sức Không Đính Đá ",
      fengShui: "Trang Sức Theo Cung Và Mệnh",
      name: "Vòng",
      description: "Vòng bạc hoa sen khắc thần chú Om mani padme hum và kinh Bát Nhã",
      price: "11.200.000đ",
      image: "https://trongnha.com/wp-content/uploads/2021/07/2-29.jpg"
    },
    {
        id: 18,
      category: "Vòng",
      material: "Bạc",
      commodityLine: "Trang Sức Không Đính Đá ",
      fengShui: "Hàng Đặt Trước",
      name: "Vòng",
      description: "Lắc Tay Bạc 925 Trơn Xoắn Twist - VCB03",
      price: "9.200.000đ",
      image: "https://bizweb.dktcdn.net/thumb/1024x1024/100/461/213/products/01-vcb03-thumb-compress.jpg?v=1687592190860"
    },
    {
        id: 19,
      category: "Lắc",
      material: "Vàng",
      commodityLine: "Trang Sức Không Đính Đá ",
      fengShui: "Hàng Đặt Trước",
      name: "Lắc",
      description: "Lắc tay vàng 18k",
      price: "4.300.000đ",
      image: "https://cdn.pnj.io/images/detailed/116/gl0000y001844-lac-tay-vang-18k-pnj-1.png"
    },
    {
        id: 20,
      category: "Lắc",
      material: "Vàng",
      commodityLine: "Trang Sức Không Đính Đá",
      fengShui: "Best Seller",
      name: "Lắc",
      description: "Lắc tay Vàng ta 990",
      price: "4.800.000đ",
      image: "https://ngoctham.com/wp-content/uploads/2022/12/lac-tay-vang-24k-CKDT31L-ntj-01-1-1-1800x2025.jpg"
    },
    {
        id: 21,
      category: "Lắc",
      material: "Vàng",
      commodityLine: "Trang Sức Không Đính Đá",
      fengShui: "Trang Sức Theo Cung Và Mệnh",
      name: "Lắc",
      description: "Lắc vàng 24K DOJI",
      price: "6.200.000đ",
      image: "https://product.hstatic.net/200000567741/product/blb0003610a1sy1_9a8c59e00ceb465192138ec62b187874_1024x1024.jpg"
    },
    {
        id: 22,
      category: "Lắc",
      material: "Bạc",
      commodityLine: "Trang Sức Không Đính Đá",
      fengShui: "Best Seller",
      name: "Lắc",
      description: "Lắc tay Bạc Ý",
      price: "5.200.000đ",
      image: "https://cdn.pnj.io/images/detailed/127/sl0000w000041-lac-tay-bac-y-pnjsilver-01.png"
    },
    {
        id: 23,
        category: "Lắc",
        material: "Bạc",
        commodityLine: "Trang Sức Không Đính Đá",
        fengShui: "Best Seller",
        name: "Lắc",
        description: "Lắc tay nữ bạc s925 Foliage nữ tính LT0121",
        price: "3.900.000đ",
        image: "https://tleejewelry.vn/wp-content/uploads/2022/06/Lac-tay-nu-TLEE-vong-tay-bac-Foliage-nu-tinh-LT0121-450x450.jpg"
    },
    {
        id: 24,
        category: "Lắc",
        material: "Bạc",
        commodityLine: "Trang Sức Không Đính Đá",
        fengShui: "Trang Sức Theo Cung Và Mệnh",
        name: "Lắc",
        description: "Lắc bạc cỏ 4 lá phong thủy may mắn",
        price: "4.200.000đ",
        image: "https://cdn.pnj.io/images/promo/220/ts-da-mau-t8-v1-1200x450_CTA.jpg"
    },
    {
        id: 25,
        category: "Dây Chuyền",
        material: "Vàng",
        commodityLine: "Trang Sức Không Đính Đá",
        fengShui: "Trang Sức Theo Cung Và Mệnh",
        name: "Dây Chuyền",
        description: "Dây chuyền Vàng 18K",
        price: "8.300.000đ",
        image: "https://ngoctham.com/wp-content/uploads/2023/01/day-chuyen-vang-18k-dvdrtvv0000p855-ntj-01-1-1800x2025.jpg"
    },
    {
        id: 26,
        category: "Dây Chuyền",
        material: "Vàng",
        commodityLine: "Trang Sức Không Đính Đá",
        fengShui: "Trang Sức Theo Cung Và Mệnh",
        name: "Dây Chuyền",
        description: "Dây Chuyền vàng hồng 18K ",
        price: "7.900.000đ",
        image: "https://locphuc.com.vn/Content/Images/Product/New%20Design%2007-2020/day-chuyen-cz-vang-hong-18k-VMP0963ANWRG-06-LP07200187-g1.jpg"
    },
    {
        id: 27,
        category: "Dây Chuyền",
        material: "Vàng",
        commodityLine: "Trang Sức Không Đính Đá",
        fengShui: "Best Seller",
        name: "Dây Chuyền",
        description: "Dây chuyền vàng 18k đính kim cương tự nhiên trái tim cỏ 4 lá ",
        price: "12.500.000đ",
        image: "https://lili.vn/wp-content/uploads/2021/12/Day-chuyen-vang-18k-co-bon-la-LILI_482417_11.jpg"
    },
    {
        id: 28,
        category: "Dây Chuyền",
        material: "Bạc",
        commodityLine: "Trang Sức Không Đính Đá",
        fengShui: "Trang Sức Theo Cung Và Mệnh",
        name: "Dây Chuyền",
        description: "Dây Chuyền Bạc Pandora ME Mắt Xích - Pandora Việt Nam ",
        price: "8.149.000đ",
        image: "https://product.hstatic.net/200000103143/product/392303c00_rgb_4141b4c368cd401ea1764bc753897288_38b6041a3370480182dec6980d617e1c_master.jpg"
    },
    {
        id: 29,
        category: "Dây Chuyền",
        material: "Bạc",
        commodityLine: "Trang Sức Không Đính Đá",
        fengShui: "Best Seller",
        name: "Dây Chuyền",
        description: "Dây Chuyền Bạc 925 Mặt Vuông Đính Đá Square Halo",
        price: "6.439.000đ",
        image: "https://bizweb.dktcdn.net/thumb/1024x1024/100/461/213/products/vun501-1687582909920.png?v=1700111068170"
    },
    {
        id: 30,
        category: "Dây Chuyền",
        material: "Bạc",
        commodityLine: "Trang Sức Không Đính Đá",
        fengShui: "Trang Sức Theo Cung Và Mệnh",
        name: "Dây Chuyền",
        description: "Dây Chuyền Bạc Many Love",
        price: "7.300.000đ",
        image: "https://glosbejewelry.net/index.php?t=ajax&p=tthumb&src=aHR0cHM6Ly9nbG9zYmVqZXdlbHJ5Lm5ldC91cGxvYWQvcHJvZHVjdC9kYXktbWFueV8zLmpwZw==&w=600;h=600"
    }
  ];
  function filterProducts(event) {
    event.preventDefault();
  
    // Lấy giá trị từ các ô lọc
    const category = document.getElementById("category").value;
    const material = document.getElementById("material").value;
    const commodityLine = document.getElementById("commodity-line").value;
    const fengShui = document.getElementById("feng-shui").value;
  
    // Lọc sản phẩm
    const filteredProducts = products.filter(product => {
      return (
        (category === "0" || product.category === category) &&
        (material === "0" || product.material === material) &&
        (commodityLine === "0" || product.commodityLine === commodityLine) &&
        (fengShui === "0" || product.fengShui === fengShui)
      );
    });
  
    // Hiển thị sản phẩm
    displayProducts(filteredProducts);
  }
  function displayProducts(productsToDisplay) {
    const productGrid = document.querySelector(".product-grid");
    productGrid.innerHTML = ""; // Xóa nội dung cũ
  
    if (productsToDisplay.length === 0) {
      productGrid.innerHTML = "<p>Không tìm thấy sản phẩm nào.</p>";
      return;
    }
  
    productsToDisplay.forEach(product => {
      const productHTML = `
        <div class="product">
          <img src="${product.image}" alt="${product.name}" style="width: 250px; height: 200px;">
          <h3>${product.name}</h3>
          <p>${product.description}</p>
          <p class="price">${product.price} VND</p>
        </div>
      `;
      productGrid.innerHTML += productHTML;
    });
  }

