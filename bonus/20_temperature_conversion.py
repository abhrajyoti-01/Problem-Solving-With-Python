print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter your choice (1/2): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C = {celsius * 9 / 5 + 32:.2f}°F")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}°F = {(fahrenheit - 32) * 5 / 9:.2f}°C")
else:
    print("Invalid choice.")
