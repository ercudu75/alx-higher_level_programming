-- create database
CREATE DATABASE if NOT EXISTS hbtn_0d_usa;
-- connect to database
USE hbtn_0d_usa;
-- create a table
CREATE TABLE IF NOT EXISTS cities(
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256),
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
