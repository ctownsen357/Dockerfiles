from turbodbc import connect, make_options, Megabytes
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
options = make_options(read_buffer_size=Megabytes(20),
					   autocommit=True)

conn = connect(dsn='drill', turbodbc_options=options)
sql = "select * from dfs.`/test.csv`"
cursor = conn.cursor()
cursor.execute(sql)
table = cursor.fetchallarrow()
data = table.to_pandas()
print(data)
