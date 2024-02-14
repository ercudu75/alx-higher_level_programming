-- create database 
CREATE DATABASE if NOT EXISTS hbtn_0d_usa;
-- connect to database
USE hbtn_0d_usa;
-- create a table
CREATE TABLE IF NOT EXISTS states(
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`name` VARCHAR(256),
	PRIMARY KEY (id)
);
