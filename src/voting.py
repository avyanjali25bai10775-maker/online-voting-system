from database import load_data, save_data
from user import register_user, login_user

USERS_FILE = "data/users.json"
CANDIDATES_FILE = "data/votes.json"


def cast_vote(username):
    users = load_data(USERS_FILE)

    # Check if user already voted
    if users[username]["voted"]:
        print("You have already voted!")
        return

    candidates = load_data(CANDIDATES_FILE)

    if not candidates:
        print("No candidates available to vote for.")
        return

    print("\n--- Candidates ---")
    for i, name in enumerate(candidates.keys(), start=1):
        print(f"{i}. {name}")

    choice = int(input("\nEnter candidate number: "))
    candidate_list = list(candidates.keys())

    if choice < 1 or choice > len(candidate_list):
        print("Invalid choice!")
        return

    selected = candidate_list[choice - 1]
    candidates[selected] += 1

    # Mark user as voted
    users[username]["voted"] = True

    save_data(CANDIDATES_FILE, candidates)
    save_data(USERS_FILE, users)

    print(f"You voted for {selected}!")
