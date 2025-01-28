#1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#3
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#4
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#5
def myfunc(n):
  return abs(n - 50)

#6
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#7
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#8
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#9
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)