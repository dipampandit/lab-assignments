# 1. Write a Python program to get the current date and time.
from datetime import datetime, timedelta, timezone
import calendar

print(datetime.now())

# 2. Create a function that returns the current year, month, and day separately.
def current_ymd():
    now = datetime.now()
    return now.year, now.month, now.day
print(current_ymd())

# 3. Write a program to display the current date in the format YYYY-MM-DD.
print(datetime.now().strftime("%Y-%m-%d"))

# 4. Write a function that takes a date string and returns the day of the week.
def get_weekday(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%A")
print(get_weekday("2023-10-15"))

# 5. Develop a program that calculates the number of days between two given dates.
d1 = datetime(2023, 1, 1)
d2 = datetime(2023, 3, 1)
print((d2 - d1).days)

# 6. Create a function that adds a specified number of days to a given date and returns the new date.
def add_days(date_str, days):
    return (datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=days)).date()
print(add_days("2023-10-10", 5))

# 7. Write a Python function to find the date of the next Monday after a given date.
def next_monday(date_str):
    d = datetime.strptime(date_str, "%Y-%m-%d")
    return (d + timedelta(days=(7 - d.weekday()))).date()
print(next_monday("2023-10-10"))

# 8. Design a program to calculate the number of seconds between two datetime objects.
dt1 = datetime(2023, 1, 1, 12, 0)
dt2 = datetime(2023, 1, 2, 12, 0)
print((dt2 - dt1).total_seconds())

# 9. Write a function to return the time difference (in hours and minutes) between now and a specified time.
def diff_from_now(t):
    now = datetime.now()
    h, m = t.split(":")
    target = now.replace(hour=int(h), minute=int(m))
    diff = abs(now - target)
    return diff.seconds // 3600, (diff.seconds % 3600) // 60
print(diff_from_now("14:30"))

# 10. Create a program that converts a given timestamp to a readable date format.
ts = 1700000000
print(datetime.fromtimestamp(ts))

# 11. Write a function that checks if a given date falls on a weekend.
def is_weekend(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").weekday() >= 5
print(is_weekend("2023-10-14"))

# 12. Write a Python program to calculate the number of leap years between two years.
def leap_count(y1, y2):
    return sum(calendar.isleap(y) for y in range(y1, y2+1))
print(leap_count(2000, 2024))

# 13. Develop a function that lists all dates between a start and end date.
def list_dates(s, e):
    start = datetime.strptime(s, "%Y-%m-%d")
    end = datetime.strptime(e, "%Y-%m-%d")
    return [(start + timedelta(days=i)).date() for i in range((end-start).days+1)]
print(list_dates("2023-10-01", "2023-10-05"))

# 14. Write a program that displays the last day of the current month.
now = datetime.now()
print(calendar.monthrange(now.year, now.month)[1])

# 15. Create a function that converts DD-MM-YYYY to YYYY-MM-DD.
def convert_date(s):
    return datetime.strptime(s, "%d-%m-%Y").strftime("%Y-%m-%d")
print(convert_date("15-10-2023"))

# 16. Write a program to find the week number of a given date.
print(datetime.strptime("2023-10-15", "%Y-%m-%d").isocalendar().week)

# 17. Write a Python function to calculate age from date of birth.
def age(dob):
    d = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.now()
    return today.year - d.year - ((today.month, today.day) < (d.month, d.day))
print(age("2004-06-15"))

# 18. Design a program to display current UTC date and time with timezone offset.
utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_now)

# 19. Write a function to determine days left until a specific holiday.
def days_to(date_str):
    target = datetime.strptime(date_str, "%Y-%m-%d")
    return (target - datetime.now()).days
print(days_to("2026-01-01"))

# 20. Format datetime as “Day, Month Date, Year Time”.
def fmt(dt):
    return dt.strftime("%A, %B %d, %Y %H:%M")
print(fmt(datetime(2024, 6, 30, 15, 45)))

# 21. Write a function that calculates business days between two dates.
def business_days(s, e):
    start = datetime.strptime(s, "%Y-%m-%d")
    end = datetime.strptime(e, "%Y-%m-%d")
    return sum((start + timedelta(days=i)).weekday() < 5 for i in range((end-start).days+1))
print(business_days("2023-10-01", "2023-10-10"))

# 22. Generate all Fridays within the next month from a start date.
def fridays_next_month(start_str):
    start = datetime.strptime(start_str, "%Y-%m-%d")
    next_month = start.replace(day=1) + timedelta(days=32)
    first = next_month.replace(day=1)
    last = calendar.monthrange(first.year, first.month)[1]
    return [first.replace(day=d).date() for d in range(1, last+1) if first.replace(day=d).weekday() == 4]
print(fridays_next_month("2023-10-10"))

# 23. Convert 24-hour time to 12-hour format.
def to_12(t):
    return datetime.strptime(t, "%H:%M").strftime("%I:%M %p")
print(to_12("14:30"))

# 24. Round a timestamp to nearest hour.
ts = datetime(2023, 10, 10, 14, 20)
print((ts + timedelta(minutes=30)).replace(minute=0, second=0))

# 25. Find date one month from now, handling month lengths.
def add_month(dt):
    m = dt.month + 1
    y = dt.year + (m > 12)
    m = m if m <= 12 else m - 12
    d = min(dt.day, calendar.monthrange(y, m)[1])
    return datetime(y, m, d)
print(add_month(datetime.now()))

# 26. Return all dates that fall on the 15th in a year.
def fifteenths(year):
    return [datetime(year, m, 15).date() for m in range(1, 12+1)]
print(fifteenths(2025))

# 27. Determine whether a given datetime is past or future.
def past_or_future(dt):
    return "past" if dt < datetime.now() else "future"
print(past_or_future(datetime(2026, 1, 1)))

# 28. Format datetime in ISO 8601.
print(datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))

# 29. Convert UTC datetime to another timezone offset (manual).
def convert_timezone(dt, offset_hours):
    return dt + timedelta(hours=offset_hours)
print(convert_timezone(datetime.utcnow(), 5.5))

# 30. Add or subtract time from a datetime.
def adjust(dt, h=0, m=0, s=0):
    return dt + timedelta(hours=h, minutes=m, seconds=s)
print(adjust(datetime(2023, 10, 10, 10, 0), h=2))
