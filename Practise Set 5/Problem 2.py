# dict.fromkeys(["id","name","father_name","class"])

# data = {}
# data['id'] = input("Enter your id:\n")
# data['name'] = input("Enter your name:\n")
# data['father_name'] = input("Enter your father name:\n")
# data['class'] = input("Enter your class:\n")

# print(data)
# print(type(data))

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
# print(dic.items())
# print(dic.keys())
# print(dic.values())
print(dic)
dic1 = {
    "my life" : "sana",
    "she hates" : "zubair"    
}
dic.update(dic1)
print(dic)
print(dic.get('name'))
print(dic["anotherdic"])