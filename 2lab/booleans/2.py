bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#2
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#3 
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))