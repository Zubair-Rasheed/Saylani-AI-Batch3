from tokenize import Name


dic = {
    "name" : "zubair",
    "f.name" : "Abdul Rasheed",
    "marks" : [3,23,2],
    'anotherdic' : { "sana" : "Zubair",
                    "sana loves me" : "No"
                    },
}

print(dic["name"])
print(dic["f.name"])
print(dic["marks"])
print(dic["anotherdic"]["sana"])
print(dic.items())
print(dic.keys())
print(dic.values())

from unicodedata import name


dict.fromkeys(['id','name'])

data = {}
data['id'] = input("Enter your id: ")
data['name'] = input("Enter your name: ")

print(data)