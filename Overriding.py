# Python program to demonstrate
# method overriding


# Defining parent class
class Parent():

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)


# Defining child class
class Child(Parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()

# =================================================

# Python program to demonstrate
# overriding in multiple inheritance


# Defining parent class 1
class Parent1():

    # Parent's show method
    def show(self):
        print("Inside Parent1")


# Defining Parent class 2
class Parent2():

    # Parent's show method
    def display(self):
        print("Inside Parent2")


# Defining child class
class Child(Parent1, Parent2):

    # Child's show method
    def show(self):
        print("Inside Child")


# Driver's code
obj = Child()

obj.show()
obj.display()
