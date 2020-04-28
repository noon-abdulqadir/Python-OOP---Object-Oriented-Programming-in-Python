class Mother:
    def cook(self):
        print('Can cook pasta')

 
class Father:
    def cook(self):
        print('Can cook noodles')

 
class Daughter(Father, Mother):
    pass

 
class Son(Mother, Father):
    def cook(self):
        super().cook()
        print('Can cook butter chicken') 

d = Daughter()  
s = Son()
 
d.cook()
print()
s.cook()


class Person:

    def greet(self):
        print('I am a Person')

 
class Teacher(Person):

    def greet(self):
        Person.greet(self)    
        print('I am a Teacher')

 
class Student(Person):

    def greet(self):
        Person.greet(self)    
        print('I am a Student')

 
class TeachingAssistant(Student, Teacher):

    def greet(self):
        super().greet()
        print('I am a Teaching Assistant')

       
x = TeachingAssistant()
x.greet()