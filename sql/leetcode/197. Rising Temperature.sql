-- https://leetcode.com/problems/rising-temperature/?envType=study-plan-v2&envId=top-sql-50
select id 
from (select id, recorddate, temperature, 
lag(temperature)  over(order by recorddate) as old_temp,
lag(recorddate) over(order by recorddate) as old_date
from Weather ) d where temperature>old_temp
and datediff(day,old_date,recorddate)=1
