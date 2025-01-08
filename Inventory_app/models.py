from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    CUT_CHOICES = [
        ('Heart', 'Heart'),
        ('Round', 'Round'),
        ('Oval', 'Oval'),
        ('Princess', 'Princess'),
        ('Marquise', 'Marquise'),
        ('Radiant', 'Radiant'),
        ('Emerald', 'Emerald'),
    ]

    ProductName = models.CharField(max_length=255)
    DescProduct = models.TextField(blank=True, null=True)
    Carat_weight = models.FloatField()
    Origin = models.CharField(max_length=50)
    Clarity = models.FloatField()
    Category = models.CharField(max_length=100)
    Cut = models.CharField(max_length=50, choices=CUT_CHOICES)
    Price = models.FloatField()
    Stock = models.PositiveIntegerField()
    ImagePro = models.CharField(max_length=255, blank=True, null=True)
    Color = models.CharField(max_length=50, blank=True, null=True)
    Price_shell = models.FloatField()
    Create_at = models.DateTimeField(auto_now_add=True)
    Update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100)
    # Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.ProductName

class Desci(models.Model):
    CategoryDesc = models.CharField(max_length=100)
    NameDesc = models.CharField(max_length=255)
    Image = models.CharField(max_length=255, blank=True, null=True)
    Content = models.TextField()

    def __str__(self):
        return self.NameDesc