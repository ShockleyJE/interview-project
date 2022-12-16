SELECT 
*
FROM postgres.information_schema.table_constraints
WHERE table_name = 'books_authors_link'
AND constraint_type = 'FOREIGN KEY'
--AND constraint_name = 'books_authors_link_author_fkey'
--constraint_name
;

SELECT 
table_name, 
column_name
FROM postgres.information_schema.constraint_column_usage
WHERE constraint_name = 'books_authors_link_author_fkey'
;

SELECT 
cu.table_name
,cu.column_name
FROM postgres.information_schema.table_constraints tc
INNER JOIN postgres.information_schema.constraint_column_usage cu 
ON tc.constraint_name = cu.constraint_name
WHERE tc.table_name = 'books_authors_link'
AND tc.constraint_type = 'FOREIGN KEY'
AND tc.constraint_name = 'books_authors_link_author_fkey'
;

SELECT  cu.table_name ,cu.column_name FROM postgres.information_schema.table_constraints tc 
INNER JOIN postgres.information_schema.constraint_column_usage cu  
ON tc.constraint_name = cu.constraint_name WHERE tc.table_name = '{table}' AND tc.constraint_type = 'FOREIGN KEY'