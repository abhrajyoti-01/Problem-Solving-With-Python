def is_palindrome_number(number):
    return number >= 0 and number == int(str(number)[::-1])


number = int(input("Enter a number to check: "))
print(f"{number} is {'a palindrome' if is_palindrome_number(number) else 'not a palindrome'} number.")

start, end = map(int, input("Enter a range (start end) to list palindromes: ").split())
print(f"Palindrome numbers between {start} and {end}: {[n for n in range(start, end + 1) if is_palindrome_number(n)]}")
