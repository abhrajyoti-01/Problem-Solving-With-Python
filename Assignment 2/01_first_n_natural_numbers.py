count = int(input("Enter the value of N: "))
print("Please enter a positive integer." if count <= 0 else f"First {count} natural numbers:\n" + " ".join(map(str, range(1, count + 1))))
