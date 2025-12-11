def register_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    students[roll] = {
        "name": name,
        "course": course
    }
    print("\nStudent Registered Successfully!\n")
