#1
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#4
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)