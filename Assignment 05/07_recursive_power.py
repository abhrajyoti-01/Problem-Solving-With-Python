def power(base, exponent):
    if exponent == 0:
        return 1
    return 1 / power(base, -exponent) if exponent < 0 else base * power(base, exponent - 1)


base, exponent = 2.0, 5
print(f"{base} raised to the power {exponent} is {power(base, exponent)}")
