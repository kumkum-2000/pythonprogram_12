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
    print("3. Exit")

def registration():
    print("\n--- Registration Form ---")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    users = load_data()
    new_user = {"name": name, "email": email, "phone": phone}
    users.append(new_user)
    save_data(users)

    print("\nRegistration Successful! Data saved in student.json")

def show_users():
    print("\n--- Registered Users ---")
    users = load_data()

    if not users:
        print("No users found!")
        return

    for index, user in enumerate(users, start=1):
        print(f"{index}. Name: {user['name']}, Email: {user['email']}, Phone: {user['phone']}")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        registration()
    elif choice == "2":
        show_users()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
