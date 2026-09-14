string = input("Enter a string: ")
reversed_string = string[::-1]
print(f"Reversed string: {reversed_string}")
print(f'"{string}" is {"a palindrome" if string == reversed_string else "not a palindrome"} string.')
