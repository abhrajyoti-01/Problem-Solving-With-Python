string = input("Enter a string: ")
duplicates = sorted({char for char in string if string.count(char) > 1})
print(f"Duplicate characters: {duplicates}" if duplicates else "No duplicate characters.")
