num = int(input("Enter your number:\n"))

if num%2 == 0:
    print("Even")
else:
    print("Odd")


num = int(input("Enter your number:\n"))

if num%2 == 0:
    print(f"The value of {num} is Even")
else:
    print(f"The value of {num} is Odd")


a = 20
b = 30
c = 40

(a%2==0) or (b%2==0) and (c%2==0)
