year = int(input("Enter a year: "))
print(f"{year} is {'a' if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else 'not a'} leap year.")
