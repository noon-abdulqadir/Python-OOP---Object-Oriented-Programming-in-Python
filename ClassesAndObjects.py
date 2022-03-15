class Person():
    
    company = "XYZ" # class variable
    count = 0
    
    def __init__(self, title, name, age, maritalStatus):
        self._title = title
        self.__name = name # dunder __ for private
        self.__age = age
        self.__maritalStatus = maritalStatus
        Person.count+=1
        
    def _display(self): # _ for protected
        print(f"I am {self.__name} and I am {self.__age} years old.")
    
    def greet(self):
        if self.age < 70:
            print("Hello, how are you?")
        else:
            print("Hello, how do you do?")
        self._display()
    
    @property  # Decorator. To access this method, we call it like an instance variable but we can't assign anything to it
    def title(self):
        return(self._title)
    
    @title.setter
    def title(self, title):
        self._title = title
    
    @property 
    def age(self):
        return(self.__age)
    
    @age.setter # a condition applied to a property also applies to the object instance
    def age(self, new_age):
        if 20 < new_age < 80:
            self.__age = new_age
        else:
            raise(ValueError("Age must be between 20 and 80."))
        
    @property  # without a setter, the property (aka getter) becomes read-only
    def fullname(self):
        return f'{self._title} {self.__name}'
    
    @property  # without a getter functionality, the setter becomes write-only
    def maritalStatus(self):
        raise(ValueError("Marital Status is write-only."))
    
    @maritalStatus.setter  # setter to access the getter/decorator
    def maritalStatus(self, maritalStatus):
        self.__maritalStatus = maritalStatus
    
    @maritalStatus.deleter
    def maritalStatus(self):
        print("Marital Status Deleted.")
    
    @classmethod
    def show_count(cls):
        print(f'There are {cls.count} employees in {cls.company} company.')
    
    @classmethod
    def from_str(cls,s):
        title, name, age, maritalStatus = s.split(',')
        return cls(title, name, int(age), maritalStatus)
    
    @classmethod
    def from_dict(cls, d):
        return cls(d['title'], d['name'], d['age'], d['maritalStatus'])
    
# print(dir(p1))

p1 = Person("Mr.", "Bob", 21, "Single")
p2 = Person("Ms.", "Marry", 79, "Married")

print(type(p1))
print(type(p2))

print(id(p1))
print(id(p2))

#print(p1.name) # instance variables that are made private
# print(p2.age) # instance variables that are made private

p1.greet()
p2.greet()

print(p1.title)
print(p2.title)

title = f'{p1.title}Ted'
print(title)
p1.title = "Mrs."
title = f'{p1.title}Ted'
print(title)

p1.age = 25
p1.greet()

p1.age += 1
p1._display()

print(p1.fullname)
p1.maritalStatus = "Married"
del p1.maritalStatus

print(id(p1.company))
print(id(Person.company))
p1.count

Person.show_count()
p1.show_count()

s = "Mr., Jim, 23, Married"
p3 = Person.from_str(s)
p3._display()

d = {"title": "Mrs.", "name": "Jane", "age": 39, "maritalStatus": "Single"}
p4 = Person.from_dict(d)
p4._display()
Person.show_count()
p1.show_count()