def get_document(num):
    print(f"\nEnter details for Document {num}:")
    doc_image = input("Document Image Path: ")
    return {"name": doc_name,"image":doc_image}

student_package = {
    "student_id": input("Enter Student ID: "),
    "name": input("Enter Student Name: "),
    "address": input("Enter Address: "),
    "documents": []
}

for i in range(1, 4):
    student_package["documents"].append(get_document(i))

print("\n Final Student Package:")
print(student_package)
