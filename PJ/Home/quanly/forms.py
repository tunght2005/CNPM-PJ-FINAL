from django import forms
from pj_home.models import Product
from pj_home.models import User

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Pname', 'descPr', 'carat_weight', 'origin', 
                 'clarity', 'category', 'cut', 'price', 'stock', 'image']
        widgets = {
            'Pname': forms.TextInput(attrs={'class': 'form-control'}),
            'descPr': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('necklace', 'Dây chuyền'),
                ('ring', 'Nhẫn'),
                ('bracelet', 'Vòng Tay'),
            ]),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'carat_weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'origin': forms.TextInput(attrs={'class': 'form-control'}),
            'clarity': forms.TextInput(attrs={'class': 'form-control'}),
            'cut': forms.TextInput(attrs={'class': 'form-control'}),
        }    
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
    def clean_ProductID(self):
        ProductID = self.cleaned_data.get('ProductID')
        if Product.objects.filter(ProductID=ProductID).exists():
            raise forms.ValidationError("Mã sản phẩm đã tồn tại")
        return ProductID
    def save(self, commit=True):
        product = super().save(commit=False)
        product.save()
        return product
    
class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}, choices=[
                (2, 'Sales'),
                (3, 'Staff'),
                (4, 'Delivery'),
            ]),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email này đã được sử dụng")
        return email
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password('123456')
        user.save()
        return user


class AddEmployeeForm(forms.ModelForm):
    ROLE_CHOICES = [
        (2, 'Nhân viên bán hàng'),
        (3, 'Quản lý'),
        (4, 'Nhân viên giao hàng'),
    ]
    
    GENDER_CHOICES = [
        ('M', 'Nam'),
        ('F', 'Nữ'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['email', 'username', 'phone', 'address', 'birth_date', 'gender', 'role']