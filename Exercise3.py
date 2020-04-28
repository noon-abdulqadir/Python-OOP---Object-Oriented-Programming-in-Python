# Question 6
class Fraction:
    
    def __init__(self, nr, dr = 1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1
    
    def show(self):
        print(f'{self.nr}/{self.dr}')
    
    def __str__(self):
        return(f'{self.nr}/{self.dr}')
    
    def __repr__(self):
        return(f'Fraction({self.nr}/{self.dr})')
    
    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return(f)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __iadd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr - other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return(f)
    
    def __rsub__(self, other):
        return self.__sub__(other)
    
    def __isub__(self, other):
        return self.__sub__(other)
    
    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.nr , self.dr * other.dr)
        f._reduce()
        return(f)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __imul__(self, other):
        return self.__mul__(other)
    
    def __eq__(self, other):
        return (self.nr * other.dr) == (self.dr * other.nr)
    
    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s
    
    def _reduce(self):
        h = Fraction.hcf(self.nr, self.dr)
        if h == 0:
            return
        self.nr //= h
        self.dr //= h


f1 = Fraction(2, 3)
f1.show()
f2 = Fraction(3, 4)
f2.show()
f3 = f1.__mul__(f2)
f3.show()
f3 = f1.__add__(f2)
f3.show()
f3 = f1.__add__(5) 
f3.show()
f3 = f1.__mul__(5) 
f3.show()
f3 = f1 + f2
f3.show()
f3 = f1 - f2
f3.show()
f3 = f1 * f2
f3.show()
print(f1)
str(f1)
lst = [f1, f2, f3]
print(lst)