-- Write your MySQL query statement below
select afterw.Id from Weather afterw, Weather beforew 
where DATEDIFF(day, beforew.recordDate, afterw.recordDate)=1 and afterw.temperature > beforew.temperature