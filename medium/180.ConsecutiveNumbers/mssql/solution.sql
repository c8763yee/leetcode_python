/* Write your T-SQL query statement below */
SELECT DISTINCT n.num AS ConsecutiveNums FROM (
    SELECT *, LEAD(num) OVER (ORDER BY id) AS leads_num, LAG(num) OVER (ORDER BY id) AS lags_num, LEAD(id) OVER (ORDER BY id) AS leads_id, LAG(id) OVER (ORDER BY id) AS lags_id 
    from Logs 
) AS n
WHERE n.num=n.leads_num AND n.lags_num=n.num AND n.leads_id=n.id+1 AND n.lags_id=n.id-1