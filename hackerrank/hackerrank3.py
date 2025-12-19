'''Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''

n = int(input("Enter number of students:"))
records = []
marks = []

for _ in range(n):
    name = input("Name:")
    score = int(input("Score:"))
    marks.append(score)
    records.append([name, score])

marks.sort()
lowest_score = marks[0]
second_score = 0

for i in marks:
    if i > lowest_score:
        second_score = i
        break

names = []

for d in records:
    if d[1] == second_score:
        names.append(d[0])

names.sort()

for n in names:
    print(n)