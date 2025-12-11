from studentsdata import register_student
from studentsdata import search_student
from studentsdata import delete_student
def main_menu():
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

if __name__ == "__main__":
    main()