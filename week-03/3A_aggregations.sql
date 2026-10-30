USE northwind;

-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a

SELECT MIN(UnitPrice)
FROM Products;

-- second query to find the name of the product that has that price
SELECT ProductName
From Products 
WHERE UnitPrice = (
	SELECT MIN(UnitPrice) 
	FROM Products
);

-- 2. Write a query to find the average price of all items that Northwind sells

SELECT AVG(UnitPrice)
FROM Products;

-- 3. Write a query to find the price of the most expensive item that Northwind sells.

SELECT MAX(UnitPrice)
FROM Products; 

 -- 3.b Then write a second query to find the name of the product with that price, plus the name of
-- the supplier for that product.

SELECT Products.ProductName, Suppliers.CompanyName
FROM Products
JOIN Suppliers
    ON Products.SupplierID = Suppliers.SupplierID
WHERE Products.UnitPrice = (
    SELECT MAX(UnitPrice)
    FROM Products
);
    
-- 4. Write a query to find total monthly payroll (the sum of all the employees’ monthly
-- salaries).

SELECT SUM(Salary) / 12 AS Total_Monthly_Payroll 
FROM Employees;

--  5. Write a query to identify the highest salary and the lowest salary amounts which any
-- employee makes. (Just the amounts, not the specific employees!)

SELECT MAX(Salary) , MIN(Salary)
FROM Employees;

-- 6. Write a query to find the name and supplier ID of each supplier and the number of
-- items they supply. Hint: Join is your friend here.

SELECT Suppliers.CompanyName, Suppliers.SupplierID, COUNT(Products.ProductID)
FROM Suppliers
JOIN Products
    ON Suppliers.SupplierID = Products.SupplierID
GROUP BY Suppliers.CompanyName, Suppliers.SupplierID; 

-- 7. Write a query to find the list of all category names and the average price for items in
-- each category.

SELECT 
	Categories.CategoryName , 
	AVG(Products.UnitPrice) AS Average_Price 
FROM Categories 
INNER JOIN Products 
	ON Categories.CategoryID = Products.CategoryID
GROUP BY Categories.CategoryName;

-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
-- is the name of each supplier and the number of items they supply

SELECT 
	Suppliers.CompanyName , 
    COUNT(Products.ProductID) AS Number_of_Items 
FROM Suppliers 
JOIN Products 
	ON Suppliers.SupplierID = Products.SupplierID 
GROUP BY Suppliers.CompanyName
HAVING COUNT(Products.ProductID) >= 5;

-- 9. Write a query to list products currently in inventory by the product id, product name,
-- and inventory value (calculated by multiplying unit price by the number of units on
-- hand). Sort the results in descending order by value. If two or more have the same
-- value, order by product name. If a product is not in stock, leave it off the list.

SELECT
    Products.ProductID,
    Products.ProductName,
    Products.UnitPrice * Products.UnitsInStock AS Inventory_Value
FROM Products
WHERE Products.UnitsInStock > 0
ORDER BY Inventory_Value DESC, Products.ProductName ASC;









