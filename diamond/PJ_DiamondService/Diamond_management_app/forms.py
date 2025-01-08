from django import forms
from .models import diamond

class DiamondForm(forms.ModelForm):
    class Meta:
        model = diamond
        fields = ['DiaName', 'carat', 'shape', 'cut', 'color', 'clarity', 'DiamondPrice']
        widgets = {
            'shape': forms.Select(attrs={'class': 'form-control'}),
            'cut': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'clarity': forms.TextInput(attrs={'class': 'form-control'}),
            'DiaName': forms.TextInput(attrs={'class': 'form-control'}),
            'carat': forms.NumberInput(attrs={'class': 'form-control'}),
            'DiamondPrice': forms.NumberInput(attrs={'class': 'form-control'}),
        }
