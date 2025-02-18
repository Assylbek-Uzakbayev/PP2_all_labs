from datetime import datetime ,timedelta
current = datetime.now()
new = current - timedelta(5)
print(new.strftime("%x"))