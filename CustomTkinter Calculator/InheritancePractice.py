class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age

    def printdetails(self):
        print(self.firstname, self.lastname)
    
    def combine(self, person1):
        print(self.fname + " " + person2.fname)
        print(self.lname + " " + person.lname)
        print(self.age + person.age)
        
class Student(Person):
    pass 


x = Person("John", "Doe", 52)
x.printdetails()

y = Student("Mike", "Olsen", 15)
y.printdetails()

x.combine(x, y)
y.combine(x, y)



