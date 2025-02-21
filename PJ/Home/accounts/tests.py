from django.test import TestCase, Client, LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .models import Users
import bcrypt
import time

class AccountTests(TestCase):
    def setUp(self):
        # Tạo client để test
        self.client = Client()
        # Tạo user test
        self.test_user = Users.objects.create(
            username="Test User",
            email="test@example.com",
            password=bcrypt.hashpw("Test@123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            userphone="0123456789",
            is_active=True,
            role=1
        )

    def test_register_page_load(self):
        """Test trang đăng ký load thành công"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_success(self):
        """Test đăng ký thành công với dữ liệu hợp lệ"""
        data = {
            'username': 'New User',
            'email': 'newuser@example.com',
            'userphone': '0987654321',
            'password1': 'NewUser@123',
            'password2': 'NewUser@123'
        }
        response = self.client.post(reverse('register'), data)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(Users.objects.filter(email='newuser@example.com').exists())

    def test_register_invalid_email(self):
        """Test đăng ký với email không hợp lệ"""
        data = {
            'username': 'New User',
            'email': 'invalid-email',
            'userphone': '0987654321',
            'password1': 'NewUser@123',
            'password2': 'NewUser@123'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email', 'Email không hợp lệ')

    def test_register_weak_password(self):
        """Test đăng ký với mật khẩu yếu"""
        data = {
            'username': 'New User',
            'email': 'newuser@example.com',
            'userphone': '0987654321',
            'password1': 'weak',
            'password2': 'weak'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'password1', 'Mật khẩu phải có ít nhất 8 ký tự')

    def test_login_page_load(self):
        """Test trang đăng nhập load thành công"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_success(self):
        """Test đăng nhập thành công"""
        data = {
            'email': 'test@example.com',
            'password': 'Test@123'
        }
        response = self.client.post(reverse('login'), data)
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(self.client.session['user_email'], 'test@example.com')

    def test_login_wrong_password(self):
        """Test đăng nhập với mật khẩu sai"""
        data = {
            'email': 'test@example.com',
            'password': 'WrongPass@123'
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), 'Email hoặc mật khẩu không đúng')

    def test_login_nonexistent_user(self):
        """Test đăng nhập với email không tồn tại"""
        data = {
            'email': 'nonexistent@example.com',
            'password': 'Test@123'
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), 'Email hoặc mật khẩu không đúng')

    def test_register_duplicate_email(self):
        """Test đăng ký với email đã tồn tại"""
        data = {
            'username': 'Another User',
            'email': 'test@example.com',  # Email đã tồn tại
            'userphone': '0987654321',
            'password1': 'Test@123',
            'password2': 'Test@123'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email', 'Email này đã được sử dụng')

class AccountSeleniumTests(LiveServerTestCase):
    def setUp(self):
        # Khởi tạo Chrome WebDriver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # Tạo user test
        self.test_user = Users.objects.create(
            username="Test User",
            email="test@example.com",
            password=bcrypt.hashpw("Test@123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            userphone="0123456789",
            is_active=True,
            role=1
        )

    def tearDown(self):
        self.driver.quit()

    def test_register_form_ui(self):
        """Test UI của form đăng ký"""
        # Mở trang đăng ký
        self.driver.get(f'{self.live_server_url}/register/')
        
        # Kiểm tra tiêu đề trang
        self.assertEqual("Register Account", self.driver.title)
        
        # Kiểm tra các trường input tồn tại
        username_input = self.driver.find_element(By.NAME, "username")
        email_input = self.driver.find_element(By.NAME, "email")
        phone_input = self.driver.find_element(By.NAME, "userphone")
        password1_input = self.driver.find_element(By.NAME, "password1")
        password2_input = self.driver.find_element(By.NAME, "password2")
        
        # Điền thông tin đăng ký
        username_input.send_keys("Selenium Test User")
        email_input.send_keys("selenium@test.com")
        phone_input.send_keys("0987654321")
        password1_input.send_keys("Selenium@123")
        password2_input.send_keys("Selenium@123")
        
        # Submit form
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Đợi chuyển hướng đến trang login
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(f'{self.live_server_url}/login/')
        )

    def test_login_form_ui(self):
        """Test UI của form đăng nhập"""
        # Mở trang đăng nhập
        self.driver.get(f'{self.live_server_url}/login/')
        
        # Kiểm tra tiêu đề trang
        self.assertEqual("Login Account", self.driver.title)
        
        # Kiểm tra các trường input tồn tại
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        
        # Điền thông tin đăng nhập
        email_input.send_keys("test@example.com")
        password_input.send_keys("Test@123")
        
        # Submit form
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Đợi chuyển hướng đến trang home
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(f'{self.live_server_url}/home/')
        )

    def test_login_validation_messages(self):
        """Test hiển thị thông báo lỗi khi đăng nhập"""
        self.driver.get(f'{self.live_server_url}/login/')
        
        # Test với email không tồn tại
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        
        email_input.send_keys("wrong@email.com")
        password_input.send_keys("WrongPass@123")
        
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Đợi và kiểm tra thông báo lỗi
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        )
        self.assertIn("Email hoặc mật khẩu không đúng", error_message.text)

    def test_register_validation_messages(self):
        """Test hiển thị thông báo lỗi khi đăng ký"""
        self.driver.get(f'{self.live_server_url}/register/')
        
        # Test với email không hợp lệ
        username_input = self.driver.find_element(By.NAME, "username")
        email_input = self.driver.find_element(By.NAME, "email")
        phone_input = self.driver.find_element(By.NAME, "userphone")
        password1_input = self.driver.find_element(By.NAME, "password1")
        password2_input = self.driver.find_element(By.NAME, "password2")
        
        username_input.send_keys("Test User")
        email_input.send_keys("invalid-email")
        phone_input.send_keys("0987654321")
        password1_input.send_keys("Test@123")
        password2_input.send_keys("Test@123")
        
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Đợi và kiểm tra thông báo lỗi
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        )
        self.assertIn("Email không hợp lệ", error_message.text)
