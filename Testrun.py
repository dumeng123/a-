import unittest
from pythonProject1.entity import Bank
from ddt import ddt
from ddt import  data
from ddt import unpack
from pythonProject1.utils.DataRead import Dataread
data2 = Dataread('database',database='bank',tablename='yinhang',user='root',password='').list
@ddt
class TestBank(unittest.TestCase):
    @data(*data2)
    @unpack
    def testSaveMoney(self,a,b):
        d = False

        s = Bank.bank_saveMoney(a,b)

        # id = '123456'
        # money = 1000
        # status = False


        self.assertEqual(d,s)

