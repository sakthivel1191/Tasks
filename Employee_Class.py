class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self.salary)

employee1=Employee("sakthi",23,25000)
employee2=Employee("mukil",27,50000)

employee1.display()
employee2.display()

