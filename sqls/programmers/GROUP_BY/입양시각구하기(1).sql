SELECT HOUR(DATETIME), COUNT(HOUR(DATETIME))
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) > 8 and HOUR(DATETIME) < 20
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME)


SELECT HOUR(datetime) AS HOUR, COUNT(HOUR(datetime)) AS COUNT
FROM animal_outs
GROUP BY HOUR(datetime)
HAVING HOUR >= 9 AND HOUR <= 19
ORDER BY HOUR


SELECT hour(datetime) as hour,count(datetime) as count
FROM ANIMAL_OUTS
where hour(datetime) between 9 and 19
group by hour
order by hour;