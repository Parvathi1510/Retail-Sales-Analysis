-- 1. Sales and profit by category
SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

-- 2. Sales by region
SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

-- 3. Top 10 products by sales
SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;

-- 4. Monthly sales trend
SELECT
    SUBSTR(order_date, 1, 7) AS sales_month,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales
WHERE order_date IS NOT NULL
GROUP BY sales_month
ORDER BY sales_month;

-- 5. Products with the lowest total profit
SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales
GROUP BY product_name
ORDER BY total_profit ASC
LIMIT 10;