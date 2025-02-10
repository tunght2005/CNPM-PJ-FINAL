# import time
# import unittest
# import importlib  
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
#         time.sleep(5)  # Chờ API xử lý
#         self.assertEqual(button.text, "Đã Đọc", "Nút không cập nhật đúng!")

#     def test_unit_delete_notification(self):
#         delete_button = self.driver.find_element(By.CSS_SELECTOR, ".delete")
#         delete_button.click()
#         time.sleep(5)  # Chờ cập nhật UI
#         deleted_rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
#         self.assertEqual(len(deleted_rows), 0, "Thông báo không bị xóa!")

# if __name__ == "__main__":
#     unittest.main()

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NotificationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  
        cls.driver.maximize_window()
        cls.driver.get("http://127.0.0.1:8000/")  # URL của ứng dụng Django

    def test_unit_load_notifications(self):
        """Test: Kiểm tra danh sách thông báo có hiển thị không"""
        # Chờ đến khi các hàng trong bảng được load (tối đa 10 giây)
        notifications = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr"))
        )
        # Nếu không có thông báo, trang sẽ hiển thị dòng "Không có thông báo nào."
        # Ta kiểm tra xem nội dung của hàng đó có chứa "Không có thông báo nào" không.
        if notifications and "Không có thông báo nào" in notifications[0].text:
            self.fail("Không có thông báo nào hiển thị! Hãy kiểm tra dữ liệu test.")
        else:
            self.assertGreater(len(notifications), 0, "Không có thông báo nào hiển thị!")

    def test_unit_mark_as_read(self):
        """Test: Kiểm tra nút 'Đánh Dấu Đã Đọc' hoạt động và cập nhật trạng thái"""
        driver = self.driver

        # Chờ nút 'Đánh Dấu Đã Đọc' xuất hiện và có thể click được
        mark_read_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".mark-read"))
        )
        mark_read_button.click()

        # Chờ backend xử lý (2 giây) và reload trang
        time.sleep(2)
        driver.refresh()
        time.sleep(2)

        # Tìm lại nút; nếu đã được cập nhật, nội dung sẽ là "Đã Đọc"
        updated_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".mark-read"))
        )
        self.assertEqual(updated_button.text.strip(), "Đã Đọc", "Nút không cập nhật đúng trạng thái 'Đã Đọc'!")

    def test_unit_delete_notification(self):
        """Test: Kiểm tra nút 'Xóa' hoạt động và xóa thông báo khỏi giao diện"""
        driver = self.driver

        # Chờ nút 'Xóa' có thể click được
        delete_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".delete"))
        )
        delete_button.click()

        # Chờ backend xử lý xóa (2 giây) và reload trang
        time.sleep(2)
        driver.refresh()
        time.sleep(2)

        # Lấy danh sách các hàng thông báo còn lại
        remaining_notifications = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        # Nếu trang hiển thị dòng "Không có thông báo nào", nghĩa là đã xóa hết dữ liệu.
        if remaining_notifications and "Không có thông báo nào" in remaining_notifications[0].text:
            self.assertEqual(len(remaining_notifications), 1, "Thông báo không bị xóa!")
        else:
            self.fail("Thông báo không bị xóa!")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
