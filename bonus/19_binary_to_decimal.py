def binary_to_decimal(binary_string):
    if any(char not in "01" for char in binary_string):
        raise ValueError(f"'{binary_string}' is not a valid binary number.")
    decimal = 0
    for digit in binary_string:
        decimal = decimal * 2 + int(digit)
    return decimal


binary_string = input("Enter a binary number: ")
print(f"Binary {binary_string} -> Decimal {binary_to_decimal(binary_string)}")
