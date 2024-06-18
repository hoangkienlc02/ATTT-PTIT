CREATE TABLE Company(
   cid VARCHAR(5) PRIMARY KEY,
   cname VARCHAR(20),
   city VARCHAR(20));

INSERT INTO Company VALUES ('123','GizmoWorks', 'New York');
INSERT INTO Company VALUES ('234','Canon',    'Tokyo');
INSERT INTO Company VALUES ('345','Hitachi',  'Tokyo');

CREATE TABLE Product(
   pname VARCHAR(20) PRIMARY KEY,
   price float,
   cid VARCHAR(5) references Company);

PRAGMA foreign_keys=ON;

INSERT INTO Product VALUES ('Gizmo',      19.99, '123');
INSERT INTO Product VALUES ('PowerGizmo', 29.99, '123');
INSERT INTO Product VALUES ('SingleTouch', 149.99, '234');
INSERT INTO Product VALUES ('MultiTouch', 199.99, '345');
INSERT INTO Product VALUES ('SuperGizmo', 49.99, '345');

-- Before we start, let's switch to a better query output format
.mode column
.header ON

--------------------------------------------------------------------------------
-- 1. Subqueries in WHERE

--- For each product, return the city where it is manufactured

SELECT X.pname, ( SELECT Y.city
                  FROM Company Y
                  WHERE Y.cid=X.cid) as City
FROM  Product X

--- Or Equivalent

SELECT X.pname, Y.city  FROM  Product X, Company Y  WHERE X.cid=Y.cid

--- Compute the number of products made by each company

SELECT DISTINCT C.cname, ( SELECT count(*)
                           FROM Product P  
                           WHERE P.cid=C.cid)
FROM  Company C

--- Unnest it using GROUP BY

SELECT C.cname, count(*)  FROM Company C, Product P  WHERE C.cid=P.cid

--- GROUP bY with OUTER JOIN

SELECT C.cname, count(pname)
FROM Company C LEFT OUTER JOIN Product P  ON C.cid=P.cid
GROUP BY C.cname

-- 2. Subqueries in FROM

--- Find all products whose prices is > 20 and < 500

SELECT X.pname
FROM (SELECT * FROM Product AS Y WHERE price > 20) as X  
WHERE X.price < 500

--- Unnest above query

SELECT pname  
FROM Product
WHERE price > 20 AND price < 500

--- Find all companies that make some products with price < 100

---- Using EXISTS

SELECT DISTINCT   C.cname
FROM  Company C  WHERE  
   EXISTS (SELECT *
               FROM Product P
               WHERE C.cid = P.cid and P.price < 100)

---- Using IN

SELECT DISTINCT   C.cname
FROM  Company C
WHERE C.cid IN (SELECT P.cid
                  FROM Product P  
                  WHERE P.price < 100)

---- Using ANY (Not supported in SQLite !!!)

SELECT DISTINCT   C.cname
FROM  Company C
WHERE 100 > ANY (SELECT price
                  FROM Product P  
                  WHERE P.cid = C.cid)

---- Unnest it -> Existential quantifiers are easy !

SELECT DISTINCT   C.cname
FROM  Company C, Product P  
WHERE   C.cid= P.cid and P.price < 100

--- Find all companies where all their products have price < 100

---- 1. Find the other companies with some product having price ≥ 100

SELECT DISTINCT   C.cname
FROM  Company C
WHERE C.cid IN (SELECT P.cid
                  FROM Product P  
                  WHERE P.price >= 100)

---- 2. Find all companies where all their products have price < 100

SELECT DISTINCT   C.cname
FROM  Company C
WHERE C.cid NOT IN (SELECT P.cid
                     FROM Product P  
                     WHERE P.price >= 100)

---- Using EXISTS

SELECT DISTINCT   C.cname
FROM  Company C
WHERE NOT EXISTS (SELECT *
                  FROM Product P
                  WHERE P.cid = C.cid and P.price >= 100)

---- Using ALL (Not supported in SQLite !!!)

SELECT DISTINCT   C.cname
FROM  Company C
WHERE 100 >= ALL  (SELECT price
                     FROM Product P  
                     WHERE P.cid = C.cid)

---- Unnest it -> This kind of query can not be unnested !!!

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
-- EXERCISE: Write the following queries, based on the database schema

---- Product(maker,model, type)
---- PC(model, speed, ram, hd, price) 
---- Laptop(model, speed, ram, hd, screen, price) 
---- Printer(model, color, type, price)

--- You should use at least one subquery in each of your answers and write each query in two significantly different ways 
--- (e.g., using different sets of the operators EXISTS,IN,ALL,and ANY).

--- 1. Find the makers of PC’s with a speed of at least 3.0.

--- 2. Find the printers with the highest price.

--- 3. Find the laptops whose speed is slower than that of any PC.

--- 4. Find the model number of the item (PC, laptop, or printer) with the highest price.

--- 5. Find the maker of the color printer with the lowest price.

--- 6. Find the maker(s) of the PC(s) with the fastest processor among all those PC’s that have the smallest amount of RAM.
