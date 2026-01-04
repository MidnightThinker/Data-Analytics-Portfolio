-- 1. ¿Cuál es el producto que más ingresos generó?
SELECT 
    Product, 
    SUM(Total_Revenue) as Total_Revenue
FROM sales_data
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 1;

-- 2. ¿Cuál es el promedio de venta por cada categoría de producto?
SELECT 
    Category, 
    AVG(Total_Revenue) as Avg_Revenue
FROM sales_data
GROUP BY Category;

-- 3. Ranking de los 5 mejores clientes basado en su gasto total.
SELECT 
    CustomerID, 
    SUM(Total_Revenue) as Total_Spent
FROM sales_data
GROUP BY CustomerID
ORDER BY Total_Spent DESC
LIMIT 5;
