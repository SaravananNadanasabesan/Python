# Author: Saravanan Nadanasabesan
# Date: 2025-05-22
# Description: Simulated cloud storage tracking system.
# Features:
# 1. Create a new account.
# 2. Delete an account.
# 3. Upload file.
# 4. List accounts.
# 5. Exit.


def create_account(usernames, storage_space):
    
# Creates a new account.
# Username must be unique and non-blank.
# Storage must be a positive number.
    
    username = input("Enter a username: ").strip()
    if not username:
        print("Username cannot be blank!")
        return

    if username in usernames:
        print("Username already exists. Choose another username.")
        return

    storage = input("Enter available storage (positive number): ").strip()
    if not storage.isdigit() or int(storage) <= 0:
        print("Invalid storage space. It must be a positive number.")
        return

    usernames.append(username)
    storage_space.append(int(storage))
    print(f"Account created for '{username}' with {storage} MB of storage.")
    

def delete_account(usernames, storage_space):
    
# Deletes an account by username.

    username = input("Enter the username to delete: ").strip()
    if username in usernames:
        index = usernames.index(username)
        del usernames[index]
        del storage_space[index]
        print(f"Account '{username}' has been deleted.")
    else:
        print("User not found. No account deleted.")
        

def upload_file(usernames, storage_space):

# Uploads a file for a given user if enough storage exists.

    username = input("Enter the username: ").strip()
    if username not in usernames:
        print("User not found.")
        return

    filename = input("Enter the filename: ").strip()
    filesize_input = input("Enter the filesize (positive number): ").strip()

    if not filesize_input.isdigit() or int(filesize_input) <= 0:
        print("Invalid filesize. It must be a positive number.")
        return

    filesize = int(filesize_input)
    index = usernames.index(username)

    if storage_space[index] >= filesize:
        storage_space[index] -= filesize
        print(f"File '{filename}' uploaded successfully for '{username}'.")
        print(f"Remaining storage: {storage_space[index]} MB.")
    else:
        print("Not enough storage to upload the file.")
        

def list_accounts(usernames, storage_space):
#  Lists all accounts and their available storage.

    if not usernames:
        print("No accounts to display.")
        return

    print("\nCurrent accounts:")
    for i in range(len(usernames)):
        print(f"- {usernames[i]}: {storage_space[i]} MB available")
        

def main():
    
# Main function to display the menu and handle user choices.
# Uses while choice != "5" to control the loop.

    usernames = []
    storage_space = []

# Initialize to something other than "5"
    choice = ""  

    while choice != "5":
        print("\nMenu:")
        print("1. Create a new account.")
        print("2. Delete an account.")
        print("3. Upload file.")
        print("4. List accounts.")
        print("5. Exit.")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            create_account(usernames, storage_space)
        elif choice == "2":
            delete_account(usernames, storage_space)
        elif choice == "3":
            upload_file(usernames, storage_space)
        elif choice == "4":
            list_accounts(usernames, storage_space)
        elif choice == "5":
            print("Exiting program. Goodbye!")
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Main method 
if __name__ == "__main__":
    main()
