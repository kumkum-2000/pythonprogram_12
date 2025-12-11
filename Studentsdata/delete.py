def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    if roll in students:
        del students[roll]
        print("\nStudent Deleted Successfully!\n")
    else:
        print("\nStudent Not Found!\n")