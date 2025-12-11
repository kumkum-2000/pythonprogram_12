from searchidpython import *

import requests
import json

response=requests.get("https://share.google/images/KMLm2V85Sd9LKLOEy")
print(json.dumps(response.json(),indent=4))
response=response.json()

while True:
    print("1. search by id")
    print("2. search by name")
    print("3. exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        search_by_id(response)
    elif choice==2:
        search_by_ingredient(response)
    elif choice==3:
        break
    else:
        print(f"{choice} is invalid choice")
