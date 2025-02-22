# from django.urls import path
# from .views import notification_list, mark_as_read, delete_notification
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('', notification_list, name='notifications'),  
#     path('mark-as-read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
#     path('delete-notification/<int:notification_id>/', delete_notification, name='delete_notification'),
# ]

# # Chỉ sử dụng khi chạy server local (development mode)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# Tim kiem log_search
from .views import log_search
#seller
# from .views import best_selling_products
#new product
# from .views import new_products
from .views import search_products
# from .views import add_to_cart
# from .views import cart_count
from .views import ChangePasswordView
from .views import viewed_products
urlpatterns = [
    # path('', notification_list, name='notifications'),  
    # path('mark-as-read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
    # path('delete-notification/<int:notification_id>/', delete_notification, name='delete_notification'),
    path('cart/', views.cart_page, name='cart_page'),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    path('update_item/', views.updateItem, name='update_item'),
    # path('buy-now/<int:product_id>/', views.buy_now, name='buy_now'),
    # path('cart-count/', cart_count, name='cart_count'),
    # path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('search/', search_products, name='search_products'),
    # path('san-pham-moi/', new_products, name='new_products'),
    # path('best-selling-products/', best_selling_products, name='best_selling_products'),
    path('log-search/', log_search, name='log_search'),
    path('', views.pj_home, name='pj_home'),
    #Trang Suc
    path('jewelry/', views.jewelry_page, name='jewelry_page'),
    # Dia chi
    path('address/', views.address_page, name='address_page'),
    #Bao mat tt
    path('security/', views.security_page, name='security_page'),
    #Blog
    path('blog/', views.blog_page, name = 'blog_page'),
    #buy bill
    path('buybill/', views.buybill_page, name = 'buybill_page'),
    #cam nang
    path('guide/', views.guide_page, name = 'guide_page'),
    #cart
    path('cart/', views.cart_page, name ='cart_page'),
    #cart finish
    path('cartfinish/', views.cartfinish_page, name ='cartfinish_page'),
    #cau hoi thuong gap
    path('faq/', views.faq_page, name ='faq_page'),
    #chinh sach bao hanh
    path('warranty/', views.warranty_page, name ='warranty_page'),
    #Chinh sach giao hang
    path('delivery/', views.delivery_page, name ='delivery_page'),
    #comments
    path('comments/', views.comments_page, name ='comments_page'),
    #customer
    path('customer/', views.customer_page, name ='customer_page'),
    #details
    path('details/<str:product_id>/', views.details_page, name='details_page'),
    #Diamond
    path('diamond/', views.diamond_page, name ='diamond_page'),
    #Dong Ho
    path('watch/', views.watch_page, name ='watch_page'),
    #gift
    path('gift/', views.gift_page, name ='gift_page'),
    #Huong dan do size
    path('size/', views.size_page, name ='size_page'),
    #Home - chua login
    path('home/', views.home_page, name ='home_page'),
    #Home - da login
    path('home1/', views.home_page1, name ='home_page1'),
    #Inspection
    path('inspection/', views.inspection_page, name ='inspection_page'),
    #manage order
    path('manageorder/', views.manageorder_page, name ='manageorder_page'),
    #Notifi
    path('notification/', views.notification_list, name='notification_list'),
    # path('mark-as-read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
    # path('delete-notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    #product view
    path('productview/', views.productview_page, name ='productview_page'),
    #review
    path('review/', views.review_page, name ='review_page'),
    #wedding
    path('wedding/', views.wedding_page, name ='wedding_page'),
    #wishlist
    path('wishlist/', views.wishlist_page, name ='wishlist_page'),
    #sales
    path('sales/', views.sales_page, name ='sales_page'),
    path("api/orders/<str:order_id>/mark-read/", views.mark_order_read, name="mark_order_read"),
    path("api/orders/<str:order_id>/delete/", views.delete_order, name="delete_order"),
    path("api/order_notifi/", views.get_notifications, name="get_notifications"),
    path('viewed-products/', viewed_products, name='viewed_products'),
    # path("wishlist/toggle/<str:product_id>/", views.toggle_wishlist, name="toggle_wishlist"),
    path("api/get-product/<str:product_id>/", views.get_product, name="get_product"),
    path("api/create-order/", views.create_order, name="create_order"),
    path("api/orders/", views.get_orders, name="get_orders"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)