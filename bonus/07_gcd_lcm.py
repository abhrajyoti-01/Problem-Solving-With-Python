def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


x, y = map(int, input("Enter two numbers: ").split())
print(f"GCD of {x} and {y} is {gcd(x, y)}")
print(f"LCM of {x} and {y} is {lcm(x, y)}")
