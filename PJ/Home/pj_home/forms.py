from django import forms
from .models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'full_name', 'nickname', 'birth_date', 'gender', 'nationality', 'phone', 'email']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
