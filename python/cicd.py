from datetime import datetime 
from datetime import timedelta
todays_date = datetime.now()

# to get hour from datetime
print('Hour: ', todays_date.hour)

# to get minute from datetime
print('Minute: ', todays_date.minute)



# datetime(year, month, day, hour, minute, second)
a = datetime.datetime(2017, 6, 21, 18, 25, 30)
b = datetime.datetime(2017, 5, 16, 8, 21, 10)

# returns a timedelta object
c = a-b
print('Difference: ', c)

minutes = c.total_seconds() / 60
print('Total difference in minutes: ', minutes)

# returns the difference of the time of the day
minutes = c.seconds / 60
print('Difference in minutes: ', minutes)
