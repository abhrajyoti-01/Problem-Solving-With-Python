first_number = int(input("Enter the first integer: "))
second_number = int(input("Enter the second integer: "))

print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
print(f"{first_number} * {second_number} = {first_number * second_number}")

if second_number == 0:
    print("Division is not possible because the second number is zero.")
else:
    print(f"{first_number} / {second_number} = {first_number / second_number}")
