from django import forms

class diamondform(forms.Form):
    SHAPE_CHOICES = [
        ('Round', 'Round'),
        ('Princess', 'Princess'),
        ('Oval', 'Oval'),
        ('Emerald', 'Emerald'),
        ('Cushion', 'Cushion'),
        ('Marquise', 'Marquise'),
        ('Pear', 'Pear'),
        ('Asscher', 'Asscher'),
        ('Radiant', 'Radiant'),
        ('Heart', 'Heart'),
    ]

    CUT_CHOICES = [
        ('Bad', 'Bad'),
        ('Good', 'Good'),
        ('Very Good', 'Very Good'),
        ('Excellent', 'Excellent'),
    ]

    DiaName = forms.CharField(
        label='Tên kim cương',
        max_length=100,
    )
    carat = forms.FloatField(
        label='Carat',
    )
    shape = forms.ChoiceField(
        label='Hình dạng',
        choices=SHAPE_CHOICES,
    )
    cut = forms.ChoiceField(
        label='Cắt',
        choices=CUT_CHOICES,
    )
    color = forms.CharField(
        label='Màu',
        max_length=100,
    )
    clarity = forms.CharField(
        label='Độ trong suốt',
        max_length=100,
    )
    DiamondPrice = forms.IntegerField(
        label='Giá',
    )
    image = forms.ImageField(
        label='Hình ảnh',
        required=False,
    )
