import os


if not os.path.exists("logs"):
    os.mkdir("logs")

with open("logs/log1.txt", "w", encoding="utf-8") as file_object:
    file_object.write("Log entry 1\n")
    file_object.write("Log entry 2\n")

print("logs directory created successfully.")
with open("logs/log1.txt", "r", encoding="utf-8") as file_object:
    print(file_object.read())
