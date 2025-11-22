from database import load_data, save_data

USERS_FILE = "data/users.json"

# Register a new user
def register_user():
    users = load_data(USERS_FILE)

    username = input("Enter username: ")
    if username in users:
        print("User already exists!")
        return

    password = input("Enter password: ")

    users[username] = {
        "password": password,
        "voted": False
    }

    save_data(USERS_FILE, users)
    print("Registration successful!")


# Login existing user
def login_user():
    users = load_data(USERS_FILE)

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username]["password"] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password!")
        return None
