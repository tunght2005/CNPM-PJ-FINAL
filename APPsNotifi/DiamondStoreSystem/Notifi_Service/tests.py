from django.test import TestCase
from .models import Notification

class NotificationModelTest(TestCase):

    def test_create_notification(self):
        notification = Notification.objects.create(
            title="Test Notification",
            message="This is a test notification",
            customer_email="test@example.com"
        )
        self.assertEqual(notification.title, "Test Notification")
        self.assertFalse(notification.is_read)

# Form có sẳn
# from django.test import TestCase
# from .models import Notification

# class NotificationTestCase(TestCase):
#     def setUp(self):
#         Notification.objects.create(
#             order_code="#00123", status="Đang xử lý", order_date="2024-12-15"
#         )

#     def test_notification_creation(self):
#         notification = Notification.objects.get(order_code="#00123")
#         self.assertEqual(notification.status, "Đang xử lý")