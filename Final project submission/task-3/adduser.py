def add_user():
    username = input("Enter new username: ").strip().lower()
    real_name = input("Enter real name: ").strip()
    password = getpass.getpass("Enter password: ")
    encrypted_password = encrypt_password(password)

    USERS[username] = {'real_name': real_name, 'password': encrypted_password}

    print("User Created.")