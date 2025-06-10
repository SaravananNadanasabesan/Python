# Author: Saravanan Nadanasabesan
# Date: 2025-05-28
# Description: Defining a function that returns True if the value is a positive number.

def is_positive(value):
# Return True if value is a positive number (int or float), else False.
    if isinstance(value, (int, float)):
        return value > 0
    return False

# Testing the function
if __name__ == "__main__":
    test_values = [10, -5, 0, 2.72, -0.01]
    for value in test_values:
        print(f"is_positive({value}) = {is_positive(value)}")
