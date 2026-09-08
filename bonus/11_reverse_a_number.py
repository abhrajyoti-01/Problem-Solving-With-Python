def reverse_number(number):
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return reversed_number


number = int(input("Enter a number: "))
print(f"Reverse of {number} is {reverse_number(number)}")
