-- Drop users if they exist
DROP USER IF EXISTS 'user_0d_1'@'localhost';
DROP USER IF EXISTS 'user_0d_2'@'localhost';

-- Create users
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY '01234';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY '56789';

-- Grant privileges
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE ON *.* TO 'user_0d_2'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

-- Display privileges
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';