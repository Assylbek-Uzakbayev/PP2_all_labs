#1
def greeting(name):
  print("Hello, " + name)


#2
import mymodule
mymodule.greeting("Jonathan")


#3
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}


#4
import mymodule
a = mymodule.person1["age"]
print(a)


#5
import mymodule as mx
a = mx.person1["age"]
print(a)


#6
import platform
x = platform.system()
print(x)


#7
import platform

x = dir(platform)
print(x)


#8
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}


