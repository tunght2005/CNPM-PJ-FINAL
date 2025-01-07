from django.shortcuts import render
from .models import Customer, Order, Shipping


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'oder_service_mng/customer_list.html', {'customers': customers})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'oder_service_mng/order_list.html', {'orders': orders})


def shipping_list(request):
    shippings = Shipping.objects.all()
    return render(request, 'oder_service_mng/shipping_list.html', {'shippings': shippings})

def home(request):
    return render(request, 'oder_service_mng/home.html')

