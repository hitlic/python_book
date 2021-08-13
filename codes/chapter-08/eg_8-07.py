import sqlite3
conn = sqlite3.connect('test.db')          # 建立数据库连接
cur = conn.cursor()                        # 获取游标
sql = 'create table users(id int primary key, name varchar, email varchar)'
cur.execute(sql)                           # 执行SQL语句
cur.close()                                # 关闭游标
conn.close()                               # 关闭数据库连接
