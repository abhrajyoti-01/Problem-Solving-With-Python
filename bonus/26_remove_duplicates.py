string = input("Enter a string: ")

if len(string) != len(set(string)):
    duplicates = sorted({char for char in string if string.count(char) > 1})
    print(f"Duplicate characters: {duplicates}")
else:
    print("No duplicate characters.")
