# a = {1,2,3,4,5}         #set

# print(type(a))

# b = {}                  #dict
# print(type(b))

# c = set()               #empty set
# print(type(c))

c = set()               
print(type(c))

c.add(1)
c.add(2)
c.add(3)
c.add((1,2,3))
print(c)
c.remove(2)
print(c)
print(len(c))
print(c.pop())