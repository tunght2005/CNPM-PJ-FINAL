from django.shortcuts import render, get_object_or_404, redirect
from .models import diamond
from django.http import HttpResponse, JsonResponse

# View hiển thị danh sách diamonds
def diamond_list(request):
    diamonds = diamond.objects.all()
    return render(request, 'table-data-info.html', {'diamonds': diamonds})

# View thêm mới diamond
def add_diamond(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        dia_name = request.POST['DiaName']
        carat = request.POST['carat']
        shape = request.POST['shape']
        cut = request.POST['cut']
        color = request.POST['color']
        clarity = request.POST['clarity']
        diamond_price = request.POST['DiamondPrice']
        
        # Xử lý ảnh tải lên nếu có
        image = request.FILES.get('image')
        
        # Tạo và lưu vào cơ sở dữ liệu
        diamond_obj = diamond(
            DiaName=dia_name,
            carat=carat,
            shape=shape,
            cut=cut,
            color=color,
            clarity=clarity,
            DiamondPrice=diamond_price,
            image=image
        )
        diamond_obj.save()
        
        return redirect('diamond_list')  # Quay lại danh sách diamonds
    
    return render(request, 'form-add-news.html')

# View chỉnh sửa diamond
def edit_diamond(request, diamond_id):
    diamond_obj = get_object_or_404(diamond, id=diamond_id)
    
    if request.method == 'POST':
        diamond_obj.DiaName = request.POST['DiaName']
        diamond_obj.carat = request.POST['carat']
        diamond_obj.shape = request.POST['shape']
        diamond_obj.cut = request.POST['cut']
        diamond_obj.color = request.POST['color']
        diamond_obj.clarity = request.POST['clarity']
        diamond_obj.DiamondPrice = request.POST['DiamondPrice']
        
        # Cập nhật ảnh nếu có
        if request.FILES.get('image'):
            diamond_obj.image = request.FILES['image']
        
        diamond_obj.save()
        
        return redirect('diamond_list')  # Quay lại danh sách diamonds
    
    return render(request, 'form-edit-news.html', {'diamond': diamond_obj})

def delete_diamond(request, diamond_id):
    if request.method == 'POST':
        # Lấy diamond cần xóa
        dia = get_object_or_404(diamond, id=diamond_id)
        dia.delete()  # Xóa diamond khỏi cơ sở dữ liệu
        return JsonResponse({'success': True})  # Trả về kết quả thành công
    return JsonResponse({'success': False})  # Trả về kết quả thất bại