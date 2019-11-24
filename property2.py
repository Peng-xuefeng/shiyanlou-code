#将输入的account 美金 转化为 人民币
class Account(object):
    def __init__(self,rate):
        self.rate = rate
        self._amount = 0
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self,value):
        if value < 0:
            print("金额不能为负数")
        else:
            self._amount = value
    @property
    def cny(self):
        return self._amount * self.rate

acc = Account(7.0)
acc.amount = -1
print("目前的金额为：",acc.amount)
print("转化为人民币的金额为:",acc.cny)   
acc.amount = 30
print("目前的金额为：",acc.amount)
print("转化为人民币的金额为:",acc.cny)        
    