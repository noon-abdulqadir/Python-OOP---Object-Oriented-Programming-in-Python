class Employee:
    domains = set()
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}

    def __init__(self, name, email):
        self.name = name
        self.email = email
        print(self.email)
        Employee.domains.add(str(email.split('@')[1]))
        print(Employee.domains)
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        domain = str(new_email.split('@')[1])
        if domain in Employee.allowed_domains:
            self._email = new_email
        elif domain not in Employee.allowed_domains:
            raise RuntimeError(f"Domain {domain} is not allowed.")
    
    def display(self):
        print(self.name, self.email)
            
e1 = Employee('John', 'john@gmail.com')
e2 = Employee('Jack', 'jack@yahoo.com')
e3 = Employee('Jill', 'jill@outlook.com')
e4 = Employee('Ted', 'ted@yahoo.com')
e5 = Employee('Tim', 'tim@gmail.com')
e6 = Employee('Mike', 'mike@yahoo.com')
e7 = Employee('Noon', 'noon@xyz.com')