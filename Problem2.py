#Problem2 : Write a program to accept marks of 6 students and display them in a sorted manner.


marks = []

for i in range(6):
    marks.append(int(input("Enter the marks: ")))

marks.sort()

print(marks)

    