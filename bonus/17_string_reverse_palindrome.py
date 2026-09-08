string = input("Enter a string: ")
reversed_string = string[::-1]
print(f"Reversed string: {reversed_string}")

if string == reversed_string:
    print(f'"{string}" is a palindrome string.')
else:
    print(f'"{string}" is not a palindrome string.')
