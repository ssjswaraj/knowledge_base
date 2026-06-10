--https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50
-- time taken : 02:34
select 
product_name,year,price
from sales s
inner join product p
on s.product_id=p.product_id
