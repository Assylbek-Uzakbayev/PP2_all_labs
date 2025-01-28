#1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

#2
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#3
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

#4
newlist = [x for x in fruits if "a" in x]
print(newlist)

#5
newlist = [x for x in fruits if x != "apple"]

#6
newlist = [x for x in fruits]

#7
newlist = [x for x in range(10)]

#8
newlist = [x for x in range(10) if x < 5]

#9
newlist = ['hello' for x in fruits]

#10
newlist = [x if x != "banana" else "orange" for x in fruits]

























