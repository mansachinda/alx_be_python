# Prompt for User Input with 'num1' and 'num2' variable
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = str(input("Choose the operation (+, -, *, /): "))

# Match Case condition 
match operation:
        case "+":
            result = num1+num2
            print(f"The result is {result}.")

        case "-":
            result = num1 - num2
            print(f"The result is {result}.")

        case "*":
            result = num1 * num2
            print(f"The result is {result}.")

        case "/":
            if num1 or num2 == 0:
                print(f"Cannot divide by zero.")

            result = num1 / num2
            print(f"The result is {result}.")

