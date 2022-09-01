class Employee():

    workinghours=12
  
arun=Employee()
ranga=Employee()
arun.name="arun"
arun.salary=1
arun.degree="B.Tech"

ranga.name="Ranga"
ranga.salary=100000
ranga.degree="summa irukkarathu"
ranga.workinghours=20
print(ranga.workinghours)
print(Employee.__dict__)