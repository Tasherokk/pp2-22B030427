import datetime

d1 = datetime.date.today()
d2 = d1 - datetime.timedelta(days = 1)
d3 = d1 + datetime.timedelta(days = 1)

print(d1)
print(d2)
print(d3)
