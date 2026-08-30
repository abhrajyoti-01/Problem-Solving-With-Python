try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    print(f"Division result = {first_number / second_number}")
except ValueError:
    print("Please enter numeric values only.")
except ZeroDivisionError:
    print("The second number cannot be zero.")
finally:
    print("Calculation attempt finished.")
