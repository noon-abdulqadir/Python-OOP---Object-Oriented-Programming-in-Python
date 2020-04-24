class Person():
    def display(self):
        print("I am a person.")
    def greet(self):
        print("Hello, how are you?")

p1 = Person()
p2 = Person()

print(type(p1))
print(type(p2))

print(id(p1))
print(id(p2))

p1.display()
p1.greet()

p2.display()
p2.greet()