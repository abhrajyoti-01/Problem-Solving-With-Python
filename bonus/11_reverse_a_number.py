def reverse_number(number):
    reversed_number = 0
    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number //= 10
    return reversed_number


number = int(input("Enter a number: "))
print(f"Reverse of {number} is {reverse_number(number)}")
