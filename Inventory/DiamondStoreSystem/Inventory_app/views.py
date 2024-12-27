from django.shortcuts import render, redirect
from .models import Diamond, Transaction , Product
from .forms import ProductForm

# Trang chính
def home(request):
    return render(request, 'home.html')

# Hiển thị danh sách tồn kho
def inventory_list(request):
    diamonds = Diamond.objects.all()
    return render(request, 'inventory_list.html', {'diamonds': diamonds})

# Thêm sản phẩm vào tồn kho
def add_inventory(request):
    if request.method == 'POST':
        name = request.POST['name']
        carat = request.POST['carat']
        cut = request.POST['cut']
        color = request.POST['color']
        clarity = request.POST['clarity']
        price = request.POST['price']
        quantity = request.POST['quantity']
        Diamond.objects.create(name=name, carat=carat, cut=cut, color=color, clarity=clarity, price=price, quantity=quantity)
        return redirect('inventory_list')
    return render(request, 'inventory/add_inventory.html')

# Hiển thị danh sách giao dịch
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'inventory/transaction_list.html', {'transactions': transactions})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Xử lý dữ liệu từ form
        if form.is_valid():
            form.save()  # Lưu sản phẩm vào cơ sở dữ liệu
            return redirect('inventory:product_list')  # Chuyển hướng đến trang danh sách sản phẩm sau khi thêm thành công
    else:
        form = ProductForm()  # Form trống khi GET request

    return render(request, 'inventory/add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ cơ sở dữ liệu
    return render(request, 'inventory/product_list.html', {'products': products})