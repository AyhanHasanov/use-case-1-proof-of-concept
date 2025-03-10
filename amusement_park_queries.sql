
drop database amusement_park;
create database if not exists amusement_park;
use amusement_park;


CREATE TABLE Promotions (
    id INT PRIMARY KEY IDENTITY(1, 1),
    name NVARCHAR(255) NOT NULL,
    description STRING,           
    discount_percentage DECIMAL(5,2),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE Visitors (
    id INT PRIMARY KEY IDENTITY(1, 1),
    name NVARCHAR(255) NOT NULL,
    email NVARCHAR(255) UNIQUE NOT NULL,
    phone NVARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE Tickets (
    id INT PRIMARY KEY IDENTITY(1, 1),
    type NVARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    validity_start DATE NOT NULL,
    validity_end DATE NOT NULL,
    status NVARCHAR(50),
    promotion_id INT NULL FOREIGN KEY REFERENCES Promotions(id) ON DELETE SET NULL
);

CREATE TABLE Visitors_Tickets (
    id INT PRIMARY KEY IDENTITY(1, 1),
    visitor_id INT NOT NULL FOREIGN KEY REFERENCES Visitors(id) ON DELETE NO ACTION,
    ticket_id INT NOT NULL FOREIGN KEY REFERENCES Tickets(id) ON DELETE NO ACTION,
    purchase_date DATETIME NOT NULL DEFAULT GETDATE()
);

CREATE TABLE Shops (
    id INT PRIMARY KEY IDENTITY(1, 1),
    name NVARCHAR(255) NOT NULL,
    type NVARCHAR(100) NOT NULL,
    location NVARCHAR(255) NOT NULL
);

CREATE TABLE Products (
    id INT PRIMARY KEY IDENTITY(1, 1),
    name NVARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category NVARCHAR(100) NOT NULL,
    shop_id INT NULL FOREIGN KEY REFERENCES Shops(id) ON DELETE SET NULL
);

CREATE TABLE Attractions (
    id INT PRIMARY KEY IDENTITY(1, 1),
    name NVARCHAR(255) NOT NULL,
    type NVARCHAR(100) NOT NULL,
    capacity INT NOT NULL, 
    status NVARCHAR(50) NOT NULL,
    location NVARCHAR(255) NOT NULL
);

CREATE TABLE Job (
    id INT PRIMARY KEY IDENTITY(1, 1),
    name NVARCHAR(255) NOT NULL
);

CREATE TABLE Departments (
    id INT PRIMARY KEY IDENTITY(1, 1),
    name NVARCHAR(255) NOT NULL
);

CREATE TABLE Employees (
    id INT PRIMARY KEY IDENTITY(1, 1),
    name NVARCHAR(255) NOT NULL,
    job_id INT NOT NULL FOREIGN KEY REFERENCES Job(id) ON DELETE NO ACTION,
    department_id INT NOT NULL FOREIGN KEY REFERENCES Departments(id) ON DELETE NO ACTION,
    hire_date DATE NOT NULL,
    salary DECIMAL(10,2) NOT NULL, 
    manager_id INT NULL FOREIGN KEY REFERENCES Employees(id) ON DELETE NO ACTION
);

CREATE TABLE Maintenance_logs (
    id INT PRIMARY KEY IDENTITY(1, 1),
    attraction_id INT NOT NULL FOREIGN KEY REFERENCES Attractions(id) ON DELETE CASCADE,
    employee_id INT NULL FOREIGN KEY REFERENCES Employees(id) ON DELETE SET NULL,
    date DATE NOT NULL,
    description STRING,
    cost DECIMAL(10,2) NOT NULL
);

CREATE TABLE Attraction_usage (
    id INT PRIMARY KEY IDENTITY(1, 1),
    ticket_id INT NOT NULL FOREIGN KEY REFERENCES Tickets(id) ON DELETE CASCADE,
    attraction_id INT NOT NULL FOREIGN KEY REFERENCES Attractions(id) ON DELETE CASCADE,
    duration INT NOT NULL 
);

CREATE TABLE Sales (
    id INT PRIMARY KEY IDENTITY(1, 1),
    product_id INT NULL FOREIGN KEY REFERENCES Products(id) ON DELETE SET NULL,
    visitor_id INT NULL FOREIGN KEY REFERENCES Visitors(id) ON DELETE SET NULL,
    employee_id INT NOT NULL FOREIGN KEY REFERENCES Employees(id) ON DELETE NO ACTION,
    quantity INT NOT NULL,
    sale_date DATETIME NOT NULL DEFAULT GETDATE(),
    total DECIMAL(10,2) NOT NULL, 
    promotion_id INT NULL FOREIGN KEY REFERENCES Promotions(id) ON DELETE SET NULL
);

CREATE TABLE Special_events (
    id INT PRIMARY KEY IDENTITY(1, 1),
    name NVARCHAR(255) NOT NULL,
    type NVARCHAR(100) NOT NULL,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    location NVARCHAR(255) NOT NULL,
    description STRING
);

CREATE TABLE EventAttendance (
    id INT PRIMARY KEY IDENTITY(1, 1),
    event_id INT NULL FOREIGN KEY REFERENCES Special_events(id) ON DELETE SET NULL,
    visitor_id INT NULL FOREIGN KEY REFERENCES Visitors(id) ON DELETE SET NULL,
    date DATE NOT NULL
);

CREATE TABLE Employee_shifts (
    id INT PRIMARY KEY IDENTITY(1, 1),
    employee_id INT NOT NULL FOREIGN KEY REFERENCES Employees(id) ON DELETE CASCADE,
    date_start DATE NOT NULL,
    date_end DATE NOT NULL,
    start_hour TIME NOT NULL,
    end_hour TIME NOT NULL
);

CREATE TABLE Payroll (
    id INT PRIMARY KEY IDENTITY(1, 1),
    employee_id INT NULL FOREIGN KEY REFERENCES Employees(id) ON DELETE SET NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    gross_salary DECIMAL(10,2) NOT NULL, 
    deductions DECIMAL(10,2) NOT NULL, 
    net_salary DECIMAL(10,2) NOT NULL, 
    payment_date DATE NOT NULL
);

CREATE TABLE Transactions (
    id INT PRIMARY KEY IDENTITY(1, 1),
    type NVARCHAR(100) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    date DATETIME NOT NULL DEFAULT GETDATE(),
    visitor_id INT NULL FOREIGN KEY REFERENCES Visitors(id) ON DELETE SET NULL,
    employee_id INT NULL FOREIGN KEY REFERENCES Employees(id) ON DELETE NO ACTION,
    sale_id INT NULL FOREIGN KEY REFERENCES Sales(id) ON DELETE SET NULL,
    ticket_id INT NULL FOREIGN KEY REFERENCES Tickets(id) ON DELETE SET NULL,
    payroll_id INT NULL FOREIGN KEY REFERENCES Payroll(id) ON DELETE SET NULL,
    maintenance_id INT NULL FOREIGN KEY REFERENCES Maintenance_logs(id) ON DELETE SET NULL
);

