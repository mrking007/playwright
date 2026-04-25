from classDemo import Calculator

class inheritence(Calculator):
    num2 =300
    def __init__(self):
        Calculator.__init__(self,5,10)
    def getCompleteData(self):
        return self.num2 + self.Number+ self.SumIntergers()

obj=inheritence()
print(obj.getCompleteData())