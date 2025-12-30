class MyClass():
    def __init__(self, age, name, career):
        self.age = age
        self.name = name
        self.career = career
    
    def __str__(self):
        if hasattr(self, "age") == True:
            print("Hes got an age")
            return f"Name: {self.name}, Age: {self.age}, Career: {self.career}"
        else:
            print("No Age")
            return f"Name: {self.name}, Career: {self.career}"
    
    def print_name(self):
        return "Hello my name is " + self.name


person1 = MyClass(24, "John", "Random Guy")

print(person1)
print(person1.print_name())
person1.age = person1.age * 2
print(person1.age)
del person1.age
print(person1)