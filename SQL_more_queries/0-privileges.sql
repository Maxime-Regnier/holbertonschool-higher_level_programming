-- Create users if they do not exist and grant privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY '01234';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY '56789';

GRANT SELECT, INSERT, UPDATE, DELETE, CREATE ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE ON *.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;

-- List privileges for user_0d_1 and user_0d_2
SELECT user, host, Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv
FROM mysql.user
WHERE user IN ('user_0d_1', 'user_0d_2') AND host='localhost';