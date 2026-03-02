-- Print the column names and types of first_table
SELECT 
COLUMN_NAME AS Field,
column_type AD Type,
IS_NULLABLE AS 'Null',
COLUMN_KEY AS 'Key',
COLUMN_DEFAULT AD 'Default',
EXTRA AS Extra
FROM information_schema.columns
WHERE table_name = 'first_table';