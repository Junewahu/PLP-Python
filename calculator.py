# Ask the user to input the first number
num1 = float(input("Enter the first number: "))

# Ask the user to input the second number
num2 = float(input("Enter the second number: "))

# Ask the user to input the operation they want to perform
operation = input("Enter the operation (+, -, *, /): ")

# Initialize a variable to store the result
result = None

# Check which operation was entered and perform the corresponding calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Check if the second number is not zero to avoid division by zero error
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation entered.")

    # If a valid result was calculated, print it
if result is not None:
    print(f"{num1} {operation} {num2} = {result}")