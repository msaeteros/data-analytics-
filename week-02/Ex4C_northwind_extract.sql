-- Ex4C_northwind_extract.sql

-- 4a. The table that holds the items Northwind sells is Products.

-- 4b. The table that holds the types/categories of items
-- Northwind sells is Categories.

USE northwind;

SELECT * FROM employees;

-- 5a. Margaret Peacock is the employee whose name makes it look like shes is a bird

SELECT * FROM products; 

-- 6a. The number of records returned is 77 
-- To display only 10 rows, change the row limit in the MYSQL workbench toolbar labeled "Limit to 1000 rows" to 10 

SELECT * FROM categories;

-- 7. The category ID for Seafood id 8 

SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;

