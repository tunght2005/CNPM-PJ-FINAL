from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.utils.timezone import now
import bcrypt
import re

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

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

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        # Kiểm tra độ dài tối thiểu
        if len(password1) < 8:
            raise ValidationError("Mật khẩu phải có ít nhất 8 ký tự")
        
        # Kiểm tra có ít nhất 1 chữ hoa
        if not any(c.isupper() for c in password1):
            raise ValidationError("Mật khẩu phải chứa ít nhất 1 chữ cái viết hoa")
        
        # Kiểm tra có ít nhất 1 số
        if not any(c.isdigit() for c in password1):
            raise ValidationError("Mật khẩu phải chứa ít nhất 1 chữ số")
        
        # Kiểm tra có ít nhất 1 ký tự đặc biệt
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if not any(c in special_chars for c in password1):
            raise ValidationError("Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt")
        
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Mật khẩu không khớp")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = bcrypt.hashpw(self.cleaned_data['password1'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user.role = 3  
        user.create_at = now()
        user.update_at = now()
        if commit:
            user.save()
        return user
