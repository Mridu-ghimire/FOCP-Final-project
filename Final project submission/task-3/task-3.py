import getpass

USERS = {}

def encrypt_password(password):
    # Simple encryption for demonstration purposes
    return password[::-1]

def add_user():
    username = input("Enter new username: ").strip().lower()
    real_name = input("Enter real name: ").strip()
    password = getpass.getpass("Enter password: ")
    encrypted_password = encrypt_password(password)

    USERS[username] = {'real_name': real_name, 'password': encrypted_password}

    print("User Created.")

def delete_user():
    username = input("Enter username: ").strip().lower()

    if username in USERS:
        del USERS[username]
        print("User Deleted.")
    else:
        print("User not found.")

def change_password():
    username = input("User: ").strip().lower()

    if username in USERS:
        current_password = getpass.getpass("Current Password: ")
        if USERS[username]['password'] == encrypt_password(current_password):
            new_password = getpass.getpass("New Password: ")
            USERS[username]['password'] = encrypt_password(new_password)
            print("Password changed.")
        else:
            print("Invalid password. No change made.")
    else:
        print("User not found.")

def login():
    username = input("User: ").strip().lower()
    password = getpass.getpass("Password: ")

    if username in USERS and USERS[username]['password'] == encrypt_password(password):
        print(f"Welcome, {USERS[username]['real_name']}! Access granted.")
    else:
        print("Access denied.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add User")
        print("2. Delete User")
        print("3. Change Password")
        print("4. Login")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_user()
        elif choice == '2':
            delete_user()
        elif choice == '3':
            change_password()
        elif choice == '4':
            login()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()