from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages

#product
from .models import Product, Cart, CartItem
def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        messages.error(request, "Bạn cần đăng nhập để thêm sản phẩm vào giỏ hàng.")
        return redirect('login')

    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(customer=request.user)

    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.Pname} đã được thêm vào giỏ hàng.")
    return redirect('cart_page', ProductID=product_id)

# def add_to_cart(request):
#     if request.method == "POST":
#         import json
#         data = json.loads(request.body)
#         product_id = data.get("product_id")
        
#         product = Product.objects.get(ProductID=product_id)
        
#         # Lưu vào session nếu chưa đăng nhập
#         cart = request.session.get("cart", {})
#         cart[product_id] = cart.get(product_id, 0) + 1
#         request.session["cart"] = cart

#         return JsonResponse({"message": "Đã thêm vào giỏ hàng!", "cart_count": sum(cart.values())})
# def cart_count(request):
#     cart = request.session.get("cart", {})
#     return JsonResponse({"cart_count": sum(cart.values())})

#feedback
# Ham tinh luot tim kiem
def log_search(request):
    query = request.GET.get('q', '').strip()

    if not query:
        return JsonResponse({"message": "No query provided"}, status=400)

    # Tìm sản phẩm phù hợp
    product = Product.objects.filter(Pname__icontains=query).first()

    if product:
        product.search_count += 1
        product.save()
        return JsonResponse({"message": f"Search for '{query}' recorded", "search_count": product.search_count})

    return JsonResponse({"message": f"No product found for '{query}'"})
# Tim kiem san pham
def search_products(request):
    query = request.GET.get('q', '').strip()
    if query:
        products = Product.objects.filter(Pname__icontains=query)[:5]  # Giới hạn kết quả
        results = [
            {
                "ProductID": p.ProductID,
                "Pname": p.Pname,
                "price": str(p.price),
                "image_url": p.image.url,
                "search_count": p.search_count,
            }
            for p in products
        ]
        return JsonResponse({"results": results})
    return JsonResponse({"results": []})
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__customer=request.user)
    cart_item.delete()
    messages.success(request, "Sản phẩm đã bị xóa khỏi giỏ hàng.")
    return redirect('cart_page')
# # New product
# def new_products(request):
#     latest_products = Product.objects.all().order_by('-created_at')[:10]  # Lấy 10 sản phẩm mới nhất
#     return render(request, 'home/pages/index1.html', {'latest_products': latest_products})
# # Seller
# def best_selling_products(request):
#     best_sellers = Product.objects.filter(sold_count__gt=0).order_by('-sold_count')[:10]  # Lấy 10 sản phẩm bán chạy nhất
#     return render(request, 'home/pages/index1.html', {'best_sellers': best_sellers})
# Trang chu
def pj_home(request):
    return render(request, 'home/index.html')
# Trang suc
def jewelry_page(request):
    return render(request, 'home/pages/jewelry.html')
# Dia chi
def address_page(request):
    return render(request, 'home/pages/address.html')
# Bao mat tt
def security_page(request):
    return render(request, 'home/pages/baomattt.html')
# Blog
def blog_page(request):
    return render(request, 'home/pages/blog.html')
# Buy bill
def buybill_page(request):
    return render(request, 'home/pages/buy-bill.html')
# Cam nang
def guide_page(request):
    return render(request, 'home/pages/cam_nang.html')
# Cart
def cart_page(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    cart = Cart.objects.filter(customer=request.user).first()
    cart_items = cart.cart_items.all() if cart else []
    total_price = cart.total_price() if cart else 0
    return render(request, 'home/pages/cart.html', {'cart_items': cart_items, 'total_price': total_price})
# Cart finish
def cartfinish_page(request):
    return render(request, 'home/pages/cart-finish.html')
# Cau hoi thuong gap
def faq_page(request):
    return render(request, 'home/pages/Cau-Hoi-Thuong-Gap.html')
# Chinh sach bao hanh
def warranty_page(request):
    return render(request, 'home/pages/Chính-Sach-Bao-Hanh.html')
# Chinh sach giao hang
def delivery_page(request):
    return render(request, 'home/pages/chinhsachGH.html')
# Comments
def comments_page(request):
    return render(request, 'home/pages/comments.html')
# Customer
def customer_page(request):
    return render(request, 'home/pages/customer.html')
# Details
def details_page(request, product_id):
    product = get_object_or_404(Product, ProductID=product_id)
    # Lấy các sản phẩm tương tự (cùng danh mục, loại trừ sản phẩm hiện tại)
    related_products = Product.objects.filter(category=product.category).exclude(ProductID=product.ProductID)[:8]
    return render(request, 'home/pages/details.html', {'product': product, 'related_products': related_products})
# Diamond
def diamond_page(request):
    return render(request, 'home/pages/Diamond.html')
# Dong ho
def watch_page(request):
    return render(request, 'home/pages/Dong-Ho.html')
# Gift
def gift_page(request):
    return render(request, 'home/pages/gift.html')
# Huong dan do size
def size_page(request):
    return render(request, 'home/pages/huong_dan_do_size.html')
# Home - chua login
def home_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    best_sellers = Product.objects.filter(sold_count__gt=0).order_by('-sold_count')[:10]  # Lấy 10 sản phẩm bán chạy nhất
    latest_products = Product.objects.all().order_by('-created_at')[:10]  # Lấy 10 sản phẩm mới nhất
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    diamond_products = Product.objects.filter(category='Kim Cuong').order_by('-created_at')[:10]
    day_products = Product.objects.filter(category='kim_cuong').order_by('-created_at')[:10]
    dongho_products = Product.objects.filter(category='dong_ho').order_by('-created_at')[:10]
    trangsuc_products = Product.objects.filter(category='trang_suc_cuoi').order_by('-created_at')[:10]
    return render(request, 'home/pages/index1.html', {'products': products,'top_products': top_products, 'best_sellers': best_sellers, 'latest_products': latest_products, 'diamond_products': diamond_products, 'day_products': day_products, 'dongho_products': dongho_products, 'trangsuc_products': trangsuc_products})
# Home - da login
def home_page1(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database\
    best_sellers = Product.objects.filter(sold_count__gt=0).order_by('-sold_count')[:10]  # Lấy 10 sản phẩm bán chạy nhất
    latest_products = Product.objects.all().order_by('-created_at')[:10]  # Lấy 10 sản phẩm mới nhất
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    diamond_products = Product.objects.filter(category='kim_cuong').order_by('-created_at')[:10]
    day_products = Product.objects.filter(category='day_chuyen').order_by('-created_at')[:10]
    dongho_products = Product.objects.filter(category='dong_ho').order_by('-created_at')[:10]
    trangsuc_products = Product.objects.filter(category='trang_suc_cuoi').order_by('-created_at')[:10]
    return render(request, 'home/pages/index1.html', {'products': products,'top_products': top_products, 'best_sellers': best_sellers, 'latest_products': latest_products, 'diamond_products': diamond_products, 'day_products': day_products, 'dongho_products': dongho_products, 'trangsuc_products': trangsuc_products})
# Inspection
def inspection_page(request):
    return render(request, 'home/pages/inspection.html')
# Manage order
def manageorder_page(request):
    return render(request, 'home/pages/manage-order.html')
# Notifi
def notification_list(request):
    return render(request, 'home/pages/notification.html')
# Product view
def productview_page(request):
    return render(request, 'home/pages/product-views.html')
# Review
def review_page(request):
    return render(request, 'home/pages/review.html')
# Wedding
def wedding_page(request):
    return render(request, 'home/pages/wedding.html')
# Wishlist
def wishlist_page(request):
    return render(request, 'home/pages/wishlist.html')
# Sales
def sales_page(request):
    return render(request, 'home/pages/sales.html')

# Create your views here.
# from django.http import JsonResponse
# from django.conf import settings
# from django.shortcuts import render, get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
# from .models import Notification

# def notification_list(request):
#     notifications = Notification.objects.all()
#     return render(request, 'home/notifi.html', {'notifications': notifications, 'MEDIA_URL': settings.MEDIA_URL})

# @csrf_exempt
# def mark_as_read(request, notification_id):
#     """API: Đánh dấu thông báo là đã đọc"""
#     if request.method == "POST":
#         notification = get_object_or_404(Notification, id=notification_id)
#         notification.is_read = True
#         notification.save()
#         return JsonResponse({"success": True, "is_read": notification.is_read})
#     return JsonResponse({"success": False, "error": "Phương thức không hợp lệ"})

# @csrf_exempt
# def delete_notification(request, notification_id):
#     """ Xóa thông báo khỏi database """
#     if request.method == "DELETE":
#         try:
#             notification = get_object_or_404(Notification, id=notification_id)
#             notification.delete()
#             return JsonResponse({"success": True})
#         except Notification.DoesNotExist:
#             return JsonResponse({"success": False, "error": "Không tìm thấy thông báo."})