# from django.test import TestCase
# from .models import Notification

# class NotificationModelTest(TestCase):

#     def test_create_notification(self):
#         notification = Notification.objects.create(
#             title="Test Notification",
#             message="This is a test notification",
#             customer_email="test@example.com"
#         )
#         self.assertEqual(notification.title, "Test Notification")
#         self.assertFalse(notification.is_read)

# Form có sẳn
from django.test import TestCase
from .models import Notification

class NotificationModelTest(TestCase):

    def setUp(self):
        Notification.objects.create(
            title="Test Notification 1",
            message="This is a test notification 1",
            customer_email="test1@example.com"
        )
        Notification.objects.create(
            title="Test Notification 2",
            message="This is a test notification 2",
            customer_email="test2@example.com"
        )

    def test_notification_creation(self):
        notification1 = Notification.objects.get(title="Test Notification 1")
        notification2 = Notification.objects.get(title="Test Notification 2")
        self.assertEqual(notification1.message, "This is a test notification 1")
        self.assertEqual(notification2.message, "This is a test notification 2")