# Question 8
class Product():

    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self._discount = discount
    
    @property
    def selling_price(self):
        return self.marked_price - ((self.discount * self.marked_price) / 100)
    
    @property
    def discount(self):
        if self.marked_price > 500:
            print(f'Product price is over $500.\nNew discount in percentage: {self._discount + 2}%')
            return self._discount + 2
        else:
            return self._discount
 
    @discount.setter
    def discount(self, new_discount):
        self._discount = new_discount
    
    def display(self):
        print(f'Product ID: {self.id}\nProduct initial price: ${self.marked_price}\nDiscount in percentage: {self._discount}%\nPrice after discount: ${self.selling_price}')        
    
    
p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)

p3.display()
p3.selling_price