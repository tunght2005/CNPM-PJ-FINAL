from django.test import TestCase, Client
from django.urls import reverse

class CustomerPageTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_customer_page_loads(self):
        response = self.client.get(reverse('customer'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer.html')

    def test_customer_page_contains_profile_info(self):
        response = self.client.get(reverse('customer'))
        self.assertContains(response, 'Thông tin tài khoản')
        self.assertContains(response, 'Tài Khoản Của Tôi')

class GiftPageTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_gift_page_loads(self):
        response = self.client.get(reverse('gift'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gift.html')

    def test_gift_page_contains_voucher_info(self):
        response = self.client.get(reverse('gift'))
        self.assertContains(response, 'VOUCHER GIẢM GIÁ')
        self.assertContains(response, 'Điều Kiện Áp Dụng')