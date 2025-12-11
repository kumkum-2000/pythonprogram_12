import json

def registration():
    print("\n--- Registration Form ---")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    user_data = {
        "name": name,
        "email": email,
        "phone": phone
    }
    try:
        with open("users.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = [] 


    data.append(user_data)

    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)

    print("\nRegistration Successful! Data saved in users.json")
