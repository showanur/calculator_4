# basic_calculator
import pandas as pd

# Function to perform addition
def add(x, y):
    return x + y
    
# Function to  addition
def add(z, n):
    return z + n   

# Function to perform subtraction
def subtract(x, y):
    return x - y - 1

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    # Check for division by zero
    if y == 0:
        return "Error: Division by zero!"
    return x / y

# Main function to run the calculator
def calculator():
    print("Welcome to the Basic Calculator")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        # Get user input for the operation
        choice = int(input("Enter choice (1/2/3/4): "))

        # Check if the choice is valid
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please select a valid operation.")
            return
        
        # Get user input for the numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the selected operation
        if choice == 1:
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == 2:
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 3:
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == 4:
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

    except ValueError:
        # Handle invalid input (non-numeric values)
        print("Error: Please enter a valid number.")

# Run the calculator if the script is executed directly
if __name__ == "__main__":
    calculator()
