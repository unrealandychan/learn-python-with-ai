
# Lesson 33: Solution

from datetime import datetime, timedelta

now = datetime.now()
print("Current date and time:", now)

hundred_days = timedelta(days=100)
future_date = now + hundred_days
print("Date in 100 days:", future_date)

date_string = "2023-01-01"
date_object = datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed date object:", date_object)
