# Prompt User Input with 'number' variable
number = int(input("Enter a number to see its multiplication table: "))
current_number = number

# 'for' loop condition
for number in range(1, 11):
    if current_number <= 10:
        product = number * current_number
        print(f"{current_number} * {number} = {product}")

