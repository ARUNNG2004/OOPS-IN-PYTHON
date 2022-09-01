

class Employee():
    workinghours=10

    def __init__(self,name,salary,degree):
        self.name=name
        self.salary=salary
        self.degree=degree
    
    def printdetails(self,a):
        return f" {a} Name is {self.name} ,salary is {self.salary} and degree is{self.degree}" 
    
    @classmethod
    def changeworkinghours(cls,newworkinghours):
        cls.workinghours=newworkinghours


arun=Employee("Arun",40,"btec")
ranga=Employee("don",50,"nothing")
arun.changeworkinghours(24)
print(arun.workinghours)
a=arun
print(a.printdetails(1))





# 52
