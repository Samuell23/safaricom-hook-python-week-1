Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Basic Calculator Program
... 
... # Welcome message
... print("Welcome to the Basic Calculator Program!")
... 
... # Input: Get two numbers from the user
... try:
...     num1 = float(input("Enter the first number: "))
...     num2 = float(input("Enter the second number: "))
... except ValueError:
...     print("Invalid input! Please enter numeric values.")
...     exit()
... 
... # Input: Get the operation from the user
... print("Choose an operation: + for addition, - for subtraction, * for multiplication, / for division")
... operation = input("Enter the operation (+, -, *, /): ")
... 
... # Perform the operation and display the result
... if operation == "+":
...     result = num1 + num2
...     print(f"{num1} + {num2} = {result}")
... elif operation == "-":
...     result = num1 - num2
...     print(f"{num1} - {num2} = {result}")
... elif operation == "*":
...     result = num1 * num2
...     print(f"{num1} * {num2} = {result}")
... elif operation == "/":
...     if num2 != 0:  # Check for division by zero
...         result = num1 / num2
...         print(f"{num1} / {num2} = {result}")
...     else:
...         print("Error: Division by zero is not allowed.")
... else:
...     print("Invalid operation! Please choose +, -, *, or /.")
... 
... # Exit message
... print("Thank you for using the Basic Calculator Program!")
