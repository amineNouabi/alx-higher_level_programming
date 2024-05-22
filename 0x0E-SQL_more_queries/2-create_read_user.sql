-- Create a new user named user_0d_2 with the password user_0d_2_pwd, and give them SELECT permission on the hbtn_0d_2 database. --
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
