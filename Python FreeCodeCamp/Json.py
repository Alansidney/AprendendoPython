import json
data = '''{
    "name" : "Alan",
    "phone" : {
        "type" : "intl",
        "number" : "+55 81 98543 6465"
        },
    "email" : {
        "hide": "yes"
    }
}'''

info = json.loads(data)
print ('Name: ', info["name"])
print ('Hide: ',info["email"]["hide"])
print ('Phone: ', info["phone"]["number"])

listOfJson = '''[
    {
        "id" : "1",
        "name" : "André",
        "age" : "22"
    },
    {
        "id" : "2",
        "name" : "Diogo",
        "age" : "22"
    }
]'''

info2 = json.loads(listOfJson)
print ('# of Users:', len(info2))
for item in info2:
    print('Id: ', item['id'])
    print('Name: ', item['name'])
    print('Age: ', item['age'])
