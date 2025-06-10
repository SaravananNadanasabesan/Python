# Author: Saravanan Nadanasabesan
# Date: 2025-05-28
# Description: Defining a function that returns True if the number is a power of 2.

def is_power_of_two(number):
# Returns True if the number is a power of 2, otherwise False.
    if number <= 0:
        return False
    while number % 2 == 0:
        number //= 2
    return number == 1

# Testing the function
if __name__ == "__main__":
    test_values = [1, 2, 3, 8, 31, -8]
    for value in test_values:
        print(f"is_power_of_two({value}) = {is_power_of_two(value)}")
