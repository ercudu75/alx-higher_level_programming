-- displays the average temperature
SELECT city, AVG(value) as avg_temp
from temperatures
GROUP BY city
ORDER BY avg_temp DESC;
