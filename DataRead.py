from pythonProject1.utils.DBUtils import MYsqlUtils
# from pythonProject1.utils.ExcelUtils import  ExcelUtils
import  os
class Dataread:
    list = None #全局列表 mode = excel,filename sheetname
    #database
    def __init__(self,mode,filename='',sheetname = '0',host='localhost',database = '',user = '',password='',tablename=''):
        if mode == 'excel':
            if filename == '':
                raise Exception('文件名不能为空！，别瞎弄！')
            elif not os.path.isfile(filename):
                raise Exception('文件不存在！，别瞎弄！')
            else:
                Dataread.list=ExcelUtils.read(filename,sheetname)

        elif mode == 'database':
            Dataread.list = MYsqlUtils.read(host=host,database=database,user=user,password=password,tablename=tablename)

        else:
            raise Exception('对不起，您的操作无法识别')
