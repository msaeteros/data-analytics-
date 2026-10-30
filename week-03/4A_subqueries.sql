USE northwind;

-- 1. What is the product name(s) of the most expensive products?

SELECT ProductName
FROM Products
WHERE UnitPrice = (
	SELECT MAX(UnitPrice)
	FROM Products 
);

-- 2.What is the product name(s) and categories of the least expensive products?

SELECT Products.ProductName, Categories.CategoryName 
FROM Products 
JOIN Categories
	ON Products.CategoryID = Categories.CategoryID 
WHERE Products.UnitPrice = (
	SELECT MIN(UnitPrice)
	FROM Products
);

-- 3. What is the order id, shipping name and shipping address of all orders shipped via
-- "Federal Shipping"?

-- What I did first 
SELECT o.OrderID, o.ShipName, o.ShipAddress
FROM orders o
JOIN shippers s
    ON o.ShipVia = s.ShipperID
WHERE o.ShipVia = (
    SELECT ShipperID
    FROM shippers
    WHERE CompanyName = 'Federal Shipping'
);


-- What AI told me it should have been 
SELECT OrderID, ShipName, ShipAddress
FROM orders
WHERE ShipVia = (
    SELECT ShipperID
    FROM shippers
    WHERE CompanyName = 'Federal Shipping'
);


-- 4. What are the order ids of the orders that included "Sasquatch Ale"?
SELECT OrderID 
FROM OrderDetails 
WHERE ProductName = (
	SELECT ProductID 
    FROM Products
    WHERE ProdcutsName = 'Sasquatch Ale'
);

-- 5. What is the name of the employee that sold order 10266?

SELECT FirstName , LastName 
FROM Employees 
WHERE EmployeeID= (
	SELECT EmployeeID
    FROM Orders 
    WHERE OrderID = 10266 
);
	
-- 6. What is the name of the customer that bought order 10266

SELECT ContactName 
FROM Customers
WHERE CustomerID = (
	SELECT CustomerID
    FROM Orders
    WHERE OrderID = 10266
);





