-- Query all cities in the cities table that are located in California. The cities should be ordered by id in ascending order. --
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
