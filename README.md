# Interview Project

## Purpose:

To query database schema internals and expose over API

## Relevant Files:

### /

`start_local.py` - run the development server on 3030
`scratch.sql` - scratch sql file for testing the queries

### /server

`app.py` - simple entrypoint
`ex_query.py` - with pyodbc, handle the queries about DB schema internals. As INFORMATION_SCHEMA is ansi-standard, if we stray from syntax-specific features, we can keep queries consistent between database technologies
`ex_endpoints` - API endpoint definitions to call the functions and return from `ex_query.py`

### /server/configs

`databse.py` - define database connection details (omitted)

## Questions

Assumptions: limited to public schema

1. list all tables for a database

2. given a specific table, what are the columns and data types

3. given a specific table, find the table name and column name to which its foreign key constraints are directed towards

## Result

I passed this technical interview
