# Prompt User Input with 'rows' variable
rows = int(input("Enter the size of the pattern: "))

# 'while' loop condition will be executed first
while rows < 10:
    # 'for' loop will be executed within the 'while' loop
    for i in range(rows):
        # 'nested' 'for' loop will be executed within the 'outer' 'for' loop
        for j in range(rows):
            # Print all statement output in same line before moving to the next line
            print("*", end="")
        print()
        # Break Loop
    break

