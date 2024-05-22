-- Query the three cities with the highest average temperatures.
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
