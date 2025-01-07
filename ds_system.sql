-- Tạo bảng User
CREATE TABLE Users (
    USERID INT IDENTITY(1,1) PRIMARY KEY,  
    USERNAME VARCHAR(50) NOT NULL,
    EMAIL VARCHAR(50) NOT NULL UNIQUE,
    PASSWORD VARCHAR(255) NOT NULL,
    UserPhone VARCHAR(15),
    ADDRESS VARCHAR(255),
    ROLE INT,
    CREATE_AT DATETIME DEFAULT CURRENT_TIMESTAMP,
    UPDATE_AT DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tạo bảng Products
CREATE TABLE Products (
    ProductID INT IDENTITY(1,1) PRIMARY KEY, 
    ProductName VARCHAR(255) NOT NULL,
    DescProduct TEXT,
    Carat_weight FLOAT,
    Origin VARCHAR(50),
    Clarity FLOAT,
    Category VARCHAR(100),
    Cut VARCHAR(50) CHECK (Cut IN ('Heart', 'Round', 'Oval', 'Princess', 'Marquise', 'Radiant', 'Emerald')) NOT NULL,
    Price FLOAT,
    Stock INT NOT NULL,
    ImagePro VARCHAR(255),
    Color VARCHAR(50),  
    Price_shell FLOAT,
    Create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    Update_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tạo bảng Customer
CREATE TABLE Customer (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY, 
    CustomerName VARCHAR(50) NOT NULL,
    CustomerPhone VARCHAR(50) NOT NULL,
    CustomerEmail VARCHAR(50) NOT NULL UNIQUE,
    CustomerAddress VARCHAR(255),
    SizeNI FLOAT
);

-- Tạo bảng Orders
CREATE TABLE Orders (
    OrderID INT IDENTITY(1,1) PRIMARY KEY, 
    CustomerID INT,
    OrderStatus INT,
    TotalAmount INT,
    Create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    Update_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Tạo bảng OrderDetail
CREATE TABLE OrderDetail (
    OrderDetailID INT IDENTITY(1,1) PRIMARY KEY, 
    OrderID INT,
    ProductID INT,
    Stock INT NOT NULL,
    Price FLOAT NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Tạo bảng Cart
CREATE TABLE Cart (
    CartID INT IDENTITY(1,1) PRIMARY KEY, 
    CustomerID INT,
    Create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    Update_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    Amount INT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Tạo bảng CartItem
CREATE TABLE CartItem (
    CartItemID INT IDENTITY(1,1) PRIMARY KEY, 
    CartID INT,
    ProductID INT,
    Stock INT NOT NULL,
    FOREIGN KEY (CartID) REFERENCES Cart(CartID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Tạo bảng Feedback
CREATE TABLE Feedback (
    FeedbackID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Rating FLOAT,
    Comment TEXT,
    Create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Tạo bảng Delivery Staff
CREATE TABLE DeliveryStaff (
    DeliveryStaffID INT IDENTITY(1,1) PRIMARY KEY, 
    OrderID INT,
    Status VARCHAR(50) CHECK (Status IN ('Xử lý', 'Đang giao', 'Đã giao', 'Đã huỷ')) NOT NULL, 
    Date DATE,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Tạo bảng Employee
CREATE TABLE Employee (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY, 
    UserID INT,
    Position VARCHAR(50),
    FOREIGN KEY (UserID) REFERENCES Users(USERID) 
);

-- Tạo bảng Report
CREATE TABLE Report (
    ReportID INT IDENTITY(1,1) PRIMARY KEY, 
    EmployeeID INT,
    ContentRP TEXT,
    Create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Tạo bảng Warranty
CREATE TABLE Warranty (
    WarrantyID INT IDENTITY(1,1) PRIMARY KEY, 
    ProductID INT,
    CustomerID INT,
    StarDate DATE,
    EndDate DATE,
    Terms TEXT,
    WarrantyStatus VARCHAR(50) CHECK (WarrantyStatus IN ('Active', 'Expired', 'Claimed', 'Cancelled')) DEFAULT 'Active', 
    Claim INT,
    WarrantyCreate_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    WarrantyUpdate_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Tạo bảng Point
CREATE TABLE Point (
    PointID INT IDENTITY(1,1) PRIMARY KEY, -- Sử dụng IDENTITY trong SQL Server
    CustomerID INT,
    Exchange_point INT,
    Point_used INT,
    Create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Tạo bảng Sales
CREATE TABLE Sales (
    SaleID INT IDENTITY(1,1) PRIMARY KEY, 
    Name VARCHAR(50),
    ProductID INT,
    StartDate DATE,
    EndDate DATE,
    Price FLOAT,
    DiscountPrice FLOAT,
    DiscountPercent DECIMAL(5,2) CHECK (DiscountPercent BETWEEN 0 AND 100), 
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Tạo bảng Desci
CREATE TABLE Desci (
    DescID INT IDENTITY(1,1) PRIMARY KEY, 
    CategoryDesc VARCHAR(100),
    NameDesc VARCHAR(255),
    Image VARCHAR(255),
    Content TEXT
);

-- Tạo bảng Wishlist
CREATE TABLE Wishlist (
    WishlistID INT IDENTITY(1,1) PRIMARY KEY, 
    ProductID INT NOT NULL,
    CustomerID INT NOT NULL,
    Create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);


SELECT * FROM Users;

SELECT * FROM Products;

SELECT * FROM Orders;

SELECT * FROM OrderDetail;

SELECT * FROM Cart;

SELECT * FROM CartItem;

SELECT * FROM Feedback;

SELECT * FROM DeliveryStaff;

SELECT * FROM Employee;

SELECT * FROM Report;

SELECT * FROM Warranty;

SELECT * FROM Point;

SELECT * FROM Sales;

SELECT * FROM Desci;

SELECT * FROM Wishlist;
