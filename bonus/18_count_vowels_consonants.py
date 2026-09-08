string = input("Enter a string: ")

vowels = consonants = digits = spaces = special = 0
for char in string:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
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
