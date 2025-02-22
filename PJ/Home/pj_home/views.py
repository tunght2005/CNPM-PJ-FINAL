from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
import uuid
from django.shortcuts import render, get_object_or_404, redirect

#product
from .models import Product, Cart, CartItem, Order, OrderDetail, Customer
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
    
#     # Kiểm tra giỏ hàng trong session
#     cart = request.session.get('cart', {})

#     # Nếu sản phẩm đã có trong giỏ, tăng số lượng
#     if str(product_id) in cart:
#         cart[str(product_id)]['quantity'] += 1
#     else:
#         cart[str(product_id)] = {
#             'name': product.name,
#             'price': product.price,
#             'quantity': 1,
#         }

#     # Lưu lại session
#     request.session['cart'] = cart
#     messages.success(request, f'Đã thêm {product.name} vào giỏ hàng!')
    
#     return redirect('cart_page')
# @csrf_exempt
# def cart_count(request):
#     if request.user.is_authenticated:
#         count = Cart.objects.filter(user=request.user).count()
#     else:
#         count = request.session.get('cart_count', 0)  # Lấy từ session nếu chưa đăng nhập
#     return JsonResponse({'cart_count': count})
# def buy_now(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
    
#     # Lấy giỏ hàng từ session
#     cart = request.session.get('cart', {})

#     # Thêm sản phẩm vào giỏ hàng (nếu chưa có)
#     if str(product_id) in cart:
#         cart[str(product_id)]['quantity'] += 1
#     else:
#         cart[str(product_id)] = {
#             'name': product.Pname,
#             'price': product.price,
#             'quantity': 1,
#         }

#     # Lưu giỏ hàng vào session
#     request.session['cart'] = cart
#     messages.success(request, f'Bạn đã thêm {product.Pname} vào giỏ hàng!')

#     # Chuyển hướng đến trang giỏ hàng
#     return redirect('cart_page')
def updateItem(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderDetail, created = OrderDetail.objects.get_or_create(order = order, product=product)

    if action == 'add':
        orderDetail.quantity = (orderDetail.quantity + 1)
    elif action == 'remove':
        orderDetail.quantity = (orderDetail.quantity - 1)

    orderDetail.save()

    if orderDetail.quantity <= 0:
        orderDetail.delete()
    return JsonResponse('Item was added', safe=False)
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
# Xoa san pham khoi gio hang
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
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    best_sellers = Product.objects.filter(sold_count__gt=0).order_by('-sold_count')[:10]  # Lấy 10 sản phẩm bán chạy nhất
    latest_products = Product.objects.all().order_by('-created_at')[:10]  # Lấy 10 sản phẩm mới nhất
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    diamond_products = Product.objects.filter(category='Kim Cuong').order_by('-created_at')[:10]
    day_products = Product.objects.filter(category='kim_cuong').order_by('-created_at')[:10]
    dongho_products = Product.objects.filter(category='dong_ho').order_by('-created_at')[:10]
    trangsuc_products = Product.objects.filter(category='trang_suc_cuoi').order_by('-created_at')[:10]
    return render(request, 'home/index.html', {'products': products,'top_products': top_products, 'best_sellers': best_sellers, 'latest_products': latest_products, 'diamond_products': diamond_products, 'day_products': day_products, 'dongho_products': dongho_products, 'trangsuc_products': trangsuc_products})
# Trang suc
def jewelry_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/jewelry.html', {'products': products, 'top_products': top_products})
# Dia chi
def address_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/address.html', {'products': products, 'top_products': top_products})
# Bao mat tt
def security_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/baomattt.html', {'products': products, 'top_products': top_products})
# Blog
def blog_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/blog.html', {'products': products, 'top_products': top_products})
# Buy bill
def buybill_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/buy-bill.html', {'products': products, 'top_products': top_products})
# Cam nang
def guide_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/cam_nang.html', {'products': products, 'top_products': top_products})
# Cart
def cart_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all() # Lấy tất cả sản phẩm trong đơn hàng
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order , 'cartItems': cartItems, 'products': products, 'top_products': top_products}
    return render(request, 'home/pages/cart.html', context)
# Cart finish
def cartfinish_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/cart-finish.html', {'products': products, 'top_products': top_products})
# Cau hoi thuong gap
def faq_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/Cau-Hoi-Thuong-Gap.html', {'products': products, 'top_products': top_products})
# Chinh sach bao hanh
def warranty_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/Chính-Sach-Bao-Hanh.html', {'products': products, 'top_products': top_products})
# Chinh sach giao hang
def delivery_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/chinhsachGH.html', {'products': products, 'top_products': top_products})
# Comments
def comments_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/comments.html', {'products': products, 'top_products': top_products})
# Customer
def customer_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/customer.html', {'products': products, 'top_products': top_products})
# Details
def details_page(request, product_id):
    product = get_object_or_404(Product, ProductID=product_id)
    # Lấy các sản phẩm tương tự (cùng danh mục, loại trừ sản phẩm hiện tại)
    if request.user.is_authenticated:
        ViewedProduct.objects.update_or_create(user=request.user, product=product)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all() # Lấy tất cả sản phẩm trong đơn hàng
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    # product = Product.objects.all() 
    related_products = Product.objects.filter(category=product.category).exclude(ProductID=product.ProductID)[:8]
    return render(request, 'home/pages/details.html', {'product': product, 'related_products': related_products, 'items': items, 'order': order , 'cartItems': cartItems})
# Diamond
def diamond_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/Diamond.html', {'products': products, 'top_products': top_products})
# Dong ho
def watch_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/Dong-Ho.html', {'products': products, 'top_products': top_products})
# Gift
def gift_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/gift.html', {'products': products, 'top_products': top_products})
# Huong dan do size
def size_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/huong_dan_do_size.html', {'products': products, 'top_products': top_products})
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
    return render(request, 'home/index.html', {'products': products,'top_products': top_products, 'best_sellers': best_sellers, 'latest_products': latest_products, 'diamond_products': diamond_products, 'day_products': day_products, 'dongho_products': dongho_products, 'trangsuc_products': trangsuc_products})
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
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/inspection.html',{'products': products, 'top_products': top_products})
# Manage order
def manageorder_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/manage-order.html', {'products': products, 'top_products': top_products})
# Notifi
def notification_list(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/notification.html', {'products': products, 'top_products': top_products})
# Product view
def productview_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/product-views.html', {'products': products, 'top_products': top_products})
# Review
def review_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/review.html', {'products': products, 'top_products': top_products})
# Wedding
def wedding_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/wedding.html', {'products': products, 'top_products': top_products})
# Wishlist
def wishlist_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/wishlist.html', {'products': products, 'top_products': top_products})
# Sales
def sales_page(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    top_products = Product.objects.order_by('-search_count')[:5]  # Lấy 5 sản phẩm tìm kiếm nhiều nhất
    return render(request, 'home/pages/sales.html',  {'products': products, 'top_products': top_products})
def login(request):
    return render(request, 'accounts/login.html')
# Create your views here.
# from django.http import JsonResponse
from django.conf import settings
# from django.shortcuts import render, get_object_or_404
# from django.views.decorators.csrf import csrf_exempt

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

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from django import forms
from .forms import UserProfileForm


User = get_user_model()

# API lấy và cập nhật thông tin user
@login_required
def profile_view(request):
    user = request.user  # Lấy thông tin user hiện tại
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('customer_page')  # Reload lại trang sau khi lưu
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'home/pages/customer.html', {'form': form, 'user': user})
# API đổi mật khẩu
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not check_password(old_password, user.password):
            return Response({"error": "Mật khẩu cũ không đúng"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)

        return Response({"message": "Đổi mật khẩu thành công"}, status=status.HTTP_200_OK)

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Order, Notification

def get_notifications(request):
    """Lấy danh sách đơn hàng mới chưa đọc"""
    orders = Order.objects.filter(is_read=False).order_by("-created_at")
    data = [
        {
            "order_id": order.OrderID,
            "status": order.get_status_display(),
            "created_at": order.created_at.strftime("%d/%m/%Y"),
            "total_amount": f"{order.total_amount} VNĐ",
            "image": order.orderdetail_set.first().product.image.url if order.orderdetail_set.exists() else None,
            "is_read": order.is_read,
            "order_details": [
                {
                    "product_name": detail.product.Pname,
                    "product_image": detail.product.image.url if detail.product.image else None,
                    "price": detail.price,
                }
                for detail in order.orderdetail_set.all()
            ]
        }
        for order in orders
    ]
    return JsonResponse({"orders": data})


@csrf_exempt
def mark_order_read(request, order_id):
    """Đánh dấu đơn hàng là đã đọc"""
    if request.method != "POST":
        return JsonResponse({"error": "Phương thức không hợp lệ"}, status=400)

    order = get_object_or_404(Order, OrderID=order_id)
    order.is_read = True
    order.save()
    return JsonResponse({"message": "Đánh dấu đã đọc thành công", "order_id": order.OrderID})

@csrf_exempt
def delete_order(request, order_id):
    """Xóa đơn hàng và thông báo liên quan"""
    if request.method == "DELETE":
        order = get_object_or_404(Order, OrderID=order_id)
        order.delete()

        # Xóa tất cả các thông báo liên quan đến đơn hàng
        Notification.objects.filter(order=order).delete()

        return JsonResponse({"message": "Đơn hàng đã được xóa thành công"})
    
    return JsonResponse({"error": "Phương thức không hợp lệ"}, status=400)

from .models import ViewedProduct
from django.shortcuts import render

# Xem sản phẩm gần đây
def viewed_products(request):
    if request.user.is_authenticated:
        viewed_products = ViewedProduct.objects.filter(user=request.user)[:10]  # Lấy tối đa 10 sản phẩm gần nhất
    else:
        viewed_products = []

    return render(request, 'home/pages/product-views.html', {'viewed_products': viewed_products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Nếu user đã đăng nhập, lưu sản phẩm vào danh sách đã xem
    if request.user.is_authenticated:
        ViewedProduct.objects.update_or_create(user=request.user, product=product)

    return render(request, 'home/pages/product-views.html', {'product': product})

from .models import Wishlist

@csrf_exempt
def wishlist_view(request):
    if not request.user.is_authenticated:
        return redirect("login")  # Nếu chưa đăng nhập, chuyển hướng đến trang đăng nhập
    
    wishlist_items = Wishlist.objects.filter(customer=request.user.customer)  # Lấy danh sách yêu thích của khách hàng
    return render(request, 'home/pages/wishlist.html', {'wishlist_items': wishlist_items})


# def toggle_wishlist(request, product_id):
#     wishlist = request.session.get("wishlist", [])

#     if product_id in wishlist:
#         wishlist.remove(product_id)
#         status = "removed"
#     else:
#         wishlist.append(product_id)
#         status = "added"

#     request.session["wishlist"] = wishlist
#     return JsonResponse({"status": status})

@csrf_exempt
def remove_from_wishlist(request, product_id):
    if not request.user.is_authenticated:
        return JsonResponse({"success": False, "message": "Bạn phải đăng nhập để thực hiện thao tác này."})

    try:
        wishlist_item = Wishlist.objects.get(customer=request.user.customer, product_id=product_id)
        wishlist_item.delete()
        return JsonResponse({"success": True})
    except Wishlist.DoesNotExist:
        return JsonResponse({"success": False, "message": "Sản phẩm không tồn tại trong danh sách yêu thích."})

def get_product(request, product_id):
    """API lấy thông tin sản phẩm theo ProductID"""
    try:
        product = get_object_or_404(Product, ProductID=product_id)
        data = {
            "ProductID": product.ProductID,
            "Pname": product.Pname,
            "descPr": product.descPr,
            "price": str(product.price),  # Convert Decimal to String
            "image": product.image.url if product.image else None
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Sản phẩm không tồn tại"}, status=404)


# @csrf_exempt  
# def create_order(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             print("📌 Dữ liệu nhận được:", data)  # Debug dữ liệu JSON

#             if "cart_items" not in data or not isinstance(data["cart_items"], list):
#                 return JsonResponse({"status": "error", "message": "Thiếu hoặc sai định dạng cart_items!"}, status=400)

#             for item in data["cart_items"]:
#                 print("📌 Item:", item)  # Debug từng sản phẩm

#                 product_id = item.get("product_id")
#                 quantity = item.get("quantity")
#                 price = item.get("price")

#                 if product_id is None or quantity is None or price is None:
#                     return JsonResponse({"status": "error", "message": f"Sản phẩm không hợp lệ: {item}"}, status=400)

#             return JsonResponse({"status": "success", "message": "Dữ liệu hợp lệ!"})

#         except json.JSONDecodeError:
#             return JsonResponse({"status": "error", "message": "Dữ liệu JSON không hợp lệ!"}, status=400)

@csrf_exempt
def create_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("📌 Dữ liệu nhận được:", data)  # Debug dữ liệu JSON

            customer_id = data.get("customer_id")  # 🔥 Lấy customer_id từ request
            if not customer_id:
                return JsonResponse({"status": "error", "message": "Thiếu customer_id!"}, status=400)

            try:
                customer = Customer.objects.get(CustomerID=customer_id)  # 🔍 Tìm khách hàng trong DB
            except Customer.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Khách hàng không tồn tại!"}, status=404)

            # Kiểm tra giỏ hàng
            cart_items = data.get("cart_items", [])
            if not cart_items:
                return JsonResponse({"status": "error", "message": "Giỏ hàng trống!"}, status=400)

            # Tạo đơn hàng mới
            order = Order.objects.create(
                customer=customer,
                total_amount=0,  # Tổng tiền sẽ cập nhật sau
                status="pending",
                guest=False  # Không phải khách vãng lai
            )

            total_amount = 0
            for item in cart_items:
                product_id = item.get("product_id")
                quantity = item.get("quantity")
                price = item.get("price")

                if not product_id or not quantity or not price:
                    return JsonResponse({"status": "error", "message": "Dữ liệu sản phẩm không hợp lệ!"}, status=400)

                product = Product.objects.get(pk=product_id)

                order_detail = OrderDetail.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=price
                )

                total_amount += order_detail.get_total

            # Cập nhật tổng tiền
            order.total_amount = total_amount
            order.save()

            return JsonResponse({"status": "success", "message": "Đơn hàng đã được tạo!", "order_id": order.OrderID})

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Dữ liệu JSON không hợp lệ!"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Lỗi hệ thống: {str(e)}"}, status=500)

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
@receiver(user_logged_in)
def ensure_customer_exists(sender, request, user, **kwargs):
    if not hasattr(user, 'customer'):  # Kiểm tra user đã có Customer chưa
        Customer.objects.create(user=user)
        print(f"✅ Tạo Customer mới cho {user.username}")


from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Order
from .serializers import OrderSerializer
@api_view(["GET"])
def get_orders(request):
    user = request.user
    print(f"🔍 User: {user}")  # Kiểm tra user

    if user.is_authenticated:
        orders = Order.objects.filter(customer=user).order_by("-created_at")
    else:
        orders = Order.objects.all()

    print(f"📦 Orders: {orders}")  # Kiểm tra danh sách đơn hàng

    serializer = OrderSerializer(orders, many=True)
    print(f"📝 Serialized Data: {serializer.data}")  # Kiểm tra dữ liệu trước khi trả về

    return Response({"orders": serializer.data})
