import sqlite3
conn = sqlite3.connect("test.db")  # 建立数据库连接
cur = conn.cursor()                # 获取游标

sql = "insert into users values(1, '张三', 'zhangsan@test.com')"
cur.execute(sql)                   # 添加一条数据

sql = "insert into users values(?,?,?)"
data = [(2, '李四', 'lisi@test.com'),
        (3, '王五', 'wangwu@test.com'),
        (4, '赵六', 'zhaoliu@test.com')]
cur.executemany(sql, data)         # 添加多条数据

sql = "update users set email='lisi_new@test.com' where id=2"
cur.execute(sql)                   # 修改数据

sql = "delete from users where id=3"
cur.execute(sql)                   # 删除数据
conn.commit()                      # 提交操作
cur.close()
conn.close()
