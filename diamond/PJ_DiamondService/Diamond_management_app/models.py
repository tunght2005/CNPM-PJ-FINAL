from django.db import models

# Create your models here.
class diamond(models.Model):
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


    DiaName = models.CharField(max_length=100)
    carat = models.FloatField()
    shape = models.CharField(max_length=20, choices=SHAPE_CHOICES)
    cut = models.CharField(max_length=100, choices=[('Bad', 'Bad'), ('Good', 'Good'), ('Very Good', 'Very Good'), ('Excellent', 'Excellent')])
    color = models.CharField(max_length=100)
    clarity = models.CharField(max_length=100)
    DiamondPrice = models.FloatField()
    UpdatedDate = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='diamonds/', null=True, blank=True)
