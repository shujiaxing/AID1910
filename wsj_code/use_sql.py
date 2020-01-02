
import pymysql
class Python_use_mysql():
    # 服务端定好这些参数，然后传递过来
    def __init__(self,host,port,user,password,database,charset):
        self.db = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset=charset)
        self.cursor = self.db.cursor()

    # 查询，得到数据后，还需要遍历，然后判断结果
    def select_data(self, sql):
        try:
            self.cursor.execute(sql)
            # 得到一条查询结果
            res = self.cursor.fetchall()
        except pymysql.Error as e:
            print(e)
        return res

    # 析构函数,服务器代码要执行这个函数去关闭数据库连接
    def __del__(self):
        # 对象销毁时关闭游标和数据库连接
        self.cursor.close()
        self.db.close()
