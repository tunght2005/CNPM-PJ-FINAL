from django.test import TestCase

# Create your tests here.
import sqlite3
import os
from django.db import connection
from django.test import TestCase

class MyTestCase(TestCase):
    def setUp(self):
        # Tạo cơ sở dữ liệu tạm thời cho test
        self.db_name = "test_database.db"
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

        # Tạo bảng trong cơ sở dữ liệu
        self.cursor.execute('''
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.connection.commit()

        # Chèn dữ liệu vào bảng
        self.cursor.execute('''
            INSERT INTO products (name, price) VALUES
            ('Diamond', 500),
            ('Gold', 300)
        ''')
        self.connection.commit()

    def test_database_query(self):
        # Kiểm tra việc truy vấn từ cơ sở dữ liệu
        self.cursor.execute('SELECT * FROM products')
        rows = self.cursor.fetchall()

        # Kiểm tra có bao nhiêu sản phẩm trong bảng
        self.assertEqual(len(rows), 2)

        # Kiểm tra tên sản phẩm
        self.assertEqual(rows[0][1], 'Diamond')
        self.assertEqual(rows[1][1], 'Gold')

    def tearDown(self):
        # Đóng kết nối và xóa cơ sở dữ liệu sau khi kiểm tra
        self.cursor.close()
        self.connection.close()
        os.remove(self.db_name)
