import pyodbc

conn = pyodbc.connect("DSN=drill", autocommit=True)
cursor = conn.cursor()

sql = 'select * from dfs.`/test.csv`'

cursor.execute(sql)

data = cursor.fetchall()

print(data)
