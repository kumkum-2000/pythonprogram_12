def delete_(allstudent):
    name = input("Enter name: ")
    for i in range(len(allstudent)):
        if allstudent[i]["name"].lower() == name.lower():
            print(f"\nName {allstudent[i]['name']} Deleted Successfully")
            del allstudent[i]
            break
    return allstudent
 
