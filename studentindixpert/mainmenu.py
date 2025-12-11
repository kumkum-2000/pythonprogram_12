import register_student
import search_student
import view_students
import delete_student
allstudent=[]
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
            allstudent=register_student()
        elif choice == "2":
            view_students.view_st(allstudent)
        elif choice == "3":
            search_student.search_st(allstudent)
        elif choice == "4":
            allstudent=delete_student.delete_(allstudentl)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")
main_menu()