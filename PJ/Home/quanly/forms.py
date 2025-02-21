from django import forms
from pj_home.models import Product
from pj_home.models import User
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import re
from django.utils.timezone import now
import bcrypt

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Pname', 'stock', 'category', 'carat_weight', 'origin', 
                 'clarity', 'cut', 'color', 'price', 'price_sale', 'image', 'descPr']
        
    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        price_sale = cleaned_data.get('price_sale')
        
        if price and price_sale and price_sale > price:
            raise forms.ValidationError("Giá khuyến mãi không thể cao hơn giá gốc")
        
        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price <= 0:
            raise forms.ValidationError("Giá phải lớn hơn 0")
        return price

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock and stock < 0:
            raise forms.ValidationError("Số lượng không thể âm")
        return stock

    def clean_ProductID(self):
        ProductID = self.cleaned_data.get('ProductID')
        if Product.objects.filter(ProductID=ProductID).exists():
            raise forms.ValidationError("Mã sản phẩm đã tồn tại")
        return ProductID
    def save(self, commit=True):
        product = super().save(commit=False)
        product.save()
        return product
    
# class AddEmployeeForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'phone', 'role']

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("Email này đã được sử dụng")
#         return email
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password('123456')
#         user.save()
#         return user


class AddEmployeeForm(forms.ModelForm):   
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'username', 'password','phone','role', 'address']
    
    # def clean_role(self):
    #     role = self.cleaned_data.get('role')
    #     if role not in [3, 4, 5, 6]:
    #         raise ValidationError("Vui lòng chọn chức vụ hợp lệ")
    #     return role
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Kiểm tra định dạng email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise ValidationError("Email không hợp lệ")
        
        # Kiểm tra email đã tồn tại
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email này đã được sử dụng")
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Kiểm tra độ dài tối thiểu
        if len(password) < 8:
            raise ValidationError("Mật khẩu phải có ít nhất 8 ký tự")
        
        # Kiểm tra có ít nhất 1 chữ hoa
        if not any(c.isupper() for c in password):
            raise ValidationError("Mật khẩu phải chứa ít nhất 1 chữ cái viết hoa")
        
        # Kiểm tra có ít nhất 1 số
        if not any(c.isdigit() for c in password):
            raise ValidationError("Mật khẩu phải chứa ít nhất 1 chữ số")
        
        # Kiểm tra có ít nhất 1 ký tự đặc biệt
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if not any(c in special_chars for c in password):
            raise ValidationError("Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt")
        
        return password
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = bcrypt.hashpw(self.cleaned_data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user.create_at = now()
        user.update_at = now()
        if commit:
            user.save()
        return user
    
class AddCustomerForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'username', 'phone', 'password', 'address']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Kiểm tra định dạng email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise ValidationError("Email không hợp lệ")
        
        # Kiểm tra email đã tồn tại
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email này đã được sử dụng")
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Kiểm tra độ dài tối thiểu
        if len(password) < 8:
            raise ValidationError("Mật khẩu phải có ít nhất 8 ký tự")
        
        # Kiểm tra có ít nhất 1 chữ hoa
        if not any(c.isupper() for c in password):
            raise ValidationError("Mật khẩu phải chứa ít nhất 1 chữ cái viết hoa")
        
        # Kiểm tra có ít nhất 1 số
        if not any(c.isdigit() for c in password):
            raise ValidationError("Mật khẩu phải chứa ít nhất 1 chữ số")
        
        # Kiểm tra có ít nhất 1 ký tự đặc biệt
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if not any(c in special_chars for c in password):
            raise ValidationError("Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt")
        
        return password
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = bcrypt.hashpw(self.cleaned_data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user.role = 2 #customer
        user.create_at = now()
        user.update_at = now()
        if commit:
            user.save()
        return user