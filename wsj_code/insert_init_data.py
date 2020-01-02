import pymysql
import re
# 连接数据库
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='123456',
                     database='project',
                     charset='utf8')
# 封装成基类：连接库/自动关闭

# 生产游标对象 （操作数据库执行sql语句获取结果的对象）
cur = db.cursor()
# 插入单词
f = open('/home/tarena/下载/lc1.txt')
args_list = []
for line in f:
    # 获取单词和解释
    result = re.findall(r"(\S+)\s+(.*)",line)
    args_list.extend(result) # 合并为一个列表
f.close()

sql="insert into adjective (words,name) values (%s,%s);"
try:
    cur.executemany(sql,args_list)
    db.commit()
except:
    db.rollback()


# 关闭游标和数据库
cur.close()
db.close()




