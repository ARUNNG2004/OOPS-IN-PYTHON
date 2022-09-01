from cgi import print_directory


class Employee():

    def __init__(self,name,salary,degree):
        self.name=name
        self.salary=salary
        self.degree=degree
    workinghours=12
    def printdetails(self,a):
        return f" {a} Name is {self.name} ,salary is {self.salary} and degree is{self.degree}" 
  
arun=Employee("Arun",40,"btec")
ranga=Employee("don",50,"nothing")
