def greatest_no(n1,n2,n3):
    n1 = int(input("Enter your Number: "))
    n2 = int(input("Enter your Number: "))
    n3 = int(input("Enter your Number: "))
    if (n1>n2):
        if (n1>n3):
            return n1
        else:
            return n3
    else:
        if (n2>n3):
            return n2
        else:
            return n3
a = greatest_no(2,40,5)
print(a)

from webbrowser import get


def funt(a,b):
    return a+b
c = funt(3,4)
print(c)
