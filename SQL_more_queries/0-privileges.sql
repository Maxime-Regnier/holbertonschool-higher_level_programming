-- List privileges for user_0d_1 and user_0d_2
SELECT user, host, Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv
FROM mysql.user
WHERE user IN ('user_0d_1', 'user_0d_2') AND host='localhost'