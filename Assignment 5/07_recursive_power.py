def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power(base, -exponent)
    return base * power(base, exponent - 1)


base = 2.0
exponent = 5
print(f"{base} raised to the power {exponent} is {power(base, exponent)}")
