-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50
-- time taken - 2:40
select customer_id,count(*) as  count_no_trans
from visits v left join transactions t
on v.visit_id = t.visit_id
where t.visit_id is null
group by customer_id
