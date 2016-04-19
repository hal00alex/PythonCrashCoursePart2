#class and functions 
class Employee:
    empcount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1

    def displayCount(self):
        print ("Total Employee" + Employee.empcount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

#"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
#call special display functions just like C++ 
emp1.displayEmployee()
emp2.displayEmployee()
#print (getattr(emp1, 'salary'))
print(Employee.empcount)

#gatattr(emp1, 'name')
#hasattr(emp1, 'salary')
#to change: setattr(emp1, 'age', 8)
#delatte(emp1, 'age')
#free/delete: del emp1
#child/extending: class Intern(Employee) 
