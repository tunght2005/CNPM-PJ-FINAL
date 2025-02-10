# from django.test import TestCase

# # Create your tests here.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import unittest

# class LoginTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("https://127.0.0.1/admin/login/?next=/admin/")

#     def test_valid_login(self):
#         driver = self.driver
#         username = driver.find_element(By.ID, "username")
#         password = driver.find_element(By.ID, "password")
#         submit_button = driver.find_element(By.ID, "submit")
#         username.send_keys("valid_user")
#         password.send_keys("valid_password")
#         submit_button.click()
#         welcome_message = driver.find_element(By.ID, "welcome")
#         self.assertIn("Welcome", welcome_message.text)

#     def tearDown(self):
#         self.driver.quit()

# import time
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# class NotificationTest(unittest.TestCase):
#     # KB: Hàm setUpClass() và tearDownClass() sẽ chạy 1 lần duy nhất trước và sau khi chạy tất cả các test case
#     #  Khởi tạo trình duyệt trước khi chạy test
#     # TH1: Kiểm tra danh sách thông báo có hiển thị không
#     # TH2: Kiểm tra nút 'Đánh Dấu Đã Đọc' hoạt động
#     # TH3: Kiểm tra nút 'Xóa' hoạt động
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome()  # Nếu dùng Edge, đổi thành webdriver.Edge()
#         cls.driver.maximize_window()
#         cls.driver.get("http://127.0.0.1:8000/")  # URL của ứng dụng Django

#     def test_unit_load_notifications(self):
#         notifications = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
#         self.assertGreater(len(notifications), 0, "Không có thông báo nào hiển thị!")

#     def test_unit_mark_as_read(self):
#         button = self.driver.find_element(By.CSS_SELECTOR, ".mark-read")
#         button.click()
#         time.sleep(2)  # Chờ API xử lý
#         self.assertEqual(button.text, "Đã Đọc", "Nút không cập nhật đúng!")

#     def test_unit_delete_notification(self):
#         delete_button = self.driver.find_element(By.CSS_SELECTOR, ".delete")
#         delete_button.click()
#         time.sleep(2)  # Chờ cập nhật UI
#         deleted_rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
#         self.assertEqual(len(deleted_rows), 0, "Thông báo không bị xóa!")

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()

# if __name__ == "__main__":
#     unittest.main()
