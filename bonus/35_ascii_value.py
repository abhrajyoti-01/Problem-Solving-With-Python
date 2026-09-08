char = input("Enter a character: ")
if char:
    print(f"ASCII value of '{char[0]}' is {ord(char[0])}")

code = int(input("Enter an ASCII code: "))
print(f"Character for ASCII {code} is '{chr(code)}'")

text = input("Enter a string to get ASCII values: ")
print("ASCII values:", {c: ord(c) for c in text})
