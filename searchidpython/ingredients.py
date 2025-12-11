import json

def search_by_ingredient(response):
    ingredient_name=input("Enter ingredient name: ")
    for dict in response:
        if dict['ingredients']==None:
            continue
        else:
            dict['ingredients']==eningredient_nametered_id:
            print(dict)
    