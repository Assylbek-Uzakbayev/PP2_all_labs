from datetime import datetime , timedelta
yesterday = datetime.now() - timedelta(1)
print("Yesterday: "+ yesterday.strftime("%d/%m/%y"))

today = datetime.now()
print("Today: "+ today.strftime("%d/%m/%y"))

tommarow = datetime.now() + timedelta(1)
print("Today: " + tommarow.strftime("%d/%m/%y"))