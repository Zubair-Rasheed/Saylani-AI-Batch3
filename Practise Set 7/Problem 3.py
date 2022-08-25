def fac_rec(n):
    if n == 1 or n == 0:
        return 1
    return n * fac_rec(n-1)
a = fac_rec(int(input("Enter your num: ")))
print(a)