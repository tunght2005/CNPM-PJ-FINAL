from django.shortcuts import render, get_object_or_404, redirect
from .models import diamond
from django.http import HttpResponse, JsonResponse


def diamond_list(request):
    diamonds = diamond.objects.all()
    return render(request, 'table-data-info.html', {'diamonds': diamonds})


def add_diamond(request):
    if request.method == 'POST':
       
        dia_name = request.POST['DiaName']
        carat = request.POST['carat']
        shape = request.POST['shape']
        cut = request.POST['cut']
        color = request.POST['color']
        clarity = request.POST['clarity']
        diamond_price = request.POST['DiamondPrice']
        
      
        image = request.FILES.get('image')
        
        
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


def delete_diamond(request, diamond_id):
    if request.method == 'POST':
        # Lấy diamond cần xóa
        dia = get_object_or_404(diamond, id=diamond_id)
        dia.delete()  # Xóa diamond khỏi cơ sở dữ liệu
        return JsonResponse({'success': True})  # Trả về kết quả thành công
    return JsonResponse({'success': False})  # Trả về kết quả thất bại
