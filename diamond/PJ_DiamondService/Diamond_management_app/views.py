from django.shortcuts import render, get_object_or_404, redirect
from .forms import diamondform
from .models import diamond
from datetime import datetime
from django.http import HttpResponse, JsonResponse

def diamond_list(request):
    diamonds = diamond.objects.all()
    return render(request, 'Diamond_management_app/table-data-info.html', {'diamonds': diamonds})

def add_diamond(request):
    if request.method == 'POST':
        form = diamondform(request.POST, request.FILES)
        if form.is_valid():
            DiaName = form.cleaned_data['DiaName']
            carat = form.cleaned_data['carat']
            shape = form.cleaned_data['shape']
            cut = form.cleaned_data['cut']
            color = form.cleaned_data['color']
            clarity = form.cleaned_data['clarity']
            DiamondPrice = form.cleaned_data['DiamondPrice']
            image = form.cleaned_data.get('image')

            diamond.objects.create(
                DiaName=DiaName,
                carat=carat,
                shape=shape,
                cut=cut,
                color=color,
                clarity=clarity,
                DiamondPrice=DiamondPrice,
                image=image
            )
            return redirect('diamond_list')
    else:
        form = diamondform()
    
    return render(request, 'Diamond_management_app/form-add-news.html', {'form': form})


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
        
        return redirect('diamond_list')
    
    return render(request, 'Diamond_management_app/form-add-news.html')

def delete_diamond(request, diamond_id):
    obj = get_object_or_404(diamond, id=diamond_id)
    
    if request.method == 'POST':
        obj.delete()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})

