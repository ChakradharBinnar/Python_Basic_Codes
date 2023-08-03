class Employee:
    sal = 85000

    def __init__(self, name, city):
        self.name = name
        self.city = city

    @classmethod
    def nwSalary(cls, salary):
        cls.sal = salary

    def data1(self):
        print(
            f"my name is {self.name}, i am from {self.city}. my salay is {self.sal}.")


# Employee.nwSalary(90000)

obj1 = Employee('chikku', 'nashik')
obj2 = Employee('Babdii', 'nashik')

obj1.nwSalary(98000)

obj1.data1()
obj2.data1()
