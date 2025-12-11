students = {} 

def register_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    students[roll] = {
        "name": name,
        "course": course
    }

    print("\nStudent Registered Successfully!\n")

def search_student():
    roll = input("Enter Roll Number to Search: ")

    if roll in students:
        print("\n--- Student Found ---")
        print("Name   :", students[roll]["name"])
        print("Course :", students[roll]["course"])
        print("----------------------\n")
    else:
        print("\nStudent Not Found!\n")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    if roll in students:
        del students[roll]
        print("\nStudent Deleted Successfully!\n")
    else:
        print("\nStudent Not Found!\n")

def main():
    while True:
        print("------ Student Management System ------")
        print("1. Register Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == '1':
            register_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("Exiting Program...")
            break
        else:
    
            print("Invalid Choice! Please Try Again.\n")
        # from studentsdata import menu
        # menu.main_menu()

if __name__ == "__main__":
    main()
