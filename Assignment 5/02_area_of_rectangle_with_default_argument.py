length = float(input("Enter the length: "))
breadth_input = input("Enter the breadth (press Enter to use 1): ").strip()
breadth = float(breadth_input) if breadth_input else 1
print(f"Area of the rectangle = {length * breadth}")
