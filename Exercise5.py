# Question 10
class Circle:
    def __init__(self,radius):
        self.radius = radius
            
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self,new_radius):
        if new_radius < 0:
            print("Negative radius values will be transformed to positive.")
            x = input("If that is fine with you, types YES: ")
            if x.upper() == "YES":
                new_radius = abs(new_radius)
            else:
                raise(ValueError("Radius values must be positive."))
        else:
            new_radius
        self._radius = new_radius
    
    def area(self):
        return (self.radius**2) * 3.14
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def circumference(self):
        return self.diameter * 3.14
    
    def display(self):
        print(f'Circle radius: {self.radius}\nCircle area: {self.area()}\nCircle diameter: {self.diameter}\nCircle circumference: {self.circumference}')


c1 = Circle(-5)
c1.display()