def search_student():
    roll = input("Enter Roll Number to Search: ")

    if roll in students:
        print("\n--- Student Found ---")
        print("Name   :", students[roll]["name"])
        print("Course :", students[roll]["course"])
        print("----------------------\n")
    else:
        print("\nStudent Not Found!\n")
