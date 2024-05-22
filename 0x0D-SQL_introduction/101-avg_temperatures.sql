-- Title: Average Temperatures by City
SELECT city, AVG(temperature) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
