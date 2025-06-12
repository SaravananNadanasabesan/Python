# test_practical.py
# Author: Saravanan Nadanasabesan
# Date: 2025-12-06
# Description: This script manages user input for three departments, ensuring the total number of users does not exceed a maximum limit.

# Define constants
TOTAL_DEPARTMENTS = 3
MAX_TOTAL_USERS = 32

exit_choice = "no"
while exit_choice != "yes":

    # Ask user for input
    dept1_users = int(input("Enter the number of users in Department 1: "))
    dept2_users = int(input("Enter the number of users in Department 2: "))

    total_users_entered = dept1_users + dept2_users

    if total_users_entered > MAX_TOTAL_USERS:
        print("You have exceeded the maximum allowable users.")
    elif total_users_entered == MAX_TOTAL_USERS:
        print("There are no additional users allowed.")
    else:
        remaining_users = MAX_TOTAL_USERS - total_users_entered
        print(f"There are {remaining_users} users still available.")

    # Display users for each department
    remaining_for_dept3 = MAX_TOTAL_USERS - total_users_entered
    print(f"Department 1 users: {dept1_users}")
    print(f"Department 2 users: {dept2_users}")
    print(f"Department 3 available users: {remaining_for_dept3}")

    # Ask user if they want to exit
    exit_choice = input("Do you want to exit? (yes/no): ").strip().lower()

if exit_choice == "yes":
    print("Exiting the program. Goodbye!")