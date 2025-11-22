from user import register_user, login_user
from admin import admin_login, add_candidate, view_results
from voting import cast_vote

def user_menu(username):
    while True:
        print("\n--- USER MENU ---")
        print("1. Cast Vote")
        print("2. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            cast_vote(username)
        elif choice == "2":
            print("Logged out!")
            break
        else:
            print("Invalid choice!")


def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Add Candidate")
        print("2. View Results")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            add_candidate()
        elif choice == "2":
            view_results()
        elif choice == "3":
            print("Admin logged out!")
            break
        else:
            print("Invalid choice!")


def main():
    while True:
        print("\n=== ONLINE VOTING SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. Admin Login")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_user()

        elif choice == "2":
            username = login_user()
            if username:
                user_menu(username)

        elif choice == "3":
            if admin_login():
                admin_menu()

        elif choice == "4":
            print("Thank you for using the Voting System!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
