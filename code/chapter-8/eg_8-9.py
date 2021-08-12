import sqlite3

sql = 'select * from users'
with sqlite3.connect("test.db") as conn:
    cur = conn.cursor()
    cur.execute(sql)                # 执行查询语句
    records = cur.fetchall()        # 获取查询结果
for row in records:
    print(row)
