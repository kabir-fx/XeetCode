# Write your MySQL query statement below
-- Intuition is to club 3 tables together AND for that monolith table filter out the desired outcome.

SELECT DISTINCT T1.NUM AS ConsecutiveNums

FROM LOGS T1, LOGS T2, LOGS T3

WHERE T1.ID = T2.ID -1 AND T1.ID = T3.ID -2 AND T1.NUM = T2.NUM AND T2.NUM = T3.NUM
