students = []

def register_student():
    print("\n--- Register Student ---")
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    qualification = input("Enter Qualification: ")
    qualification_year = input("Enter Qualification Year: ")

    student = {
        "name": name,
        "roll": roll,
        "qualification": qualification,
        "qualification_year": qualification_year
    }
    students.append(student)
    print("Student registered successfully!\n")


def view_students():
    print("\n--- All Student Records ---")
    if not students:
        print("No records found.\n")
        return
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Qualification: {s['qualification']}, Year: {s['qualification_year']}")
    print()

def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Record Found: Name: {s['name']}, Roll: {s['roll']}, Qualification: {s['qualification']}, Year: {s['qualification_year']}\n")
            return
    print("No student found with this roll number.\n")

def main_menu():
    while True:
        print("====== Student Management System ======")
        print("1. Register Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


main_menu()