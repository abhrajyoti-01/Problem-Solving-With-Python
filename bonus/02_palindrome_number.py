def is_palindrome_number(number):
    if number < 0:
        return False
    original = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return original == reversed_number


number = int(input("Enter a number to check: "))
if is_palindrome_number(number):
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")

start, end = map(int, input("Enter a range (start end) to list palindromes: ").split())
palindromes = [n for n in range(start, end + 1) if is_palindrome_number(n)]
print(f"Palindrome numbers between {start} and {end}: {palindromes}")
