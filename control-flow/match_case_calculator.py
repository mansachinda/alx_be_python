num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
type_of_operation = str(input("Choose the operation (+, -, *, /): "))

match type_of_operation:
    case "+":
        print(f"The result is {num1+num2}.")
    case "-":
        print(f"The result is {num1-num2}.")
    case "//":
        print(f"The result is {num1//num2}.")
    case "*":
        print(f"The result is {num1*num2}.")
    case "/":
        print(f"Cannot divide by zero.")
    case _:
        print(f"Push to start.")

