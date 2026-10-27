USE northwind;

-- 1.Write a query to list the product id, product name, and unit price of every product. This
-- time, display them in ascending order by price

SELECT ProductID, ProductName, UnitPrice
 FROM Products
 ORDER BY UnitPrice ASC;
 
 -- 2. What are the products that we carry where we have at least 100 units on hand? Order
-- them in descending order by price

SELECT ProductID, ProductName, UnitPrice
From Products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;

-- 3.  Products with at least 100 units on hand.
-- Order by price descending, then product name ascending 

SELECT ProductName, UnitsInStock, UnitPrice
FROM Products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, ProductName ASC;

-- 4. Total number of distinct customers who placed orders

SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders;

-- 5. Distinct Customers by ship country 

SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS CustomerCount 
FROM Orders 
GROUP BY ShipCountry 
ORDER BY CustomerCount DESC; 

-- 6. Products with less than 25 units in stock and at least 1 unit on order.

SELECT ProductName,
       UnitsInStock,
       UnitsOnOrder
FROM Products
WHERE UnitsInStock < 25
AND UnitsOnOrder > 0
ORDER BY UnitsOnOrder DESC, ProductName ASC;

-- 7. Job titles and number of employees

SELECT Title,
       COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Title;

SELECT Title,
       COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Title
ORDER BY EmployeeCount DESC;

