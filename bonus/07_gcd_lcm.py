from math import gcd


x, y = map(int, input("Enter two numbers: ").split())
print(f"GCD of {x} and {y} is {gcd(x, y)}")
print(f"LCM of {x} and {y} is {x * y // gcd(x, y)}")
