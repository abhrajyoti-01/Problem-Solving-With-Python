def decimal_to_binary(number):
    if number == 0:
        return "0"
    bits = []
    is_negative = number < 0
    number = abs(number)
    while number > 0:
        bits.append(str(number % 2))
        number //= 2
    binary = "".join(reversed(bits))
    return f"-{binary}" if is_negative else binary


number = int(input("Enter a decimal number: "))
print(f"Decimal {number} -> Binary {decimal_to_binary(number)}")
