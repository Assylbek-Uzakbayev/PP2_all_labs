# 1
class StringManipulator:
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = input("Enter a string: ")
    
    def printString(self):
        print(self.text.upper())

# 2 
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length

# 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# 4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# 5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

# 6
nums = [10, 15, 17, 18, 19, 21, 23, 29]
prime_numbers = list(filter(lambda x: all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1)) and x > 1, nums))
print("Prime numbers:", prime_numbers)
