import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
"""
0 - Monday
1 - Tuesday
...
"""
print(day_of_week)

day_of_birth = dt.datetime(year=1983, month=11, day=17)
print(day_of_birth)