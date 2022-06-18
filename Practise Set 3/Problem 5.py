name = input("Enter your name:\n")
dated = input("Enter selection dated:\n")

letter = '''Dear : {},
you are selected!
Dated {}'''.format(name,dated)

print(letter)

name = input("Enter your name:\n")
dated = input("Enter selection dated:\n")

letter = f'''Dear : {name},
you are selected!
Dated {dated}'''

print(letter)