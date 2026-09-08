principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest per year (%): "))
time = float(input("Enter time in years: "))

simple_interest = principal * rate * time / 100
print(f"Simple Interest: {simple_interest:.2f}")

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal
print(f"Compound Interest: {compound_interest:.2f}")
