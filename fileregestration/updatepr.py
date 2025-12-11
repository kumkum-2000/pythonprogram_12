import json
import os

FILE_NAME = "student.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def show_menu():
    print("\n===== MAIN MENU =====")
    print("1. Registration")
    print("2. Show All Registered Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Search User")
    print("6. Exit")

def registration():
    print("\n--- Registration Form ---")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    users = load_data()
    new_user = {"name": name, "email": email, "phone": phone}
    users.append(new_user)
    save_data(users)

    print("\nRegistration Successful!")

def show_users():
    print("\n--- Registered Users ---")
    users = load_data()

    if not users:
        print("No users found!")
        return

    for index, user in enumerate(users, start=1):
        print(f"{index}. Name: {user['name']}, Email: {user['email']}, Phone: {user['phone']}")

def update_user():
    users = load_data()
    if not users:
        print("No users found!")
        return

    show_users()
    index = int(input("Enter the serial number of the user to update: ")) - 1

    if 0 <= index < len(users):
        print("\n--- Update User ---")
        name = input(f"Enter new Name ({users[index]['name']}): ") or users[index]['name']
        email = input(f"Enter new Email ({users[index]['email']}): ") or users[index]['email']
        phone = input(f"Enter new Phone ({users[index]['phone']}): ") or users[index]['phone']

        users[index] = {"name": name, "email": email, "phone": phone}
        save_data(users)
        print("User updated successfully!")
    else:
        print("Invalid user number!")

def delete_user():
    users = load_data()
    if not users:
        print("No users found!")
        return

    show_users()
    index = int(input("Enter the serial number of the user to delete: ")) - 1

    if 0 <= index < len(users):
        deleted_user = users.pop(index)
        save_data(users)
        print(f"User {deleted_user['name']} deleted successfully!")
    else:
        print("Invalid user number!")

def search_user():
    users = load_data()
    if not users:
        print("No users found!")
        return

    query = input("Enter Name or Email to search: ").lower()
    found_users = [u for u in users if query in u['name'].lower() or query in u['email'].lower()]

    if found_users:
        print("\n--- Search Results ---")
        for user in found_users:
            print(f"Name: {user['name']}, Email: {user['email']}, Phone: {user['phone']}")
    else:
        print("No matching users found!")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        registration()
    elif choice == "2":
        show_users()
    elif choice == "3":
        update_user()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        search_user()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
