import  pymysql

class   MYsqlUtils:
    con = None
    cursor = None

    @classmethod
    def read(cls,host='localhost',database='bank',user='root',password='',tablename='yinhang'):
        cls.con = pymysql.connect(host=host,user=user,password=password,database=database,charset='utf8')
        cls.cursor = cls.con.cursor()

        sql = '''
            select * from {tablename}
        '''
        cls.cursor.execute(sql.format(tablename=tablename))
        return cls.cursor.fetchall()

m=MYsqlUtils.read()
print(m)

