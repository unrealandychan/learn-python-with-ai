# Lesson 33: Working with Dates and Times (`datetime` module)

Working with dates and times is a common task in many programming applications, from scheduling events to logging data with timestamps. Python's built-in `datetime` module provides classes for working with dates, times, and durations.

## Key Classes in `datetime` Module

1.  **`date`:** Represents a date (year, month, day).
2.  **`time`:** Represents a time (hour, minute, second, microsecond).
3.  **`datetime`:** Represents a combination of a date and a time.
4.  **`timedelta`:** Represents a duration, the difference between two `date`, `time`, or `datetime` instances.

## 1. `datetime` Objects

To get the current date and time, you use `datetime.datetime.now()`.

**Example:**

```python
from datetime import datetime

# Get the current date and time
now = datetime.now()
print(f"Current datetime: {now}")

# Create a specific datetime object
# datetime(year, month, day, hour, minute, second, microsecond)
specific_datetime = datetime(2023, 7, 22, 10, 30, 0)
print(f"Specific datetime: {specific_datetime}")

# Accessing components
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")
```

## 2. `date` Objects

To work only with dates, you can use `datetime.date`.

**Example:**

```python
from datetime import date

# Get the current date
today = date.today()
print(f"Current date: {today}")

# Create a specific date object
specific_date = date(2024, 1, 1)
print(f"Specific date: {specific_date}")
```

## 3. `timedelta` Objects

`timedelta` objects represent a duration or a difference between two dates/times. They are useful for performing date arithmetic.

**Example:**

```python
from datetime import datetime, timedelta

now = datetime.now()

# Create a timedelta of 7 days
seven_days = timedelta(days=7)

# Calculate a date in the future
next_week = now + seven_days
print(f"Next week: {next_week}")

# Calculate a date in the past
last_week = now - seven_days
print(f"Last week: {last_week}")

# Calculate the difference between two datetimes
date1 = datetime(2023, 1, 1)
date2 = datetime(2023, 1, 15)
difference = date2 - date1
print(f"Difference: {difference}") # Output: 14 days, 0:00:00
print(f"Difference in days: {difference.days}") # Output: 14
```

## 4. Formatting Dates and Times (`strftime` and `strptime`)

*   **`strftime()` (string format time):** Converts a `datetime` object into a formatted string.
*   **`strptime()` (string parse time):** Parses a string into a `datetime` object.

These methods use format codes (e.g., `%Y` for year, `%m` for month, `%d` for day, `%H` for hour, `%M` for minute, `%S` for second).

**Example:**

```python
from datetime import datetime

now = datetime.now()

# Format datetime to string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date: {formatted_date}") # Output: 2023-07-22 10:30:00 (example)

formatted_date_short = now.strftime("%d/%m/%y")
print(f"Short format: {formatted_date_short}") # Output: 22/07/23 (example)

# Parse string to datetime object
date_string = "2024-03-15 14:30:00"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed datetime: {parsed_datetime}")

# Example of parsing a different format
date_string_alt = "10-25-2023"
parsed_alt = datetime.strptime(date_string_alt, "%m-%d-%Y")
print(f"Parsed alternative: {parsed_alt}")
```

Working with dates and times can be complex due to time zones, daylight saving, and different formats, but the `datetime` module provides robust tools to handle most scenarios.

--- 

### Quiz

1.  **How do you get the current date and time?**
    a) `datetime.current()`
    b) `datetime.now()`
    c) `datetime.today()`

2.  **What is `timedelta` used for?**
    a) To represent a specific point in time.
    b) To represent a duration of time.
    c) To format dates.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. b
</details>