from django.test import TestCase ,Client
from .models import Product, Supplier, Category
from django.urls import reverse
class ProductModelTest(TestCase):
    def setUp(self):
        # Tạo dữ liệu test
        self.category = Category.objects.create(name="Test Category")
        self.supplier = Supplier.objects.create(name="Test Supplier")
        self.product = Product.objects.create(
            name="Test Product",
            category=self.category,
            supplier=self.supplier,
            price=1000,
            stock=50,
            quantity = 10
        )

    def test_product_creation(self):
        """Kiểm tra xem sản phẩm có được tạo thành công không"""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 1000)
        self.assertEqual(self.product.stock, 50)
        self.assertEqual(self.product.category.name, "Test Category")
        self.assertEqual(self.product.supplier.name, "Test Supplier")


class InventoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_inventory_management_view(self):
        """Kiểm tra xem view 'inventory_management' có trả về mã 200 không"""
        response = self.client.get(reverse('inventory_management'))
        self.assertEqual(response.status_code, 200)
