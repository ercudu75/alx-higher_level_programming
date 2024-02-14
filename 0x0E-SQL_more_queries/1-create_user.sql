-- create user in mysql server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY "user_0d_1_pwd";
-- give the user all privileges
GRANT ALL PRIVILEGES
ON *.*
TO 'user_0d_1'@'localhost';

