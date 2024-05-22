-- This script creates a table named unique_id with a single column id that is unique and not null. The column has a default value of 1. --
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1
);
