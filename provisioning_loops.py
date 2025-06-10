# Author: Saravanan Nadanasabesan
# Date: 2025-05-22
# Description: This program performs the basic cloud resource allocation.
# Gets the user input, validates it and then calculates the remaining resources.
# If the request exceeds the available resource, it is added to the pending list.
# otherwise, the request is accepted and resouces are allocated.
# The program uses list and loops to handle this process.

# Define two constants
TOTAL_NUMBER_OF_CPU_CORES_AVAILABLE = 24
TOTAL_AMOUNT_OF_MEMORY_GB_AVAILABLE = 12

# Track remaining resources
remaining_cpu_cores = TOTAL_NUMBER_OF_CPU_CORES_AVAILABLE
remaining_memory_gb = TOTAL_AMOUNT_OF_MEMORY_GB_AVAILABLE

# Create two empty lists
allocated_resources = list()
pending_requests = list()

# Loop control variable
is_continuing = "yes"

# Start loop for user input
while is_continuing.lower() == "yes":
    # Username input validation
    username = input("Enter username: ")
    while username.strip() == "":
        print("Username cannot be blank.")
        username = input("Enter username: ")
        
    # Input Validations of CPU cores and memory values
    cpu_cores = -1
    memory_gb = -1
    while cpu_cores < 0 or memory_gb < 0:
        cpu_cores = int(input("Enter required CPU cores: "))
        memory_gb = float(input("Enter required memory in GB: "))
        if cpu_cores < 0 or memory_gb < 0:
            print("Values must be non-negative. Please try again.")
        
    # Validate request
    if cpu_cores <= remaining_cpu_cores and memory_gb <= remaining_memory_gb:
        print("Resources provisioned successfully.")
        allocated_resources.append([username, cpu_cores, memory_gb])
        remaining_cpu_cores -= cpu_cores
        remaining_memory_gb -= memory_gb
    else:
        print("Resource request exceeds available capacity. Request pending.")
        pending_requests.append([username, cpu_cores, memory_gb])

    # Ask to continue
    is_continuing = input("Do you want to make another request? (yes/no): ")

# Display Allocated Resources
print("\n" + "*" * 50)
print("Allocated Resources:")
for record in allocated_resources:
    print("User:", record[0], "\tCPU cores:", record[1], "\tMemory (GB):", record[2])

# Display Pending Requests
print("\nPending Requests:")
for record in pending_requests:
    print("User:", record[0], "\tCPU cores:", record[1], "\tMemory (GB):", record[2])
