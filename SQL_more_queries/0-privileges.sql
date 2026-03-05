-- Create users if they do not exist and grant privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY '01234';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY '56789';

-- Grant privileges to user_0d_1
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE ON *.* TO 'user_0d_1'@'localhost';
-- Grant privileges to user_0d_2
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE ON *.* TO 'user_0d_2'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

-- Display privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Display privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';