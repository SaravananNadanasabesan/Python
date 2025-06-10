# Author: Saravanan Nadanasabesan
# Date: 2025-05-22
# Description: This program checks whether user's resource request can be allocated.
# Based on the fixied limit of available cpu and memory.
# Gets the user input, validates it and then calculates the remaining resources.
# If the request exceeds the avaiable limit, then it displays the failure message.
# The program uses if-else statments to handle this process.

# Define two constants
TOTAL_NUMBER_OF_CPU_CORES_AVAILABLE = 16
TOTAL_AMOUNT_OF_MEMORY_GB_AVAILABLE = 8

# user input and validation of two values, stored in variables 
value1 = -1
value2 = -1
while value1 < 0 or value2 < 0:
    value1 = int(input("Enter the number of required CPU Cores = "))
    value2 = float(input("Enter the amount of required memory in GB = "))
    if value1 < 0 or value2 < 0:
        print("Values must be non-negative.Please try again")
            
# using if statement to check whether the required values entered by the user are available based on the limits defined as constants
if  (value1 <= TOTAL_NUMBER_OF_CPU_CORES_AVAILABLE and value2 <= TOTAL_AMOUNT_OF_MEMORY_GB_AVAILABLE):
    print('Resources provisioned successfully')
    remaining_available_cpu_cores = (TOTAL_NUMBER_OF_CPU_CORES_AVAILABLE - value1)
    remaining_available_memory = (TOTAL_AMOUNT_OF_MEMORY_GB_AVAILABLE - value2)

else:
    print('Resource request exceeds capacity. Provisioning failed')
    remaining_available_cpu_cores = (TOTAL_NUMBER_OF_CPU_CORES_AVAILABLE)
    remaining_available_memory = (TOTAL_AMOUNT_OF_MEMORY_GB_AVAILABLE)
    
# To caluculate the remaining CPU cores and memory
print("*"*50)
print("Total remaining available cpu cores:", remaining_available_cpu_cores)
print("Total remaining available memory:", remaining_available_memory)