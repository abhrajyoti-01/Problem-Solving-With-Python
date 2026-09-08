print("1. km -> miles")
print("2. miles -> km")
print("3. kg -> pounds")
print("4. pounds -> kg")
choice = input("Enter your choice (1-4): ")

if choice == "1":
    km = float(input("Enter distance in km: "))
    print(f"{km} km = {km * 0.621371:.2f} miles")
elif choice == "2":
    miles = float(input("Enter distance in miles: "))
    print(f"{miles} miles = {miles / 0.621371:.2f} km")
elif choice == "3":
    kg = float(input("Enter weight in kg: "))
    print(f"{kg} kg = {kg * 2.20462:.2f} pounds")
elif choice == "4":
    pounds = float(input("Enter weight in pounds: "))
    print(f"{pounds} pounds = {pounds / 2.20462:.2f} kg")
else:
    print("Invalid choice.")
