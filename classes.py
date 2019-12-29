# class is a cookie cutter for creating an object
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name # assign as properties to teh class
        self.email = email
        self.age = age

    def greetings(self):
        return "My name is "+ self.name + " and I am " + str(self.age) + " years old!"

    def has_birthday(self):
        self.age += 1
# new class customer, extends user
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name # assign as properties to teh class
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greetings(self): # example of inheritance, method override
        return "My name is "+ self.name + " and I am " + str(self.age) + " years old! Blance is " + str(self.balance)


#INit user object
brad = User('Brad Traversy', 'BT@gmail.com', 33)
janet = User('Janet Traversy', 'JT@gmail.com', 30)
# properties assigned to the object
print(brad.name)
print(brad.age)
# edit property
brad.age = 22
print(brad.age)
print(brad.greetings())
print(brad.has_birthday()) # call method on brad
print(brad.greetings())

# init customer
john = Customer('VIjay', 'vj@gmail.com', 33)
print(john.name)
john.set_balance(500)
print(john.greetings()) # john is a customer so response will be different
