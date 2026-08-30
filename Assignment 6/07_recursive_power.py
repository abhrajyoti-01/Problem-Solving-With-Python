def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power(base, -exponent)
    return base * power(base, exponent - 1)


base = float(input("Enter the base value: "))
exponent = int(input("Enter the exponent: "))
print(f"{base} raised to the power {exponent} is {power(base, exponent)}")
