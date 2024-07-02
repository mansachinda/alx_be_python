# Prompt User Input with 'number' variable
number = int(input("Enter a number to see its multiplication table: "))

# 'for' loop condition
for i in range(1, 11):
    X = number
    Y = i
    product = X * Y
    Z = product
    print(f"{X} * {Y} = {Z}")

