"""
Program that implements a division calculator and robustly handles errors
such as division by zero and non-numeric inputs using command line arguments
"""

# Create 'safe_divide(numerator, denominator)' function
def safe_divide(numerator, denominator):
# ZeroDivisionError using 'try' except block
    try:
        result = float(numerator) / float(denominator)
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."

