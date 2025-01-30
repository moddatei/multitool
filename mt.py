import os
import subprocess

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def open_file(file_path):
    try:
        os.startfile(file_path)  # For Windows
    except Exception as e:
        print(f"Error opening file: {e}")

def open_browser(url):
    try:
        subprocess.run(['start', url], shell=True)  # For Windows
    except Exception as e:
        print(f"Error opening browser: {e}")

def open_directory(directory_path):
    try:
        os.startfile(directory_path)  # For Windows
    except Exception as e:
        print(f"Error opening directory: {e}")

def main():
    print("Welcome to the Multi-Tool!")
    print("Select operation:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            print(f"You selected option {choice}.")
        else:
            print("Invalid input")

        next_action = input("Do you want to perform another action? (yes/no): ")
        if next_action.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
