# Author: Saravanan Nadanasabesan
# Date: 2025-05-28
# Description: Defining a function that sums the digits of the given value.

def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

# Testing the function
if __name__ == "__main__":
    test_values = [253, 110, -143, 999, 1234]
    for value in test_values:
        print(f"sum_of_digits({value}) = {sum_of_digits(value)}")
