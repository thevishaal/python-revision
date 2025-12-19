'''The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.'''

n = int(input("Enter number of studens:"))
students = {}

for _ in range(n):
    name = input("Name:")
    line = map(float, input().split())
    score = list(line)
    students[name] = score

query_name = input("Query:")

for key, value in students.items():
    if query_name == key:
        s = sum(students[query_name])

print("{:.2f}".format(s/len(students[query_name])))