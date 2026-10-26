USE northwind;

-- 1. List the producr id, product name, and unit price of every product. 

SELECT ProductID, ProductName, UnitPrice 
FROM Products; 

-- 2. Write a query to identify the products where the unit price is $7.50 or less

SELECT ProductId, ProductName, UnitPrice
FROM Products
WHERE UnitPrice <= 7.50;

-- 3. What are the products that we carry where we have no units on hand, but 1 or more
-- units are on backorder

SELECT ProductName, UnitsInStock, UnitsOnOrder
FROM Products
WHERE UnitsInStock = 0
AND UnitsOnOrder > 0;

-- 4. List all seafood products 

SELECT ProductName FROM Products 
WHERE CategoryID = 8; 

-- 5.Products supplied by Tokyo Traders 

SELECT *
FROM Suppliers
WHERE CompanyName = 'Tokyo Traders';

-- 6. How many employeed work at Northwin and "manager somewhere in their job title 

SELECT COUNT(*) AS EmployeeCount 
FROM Employees;

SELECT FirstName, LastName, Title FROM Employees
WHERE Title Like '%manager%';
