import os


if os.path.exists("logs/log1.txt"):
    os.remove("logs/log1.txt")
    print("log1.txt deleted successfully.")
else:
    print("log1.txt was not found.")

if os.path.exists("logs"):
    os.rmdir("logs")
    print("logs directory removed successfully.")
else:
    print("logs directory was not found.")
