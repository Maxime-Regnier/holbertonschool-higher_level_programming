-- Create users if they do not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY '01234';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY '56789';

-- Revoke all privileges from user_0d_1
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_1'@'localhost';

-- Grant privileges
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE ON *.* TO 'user_0d_2'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

-- Display privileges
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';