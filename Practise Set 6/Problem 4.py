i = 1
while i<51:
    print(i)
    i += 1


fruits = ["banana", "mango", "orange", "applee"]
i = 0 
while i<len(fruits):
    print(fruits[i])
    i = i + 1 

fruits = ["banana", "mango", "orange", "applee"]
for item in fruits:
    print(item)
    print(i)   

for z in range(2,21,2):
    print(z)

for i in range(1,10):
    print(i)
else: 
    print("done")

for i in range(1,10):
    print(i)
    if i == 5:
        break
else: 
    print("done")

for i in range(2,10):
    print(i)
    if i == 5:
        continue
    print(i)
else: 
    print("done")

for i in range(10):
    if i == 1:
        continue
    print(i)