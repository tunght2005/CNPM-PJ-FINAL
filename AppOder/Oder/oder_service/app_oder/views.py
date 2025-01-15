from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse , JsonResponse
from.models import Order, Customer, Product, OrderItem
from.forms import OrderForm

def form_add_don_hang(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data['customer_name']
            customer_phone = form.cleaned_data['customer_phone']
            customer_address = form.cleaned_data['customer_address']
            seller_name = form.cleaned_data['seller_name']
            seller_id = form.cleaned_data['seller_id']
            order_date = form.cleaned_data['order_date']
            product_name = form.cleaned_data['product_name']
            product_code = form.cleaned_data['product_code']
            quantity = form.cleaned_data['quantity']
            status = form.cleaned_data['status']
            note = form.cleaned_data['note']

            # Tạo hoặc lấy thông tin khách hàng
            customer, created = Customer.objects.get_or_create(
                first_name=customer_name.split()[0],
                last_name=' '.join(customer_name.split()[1:]),
                defaults={'phone_number': customer_phone, 'address': customer_address}
            )

            # Tạo hoặc lấy thông tin sản phẩm
            product, created = Product.objects.get_or_create(
                name=product_name,
                defaults={'description': '', 'price': 0, 'stock': 0}
            )

            # Tạo đơn hàng
            order = Order.objects.create(
                customer=customer,
                status=status,
                total_amount=0  # Bạn có thể tính toán tổng số tiền dựa trên sản phẩm và số lượng
            )

            # Tạo chi tiết đơn hàng
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price  # Bạn có thể lấy giá từ sản phẩm
            )

            return redirect('table_data_oder')
    else:
        form = OrderForm()
    return render(request, 'app_oder/form_add_don_hang.html', {'form': form})

def table_data_oder(request):
    orders = Order.objects.all()
    return render(request, 'app_oder/table_data_oder.html', {'orders': orders})

def delete_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        order.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order.customer_name = form.cleaned_data['customer_name']
            order.customer_phone = form.cleaned_data['customer_phone']
            order.customer_address = form.cleaned_data['customer_address']
            order.seller_name = form.cleaned_data['seller_name']
            order.seller_id = form.cleaned_data['seller_id']
            order.order_date = form.cleaned_data['order_date']
            order.product_name = form.cleaned_data['product_name']
            order.product_code = form.cleaned_data['product_code']
            order.quantity = form.cleaned_data['quantity']
            order.status = form.cleaned_data['status']
            order.note = form.cleaned_data['note']
            order.save()
            return redirect('table_data_oder')
    else:
        initial_data = {
            'customer_name': order.customer_name,
            'customer_phone': order.customer_phone,
            'customer_address': order.customer_address,
            'seller_name': order.seller_name,
            'seller_id': order.seller_id,
            'order_date': order.order_date,
            'product_name': order.product_name,
            'product_code': order.product_code,
            'quantity': order.quantity,
            'status': order.status,
            'note': order.note,
        }
        form = OrderForm(initial=initial_data)
    return render(request, 'app_oder/form_add_don_hang.html', {'form': form})