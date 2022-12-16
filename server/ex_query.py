from server.configs.database import pgstr
import pyodbc

def get_all_tables():
    with pyodbc.connect(pgstr) as cnxn:
        cursor = cnxn.cursor()
        desc_tuple = cursor.execute('select * from information_schema.tables')
        rows = cursor.fetchall()
        # Append to a JSON serializable structure (list)
        data = []
        tables = set()
        schemas = set()
        for row in rows:
            tables.add(row.table_name)
            schemas.add(row.table_schema)
            data.append(list(row))

        print(f"Found {len(rows)} tables and {len(schemas)} schemas")

        return list(tables)

def get_coldata_for_table(table):

    qstr = f"SELECT column_name, data_type FROM postgres.information_schema.columns WHERE table_name = '{table}' AND table_schema = 'public'"
    with pyodbc.connect(pgstr) as cnxn:

        cursor = cnxn.cursor()
        cursor.execute(qstr)
        rows = cursor.fetchall()
        res = []
        for row in rows:
            name = row.column_name
            type = row.data_type
            res.append([name, type])
            print(f"col: {row.column_name}, data type: {row.data_type}")
        
        return res

def get_keydata_for_table(table):

    with pyodbc.connect(pgstr) as cnxn:

        cursor = cnxn.cursor()
        qstr = """
            SELECT 
            cu.table_name
            ,cu.column_name
            FROM postgres.information_schema.table_constraints tc
            INNER JOIN postgres.information_schema.constraint_column_usage cu 
            ON tc.constraint_name = cu.constraint_name
            WHERE tc.table_name = ?
            AND tc.constraint_type = 'FOREIGN KEY'
            """
        cursor.execute(qstr, table)
        rows = cursor.fetchall()
        res = []
        for row in rows:
            name = row[0]
            type = row[1]
            res.append([name, type])
            print(f"col: {name}, data type: {type}")
        
        return res
