-- create Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user in mysql server
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY "user_0d_2_pwd";
-- give privileges to user_0d_2
GRANT SELECT
ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost';
