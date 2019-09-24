#计算销售人员的工资，基本工资1500，卖出一台相机得200，并且得到相机单价2%的抽成
basic_salary = 1500
number = int(input("how many he sold?"))
price = int(input("how much is the camare:"))
bonus = number * 200
commission = number * price * 0.02  
print("销售人员的工资为: {:6.3f}".format(basic_salary+bonus+commission))