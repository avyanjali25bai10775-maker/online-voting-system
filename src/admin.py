from database import load_data, save_data

CANDIDATES_FILE = "data/votes.json"

# Admin password (simple)
ADMIN_PASSWORD = "admin123"

def admin_login():
    password = input("Enter admin password: ")
    if password == ADMIN_PASSWORD:
        print("Admin login successful!")
        return True
    else:
        print("Wrong password!")
        return False


def add_candidate():
    candidates = load_data(CANDIDATES_FILE)

    name = input("Enter candidate name: ")

    if name in candidates:
        print("Candidate already exists!")
        return

    candidates[name] = 0
    save_data(CANDIDATES_FILE, candidates)
    print("Candidate added successfully!")


def view_results():
    candidates = load_data(CANDIDATES_FILE)

    if not candidates:
        print("No candidates available.")
        return

    print("\n--- Voting Results ---")
    for name, votes in candidates.items():
        print(f"{name}: {votes} votes")
