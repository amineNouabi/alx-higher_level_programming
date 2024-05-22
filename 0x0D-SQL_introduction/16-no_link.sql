-- This script list all records of the table second_table where the name is not NULL and the records are ordered by score (highest first) --
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
