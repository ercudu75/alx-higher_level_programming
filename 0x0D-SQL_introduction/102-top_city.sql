-- displays top 3 cities with the average temperature
SELECT city, AVG(value) as avg_temp
from temperatures
WHERE month BETWEEN 7 and 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
