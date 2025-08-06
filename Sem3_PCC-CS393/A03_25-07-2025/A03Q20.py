day = int(input("Enter day number (1-7): "))
print("Weekend" if day in (6, 7) else "Weekday" if 1 <= day <= 5 else "Invalid day")
