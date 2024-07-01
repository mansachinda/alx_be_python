# Prompt User Input with 'number' variable
number = int(input("Enter a number to see its multiplication table: "))
user_number = number

# 'for' loop condition
for number in range(1, 11):
    if user_number <= 10:
        product = number * user_number
        print(f"{user_number} * {number} = {product}")

