import uuid
import datetime
import json
all_student=[]

def Student_register():
    count=1
    for i in range(5):
        student={}
        date=datetime.datetime.now()
        print(f">>>>>>>Details of Student {i+1}<<<<<<<<<<<")
        student={
        "id":uuid.uuid4().hex[:13],
        "name":input("Enter Your Name: "),
        "date":date.strftime("%d/%m/%Y")
        }
        all_student.append(student)
        count+=1

    all_data=json.dumps(all_student, indent=5)

    print(all_data)

Student_register()