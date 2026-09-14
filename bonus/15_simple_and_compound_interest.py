principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest per year (%): "))
time = float(input("Enter time in years: "))

print(f"Simple Interest: {principal * rate * time / 100:.2f}")
print(f"Compound Interest: {principal * (1 + rate / 100) ** time - principal:.2f}")
