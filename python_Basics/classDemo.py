# class calc():
#     num=200
#     def addtion(self):
#         print("addtion")
# obj=calc()
# obj.addtion()
# print(obj.num)

# using constructor
class Calculator():
    Number=100
    def __init__(self,a,b):
        self.FirstNumber =a
        self.SecondNumber =b
    def SumIntergers(self):
        return self.FirstNumber + self.SecondNumber + Calculator.Number
obj = Calculator(5,10)
obj.SumIntergers()
print(obj.SumIntergers())