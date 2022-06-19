c = {1,2,3,4}
b = {2,3,6}               

d = c.union(b)
print(d)

a = c.intersection(b)
print(a)

e = c.difference(b)
print(e)

f = c.difference_update((9,0))
print(f)