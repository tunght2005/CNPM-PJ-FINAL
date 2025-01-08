from django import forms
from .models import Users
from django.core.exceptions import ValidationError

import bcrypt

class RegistrationForm(forms.ModelForm):
    # name = forms.CharField(label='name', max_length=50)
    # email = forms.EmailField(label='email', max_length=50)
    # password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='password2', widget=forms.PasswordInput) 

    class Meta:
        model = Users
        fields = ['username', 'email', 'userphone']

    def clean_EMAIL(self):
        email = self.cleaned_data.get('EMAIL')
        if Users.objects.filter(EMAIL=email).exists():
            raise ValidationError("An account with this email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password1']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user.PASSWORD = hashed_password.decode('utf-8')
        user.ROLE = 3  # Default role as Customer
        if commit:
            user.save()
        return user