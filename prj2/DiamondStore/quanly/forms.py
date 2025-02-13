from django import forms
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['ProductID','name', 'description', 'carat_weight', 'origin', 
                 'clarity', 'category', 'cut', 'price', 'stock', 'image']
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # Thêm các choices cho category
        # self.fields['category'].widget = forms.Select(choices=[
        #     ('', '-- Chọn danh mục --'),
        #     ('necklace', 'Dây chuyền'),
        #     ('ring', 'Nhẫn'),
        #     ('bracelet', 'Vòng Tay'),
        # ])
        # Thêm các attribues cho fields
        # self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tên sản phẩm'})
        # self.fields['price'].widget.attrs.update({'class': 'form-control', 'id': 'sellingPrice', 'readonly': True})
    def save(self, commit=True):
        product = super().save(commit=False)
        product.save()
        return product