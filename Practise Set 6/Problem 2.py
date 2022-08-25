a = int(input("Enter your number:\n"))
b = int(input("Enter your number:\n"))
c = int(input("Enter your number:\n"))
d = int(input("Enter your number:\n"))

if a>b:
    f1 = a
else:
    f1 = b
if c>d:
    f2 = c
else:
    f2 = d
if f1>f2:
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")
