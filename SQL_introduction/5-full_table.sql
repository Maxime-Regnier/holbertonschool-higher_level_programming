-- Print the column names and types of fist_table
SELECT column_name, column_type
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';