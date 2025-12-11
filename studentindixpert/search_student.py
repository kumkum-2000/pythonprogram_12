def search_st(students):
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Record Found: Name: {s['name']}, Roll: {s['roll']}, Qualification: {s['qualification']}, Year: {s['qualification_year']}\n")
            return
    print("No student found with this roll number.\n")