def decimal_to_binary(number):
    return ("-" if number < 0 else "") + bin(abs(number))[2:]


number = int(input("Enter a decimal number: "))
print(f"Decimal {number} -> Binary {decimal_to_binary(number)}")
