-- https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=top-sql-50
-- Pyspark_Solution = 

select product_id from products
where low_fats ='Y' and recyclable ='Y'
