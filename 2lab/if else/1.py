#1
a = 33
b = 200
if b > a:
  print("b is greater than a")

#2
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#3
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#4
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#5
if a > b: print("a is greater than b")

#6
a = 2
b = 330
print("A") if a > b else print("B")

#7
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#8
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#9
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#10
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#11
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#12
a = 33
b = 200

if b > a:
  pass







