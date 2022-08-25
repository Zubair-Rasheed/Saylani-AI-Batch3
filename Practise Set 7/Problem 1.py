def percentage(students):
    p = ((students[0]+students[1]+students[2]+students[3]+students[4])/500)*100
    return p


student_1 = [34, 56, 76, 34, 23]
per1 = percentage(student_1)
print(per1)

student_2 = [23,96,87,85,89]
per2 = percentage(student_2)
print(per2)



student_1 = [34, 56, 76, 99, 23]
perc = ((student_1[0]+student_1[1]+student_1[2]+student_1[3]+student_1[4])/500)*100
print(perc)

student_2 = [23,36,77,55,34]
perc1 = ((student_2[0]+student_2[1]+student_2[2]+student_2[3]+student_2[4])/500)*100
print(perc1)