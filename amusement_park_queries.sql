--drop database amusement_park;
--create database if not exists amusement_park;
--use amusement_park;

CREATE TABLE Promotions (
    id INT PRIMARY KEY IDENTITY(1, 1),
    name NVARCHAR(255) NOT NULL,
    description STRING,              --CHECK CONSTRAINS ARE NOT ENFORCED IN SNOWFLAKE? WHY?
    discount_percentage DECIMAL(5,2), --CHECK (discount_percentage >= 0 AND discount_percentage <= 100),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE Visitors (
    id INT PRIMARY KEY IDENTITY(1, 1),
    name NVARCHAR(255) NOT NULL,
    email NVARCHAR(255) UNIQUE NOT NULL,
    phone NVARCHAR(25) UNIQUE NOT NULL
);

CREATE TABLE Tickets (
    id INT PRIMARY KEY IDENTITY(1, 1),
    type NVARCHAR(50) NOT NULL, -- CHECK (type IN ('adult', 'group', 'children', 'students')) NOT NULL, 
    price DECIMAL(10,2) NOT NULL,
    validity_start DATE NOT NULL,
    validity_end DATE NOT NULL,
    status NVARCHAR(50), -- CHECK (status IN ('active', 'expired')) NOT NULL,
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
    capacity INT NOT NULL, -- CHECK (capacity > 0),
    status NVARCHAR(50) NOT NULL,-- CHECK (status IN ('operational', 'closed')),
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
    salary DECIMAL(10,2) NOT NULL, --??? CHECK (salary > 0),
    manager_id INT NULL FOREIGN KEY REFERENCES Employees(id) ON DELETE NO ACTION
);

CREATE TABLE Maintenance_logs (
    id INT PRIMARY KEY IDENTITY(1, 1),
    attraction_id INT NOT NULL FOREIGN KEY REFERENCES Attractions(id) ON DELETE CASCADE,
    employee_id INT NULL FOREIGN KEY REFERENCES Employees(id) ON DELETE SET NULL,
    date DATE NOT NULL,
    description STRING,
    cost DECIMAL(10,2) NOT NULL --CHECK (cost >= 0)
);

CREATE TABLE Attraction_usage (
    id INT PRIMARY KEY IDENTITY(1, 1),
    ticket_id INT NOT NULL FOREIGN KEY REFERENCES Tickets(id) ON DELETE CASCADE,
    attraction_id INT NOT NULL FOREIGN KEY REFERENCES Attractions(id) ON DELETE CASCADE,
    duration INT NOT NULL -- CHECK (duration > 0)
);

CREATE TABLE Sales (
    id INT PRIMARY KEY IDENTITY(1, 1),
    product_id INT NULL FOREIGN KEY REFERENCES Products(id) ON DELETE SET NULL,
    visitor_id INT NULL FOREIGN KEY REFERENCES Visitors(id) ON DELETE SET NULL,
    employee_id INT NOT NULL FOREIGN KEY REFERENCES Employees(id) ON DELETE NO ACTION,
    quantity INT NOT NULL,-- CHECK (quantity > 0),
    sale_date DATETIME NOT NULL DEFAULT GETDATE(),
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
    gross_salary DECIMAL(10,2) NOT NULL, -- CHECK (gross_salary > 0),
    deductions DECIMAL(10,2) NOT NULL, -- CHECK (deductions >= 0),
    net_salary DECIMAL(10,2) NOT NULL, -- CHECK (net_salary >= 0),
    payment_date DATE NOT NULL
);

CREATE TABLE Transactions (
    id INT PRIMARY KEY IDENTITY(1, 1),
    reason varchar(255) not null,
    type NVARCHAR(100) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,-- CHECK (amount > 0),
    date DATETIME NOT NULL DEFAULT GETDATE(),
    sale_id INT NULL FOREIGN KEY REFERENCES Sales(id) ON DELETE SET NULL,
    ticket_id INT NULL FOREIGN KEY REFERENCES Tickets(id) ON DELETE SET NULL,
    payroll_id INT NULL FOREIGN KEY REFERENCES Payroll(id) ON DELETE SET NULL,
    maintenance_id INT NULL FOREIGN KEY REFERENCES Maintenance_logs(id) ON DELETE SET NULL
);

ALTER TABLE EMPLOYEES
ADD EMAIL VARCHAR(255) NOT NULL UNIQUE;

ALTER TABLE EMPLOYEES
ADD PHONE_NUMBER VARCHAR(25) NOT NULL;

ALTER TABLE EMPLOYEES 
ADD ADDRESS VARCHAR(255) NOT NULL;

INSERT INTO DEPARTMENTS (NAME) VALUES
('Operations'),
('Guest service'),
('Maintanence and engineering'),
('Food and bevarages'),
('Security and safety'),
('Marketing and sales'),
('Human resources'),
('Finance');

INSERT INTO JOB (NAME) VALUES
('Ride operator'),
('Guest relation specialist'),
('Technician'),
('Food Stand attendant'),
('Security officer'),
('Marketing coordinator'),
('Retail associate'),
('HR Recruiter'),
('Accountant'),
('CEO');

INSERT INTO EMPLOYEES(NAME, EMAIL, PHONE_NUMBER, ADDRESS, JOB_ID, DEPARTMENT_ID, HIRE_DATE, SALARY) VALUES
('Amanda Owen', 'yrichards@example.net', '773.420.2242', '0146 Hogan Courts Robertsonville, MS 06509', 10, 6, '1975-10-13', 6352),
('Samantha Williams', 'vincenttina@example.net', '4444995523', '705 John Fall Ricemouth, GA 63293', 7, 6, '1998-04-01', 3334),
('Tracy Johnson', 'bmonroe@example.net', '001-844-315', '98300 Weber Parkways Apt. 770 East Katherineland, NH 27443', 9, 5, '1981-12-27', 7670),
('Stephen Moody', 'terri20@example.org', '+1-446-330-4706', '125 Gilbert Shoal South Robertaborough, WY 33521', 10, 3, '2002-06-08', 4921),
('Jessica David', 'owood@example.net', '892-822-8639', 'USS Garcia FPO AA 60769', 9, 2, '2006-11-07', 2691),
('James Richards', 'yhartman@example.net', '001-320-230-52', '8183 Dylan Valley Suite 669 Caldwellborough, VA 98635', 10, 6, '1982-09-07', 8343),
('Steven Stone', 'tatekimberly@example.org', '663-416-6798', '3904 Bates Loop Apt. 300 New Kevinbury, SC 88114', 2, 7, '1990-03-10', 4098),
('Ashley Valencia', 'kelly72@example.net', '+1-710-836-536', '46976 Zachary Shores Apt. 665 South Jason, OR 33781', 8, 5, '1978-05-05', 4028),
('Curtis Cobb', 'lori86@example.org', '001-600-961-3', '379 Victoria Center Debraburgh, KY 88327', 10, 1, '1980-01-17', 6879),
('Andrea Walker', 'sandraphillips@example.net', '(409)854-7086', 'PSC 5800, Box 0162 APO AA 87419', 5, 1, '1997-06-02', 3711),
('Charles Smith', 'adamcruz@example.org', '001-804-287-7623x53492', '22219 Lester Greens Apt. 294 Anthonyton, AS 06303', 7, 1, '2013-04-15', 5420),
('Nathan Cook', 'isimon@example.com', '001-577-512-6654x891', '370 Molina Expressway West Jeff, CA 56674', 3, 2, '2002-07-07', 8606),
('Denise Allen', 'patrickmorgan@example.org', '241.613.9015', '035 Morse Square Morrowtown, NY 64568', 3, 6, '1983-05-12', 1514),
('Heather Smith', 'julianglenn@example.org', '(351)986-5610', 'PSC 6611, Box 7185 APO AE 78328', 8, 2, '1983-02-05', 6723),
('Amanda Thompson', 'adamramos@example.net', '(594)522-3057x60447', '94469 Walter Corner Jamestown, OH 96344', 7, 1, '2020-08-06', 2619),
('Omar Mcdonald', 'clarkreginald@example.org', '663-948-9110', '82461 Robert Spring Port Michael, VI 65419', 9, 8, '2021-12-15', 7626),
('Laura Ramirez', 'bobby05@example.org', '701-528-6534', '66343 Brennan Creek Armstrongport, AS 79554', 7, 3, '1976-12-22', 7619),
('Lisa Terrell', 'ruthdickson@example.net', '2902560916', '68813 Watts Turnpike South Tyler, MT 14286', 3, 2, '1980-05-16', 8146),
('Keith Lopez', 'whitekaitlyn@example.com', '447-664-3949', '40697 Crawford Plains Apt. 040 East Darlene, WV 34097', 8, 2, '1973-05-17', 1338),
('Stephanie Garrison', 'peter93@example.com', '517.564.2476', '566 Melissa Island Suite 819 Samanthaborough, WI 52563', 4, 4, '1997-02-03', 4803),
('Patricia Austin', 'hjohnson@example.net', '211.214.6736x06913', '10973 Johnathan Mountain Morrisonville, MS 60917', 9, 2, '2023-07-15', 1834),
('Jamie Freeman', 'vaughnaaron@example.com', '+1-349-559-8035', '0621 Megan Well Apt. 956 Port Deborah, MO 20669', 4, 1, '2005-08-09', 3312),
('James Owen', 'khenderson@example.org', '215-431-4771', '086 Michael Ferry Suite 910 New Kelsey, KY 44107', 9, 2, '1980-10-22', 5289),
('Joel Mullins', 'josephmorales@example.org', '001-336-260-2845x807', '1410 Robert Square Suite 236 Christianmouth, VA 12096', 3, 3, '2016-05-22', 5613),
('Linda Thomas', 'hansonfrederick@example.net', '(798)945-5504', '4451 Robinson Mission Hudsontown, DE 08659', 3, 6, '2001-09-23', 2861),
('Dennis Castaneda', 'karenyoung@example.net', '001-612-408-1250x4649', 'Unit 2503 Box 5079 DPO AA 73991', 4, 5, '1989-03-16', 8266),
('Jared Shaw', 'odonnellmichael@example.net', '+1-277-791-5941x98482', '47914 Barnes Throughway Lisabury, MT 58124', 2, 1, '1994-03-22', 2267),
('Scott Bryant', 'chase24@example.org', '001-621-332-3317', '95365 Kathy Crossing Suite 753 Hartchester, MT 63837', 7, 2, '1992-03-03', 8567),
('Lisa Roberts', 'xjohnson@example.org', '+1-623-988-6201x04333', '83117 Nicholas Pass Lake Christinechester, MH 57756', 3, 7, '2017-09-13', 2996),
('Joel Cooper', 'meganallen@example.net', '250.843.1351x03660', '055 Pierce Summit Apt. 973 East Tiffany, SD 98794', 1, 1, '2021-02-26', 5267);

select * from employees
order by id;


--1 4 6 9
update employees 
set manager_id = 1 where salary > 4000;

update employees
set manager_id = 4 where job_id > 8;

update employees
set manager_id = 6 where department_id = 6;

update employees
set manager_id = 9 where id in (19, 22, 27, 27, 15, 10);

update employees
set manager_id = null where job_id = 10;

insert into employee_shifts (employee_id, date_start, date_end, start_hour, end_hour) 
values (1, '2023-10-01', '2023-10-01', '09:00', '17:00'),
(2, '2023-10-02', '2023-10-02', '08:00', '16:00'),
(3, '2023-10-03', '2023-10-03', '10:00', '18:00'),
(4, '2023-10-04', '2023-10-04', '07:00', '15:00'),
(5, '2023-10-05', '2023-10-05', '12:00', '20:00'),
(6, '2023-10-06', '2023-10-06', '09:30', '17:30'),
(7, '2023-10-07', '2023-10-07', '08:30', '16:30'),
(8, '2023-10-08', '2023-10-08', '11:00', '19:00'),
(9, '2023-10-09', '2023-10-09', '06:00', '14:00'),
(10, '2023-10-10', '2023-10-10', '13:00', '21:00'),
(11, '2023-10-11', '2023-10-11', '10:30', '18:30'),
(12, '2023-10-12', '2023-10-12', '07:30', '15:30'),
(13, '2023-10-13', '2023-10-13', '14:00', '22:00'),
(14, '2023-10-14', '2023-10-14', '05:00', '13:00'),
(15, '2023-10-15', '2023-10-15', '12:30', '20:30'),
(16, '2023-10-16', '2023-10-16', '09:00', '17:00'),
(17, '2023-10-17', '2023-10-17', '08:00', '16:00'),
(18, '2023-10-18', '2023-10-18', '11:30', '19:30'),
(19, '2023-10-19', '2023-10-19', '06:30', '14:30'),
(20, '2023-10-20', '2023-10-20', '13:30', '21:30'),
(21, '2023-10-21', '2023-10-21', '10:00', '18:00'),
(22, '2023-10-22', '2023-10-22', '07:00', '15:00'),
(23, '2023-10-23', '2023-10-23', '14:30', '22:30'),
(24, '2023-10-24', '2023-10-24', '05:30', '13:30'),
(25, '2023-10-25', '2023-10-25', '12:00', '20:00'),
(26, '2023-10-26', '2023-10-26', '09:00', '17:00'),
(27, '2023-10-27', '2023-10-27', '08:00', '16:00'),
(28, '2023-10-28', '2023-10-28', '11:00', '19:00'),
(29, '2023-10-29', '2023-10-29', '06:00', '14:00'),
(30, '2023-10-30', '2023-10-30', '13:00', '21:00');

INSERT INTO shops (name, type, location) VALUES
('SuperMart', 'Grocery', 'NW str'),
('TechWorld', 'Electronics', 'NW str'),
('FashionHub', 'Clothing', 'NW str'),
('BookNook', 'Bookstore', 'Magic district'),
('HealthyBites', 'Restaurant', 'Magic district'),
('PetParadise', 'Pet Store', 'Magic district'),
('GadgetZone', 'Electronics', 'Magic district'),
('StyleStudio', 'Clothing', 'Magic district'),
('CafeBliss', 'Cafe', 'Center'),
('FitLife', 'Restaurant', 'Center');

INSERT INTO TICKETS (TYPE, PRICE, VALIDITY_START, VALIDITY_END, STATUS, PROMOTION_ID)
VALUES 
('Adult', 30, '2025-3-10', '2025-3-15', 'available', 0),
('Adult Group 5', 120, '2025-3-10', '2026-3-20', 'available', 0),
('Students', 10, '2025-3-10', '2025-7-15', 'available', 0),
('Children', 5, '2025-3-10', '2026-3-15', 'available', 0),
('Student Group 5', 45, '2025-3-10', '2025-3-15', 'available', 0),
('Student University', 5, '2023-3-10', '2024-3-15', 'not available', 0);

select * from tickets;

update tickets set price = price*1.1 where status like 'not available';

INSERT INTO promotions (ID, NAME, DESCRIPTION, DISCOUNT_PERCENTAGE, START_DATE, END_DATE) VALUES
(1, 'Summer Sale', 'Enjoy discounts on summer collections', 15.00, '2023-06-01', '2023-06-30'),
(2, 'Back to School', 'Special offers for school supplies', 20.00, '2023-08-01', '2023-08-31'),
(3, 'Black Friday', 'Huge discounts on electronics and more', 50.00, '2023-11-24', '2023-11-27'),
(4, 'Holiday Special', 'Festive discounts on all items', 25.00, '2023-12-15', '2023-12-31'),
(5, 'New Year Clearance', 'Clearance sale to start the new year', 30.00, '2024-01-01', '2024-01-15'),
(6, 'Spring Fling', 'Fresh deals for spring fashion', 10.00, '2023-03-01', '2023-03-31'),
(7, 'Tech Week', 'Exclusive discounts on tech gadgets', 40.00, '2023-09-10', '2023-09-17'),
(8, 'Winter Warmers', 'Cozy deals for winter essentials', 15.00, '2023-12-01', '2023-12-14'),
(9, 'Flash Sale', 'Limited-time flash sale on select items', 60.00, '2023-07-15', '2023-07-16'),
(10, 'Anniversary Sale', 'Celebrate our anniversary with special discounts', 35.00, '2023-10-10', '2023-10-20');

INSERT INTO products (shop_id, name, price, category) VALUES
(1, 'Cotton Candy', 5.99, 'Food'),
(1, 'Popcorn', 4.50, 'Food'),
(2, 'Souvenir Mug', 12.99, 'Merchandise'),
(2, 'Keychain', 7.99, 'Merchandise'),
(3, 'Hot Dog', 6.99, 'Food'),
(3, 'Soda', 3.50, 'Beverage'),
(4, 'T-Shirt', 19.99, 'Merchandise'),
(4, 'Cap', 14.99, 'Merchandise'),
(5, 'Ice Cream', 4.99, 'Food'),
(5, 'Funnel Cake', 8.50, 'Food'),
(6, 'Water Bottle', 2.99, 'Beverage'),
(6, 'Pretzel', 5.50, 'Food'),
(7, 'Stuffed Toy', 24.99, 'Merchandise'),
(7, 'Postcard Set', 9.99, 'Merchandise'),
(8, 'Burger', 7.99, 'Food'),
(8, 'Fries', 4.50, 'Food'),
(9, 'Sunglasses', 15.99, 'Merchandise'),
(9, 'Sunscreen', 10.99, 'Essentials'),
(10, 'Pizza Slice', 6.50, 'Food'),
(10, 'Smoothie', 5.99, 'Beverage');


select * from products;

insert into visitors (name, email, phone) values
('Kevin Mitchell', 'alexbrooks@example.net', '821-214-2200'),
('Ashley Cline', 'michaelmoss@example.com', '+1-957-616-8537'),
('Karen Tran', 'tsullivan@example.net', '(475)739-2682'),
('David Underwood', 'christinahess@example.net', '435-831-3160'),
('Thomas Smith', 'deborah41@example.com', '660.255.0917'),
('Kim Nelson', 'wendy05@example.org', '(878)867-3094'),
('Michael Weiss', 'nicholas04@example.org', '001-449-731-9'),
('Jose Jones', 'jacobfarrell@example.org', '819.606.9943'),
('Shannon Kirk', 'wilsontonya@example.org', '001-398-809'),
('Christopher Pineda', 'michelle85@example.com', '+1-593-816-1434'),
('Matthew Williamson', 'rsmith@example.org', '471-322-6820'),
('Jeffrey Anderson', 'xmartinez@example.com', '614-274-2210'),
('Katherine Stafford', 'corey62@example.org', '606.217.8075'),
('Melissa Johnson', 'howens@example.org', '+1-573-769-9740'),
('Sandra Wilson', 'derrickbrown@example.net', '706.520.1156'),
('Mrs. Hannah Benjamin', 'rhonda88@example.org', '3493643164'),
('Andrew Davis MD', 'amy19@example.com', '001-879-722-9164'),
('Mr. Kevin Grant', 'lboone@example.net', '001-960-319-9694'),
('William Larson', 'ethan03@example.com', '(936)387-2938'),
('Frank Valdez', 'elizabethrodriguez@example.org', '2969053666');

INSERT INTO ATTRACTIONS (NAME, TYPE, CAPACITY, STATUS, LOCATION)
VALUES ('Ferris Wheel', 'Ride', 100, 'Open', 'Amusement Park'),
('Haunted House', 'Ride', 50, 'Closed', 'Theme Park'),
('Roller Coaster', 'Ride', 200, 'Open', 'Adventure Park'),
('Water Slide', 'Water Ride', 150, 'Open', 'Water Park'),
('Bumper Cars', 'Ride', 40, 'Closed', 'Amusement Park'),
('Carousel', 'Ride', 60, 'Open', 'Theme Park'),
('Ferris Tower', 'Ride', 120, 'Open', 'City Park'),
('Log Flume', 'Water Ride', 80, 'Open', 'Water Park'),
('Drop Tower', 'Ride', 100, 'Closed', 'Adventure Park'),
('Pirate Ship', 'Ride', 150, 'Open', 'Amusement Park');



