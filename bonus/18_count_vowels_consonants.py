string = input("Enter a string: ")

vowels = consonants = digits = spaces = special = 0
for char in string:
    if char.isalpha():
        vowels += char.lower() in "aeiou"
        consonants += char.lower() not in "aeiou"
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special characters: {special}")
