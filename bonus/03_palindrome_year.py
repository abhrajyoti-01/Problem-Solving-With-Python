def is_palindrome_year(year):
    return str(year) == str(year)[::-1]


def next_palindrome_year(year):
    year += 1
    while not is_palindrome_year(year):
        year += 1
    return year


year = int(input("Enter a year: "))
if is_palindrome_year(year):
    print(f"{year} is a palindrome year.")
else:
    print(f"{year} is not a palindrome year.")
    print(f"The next palindrome year after {year} is {next_palindrome_year(year)}.")

start, end = map(int, input("Enter a year range (start end): ").split())
print(f"Palindrome years between {start} and {end}: {[y for y in range(start, end + 1) if is_palindrome_year(y)]}")
