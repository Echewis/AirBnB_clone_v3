-- this script will prepare an MySQL server for the project
-- This will create project testing database named : hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- This is for creating new user named :
-- hbnb_test with all privileges on the db hbnb_test_db
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- This is for granting the SELECT privilege for the user named
-- hbnb_test on the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- This is for granting all privileges to the new user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
