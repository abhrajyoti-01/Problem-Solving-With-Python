user_input = 'abc'

try:
    number = int(user_input)
    print(f"You entered {number}.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
