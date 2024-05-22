-- Query the three cities with the highest average temperatures between July and August. --
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month > 6 AND month <= 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
