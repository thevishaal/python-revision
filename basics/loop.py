#loops - loops are used to repeat instructions

# count = 1
# while count <= 5:
#     print("hello")
#     count += 1

# i = 1
# while i <= 100:
#     # print(i)
#     i += 1

# n = int(input("Enter a number:"))
# i = 1 
# while i <= 10:
#     print(f"{n} X {i} = {n*i}")
#     print(i * i)
#     i += 1

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 36

# i = 0
# while i < len(tup):
#     if (tup[i] == x):
#         print(f"found at indx {i}")
        # break
#     else:
#         print("finding..")

#     i +=1

# i = 0 
# while i <=5:
#     if (i == 3):
#         i += 1
#         continue #skip
#     print(i)
#     i += 1

# nums = [1, 2, 3, 4, 5]

# for num in nums:
#     print(num)

# string = "vishalbaghel"

# for char in string:
#     if(char == 'a'):
#         print(f"{char} found")
#         break
#     print(char)
# else:
#     print("End")

#ques - print the elements of the following list using a loop:

# li = [1, 4, 16, 25, 36, 49, 64, 81, 100]

# x = 49    # linear search
# for l in li:
#     if(l == x):
#         print("found ", l)
#         break

# for i in range(100, 0, -1):
#     print(i)

# num = int(input("Enter a number:"))
# for i in range(1, 11):
#     print(f"{num} X {i} = {num * i}")

for i in range(5):
    #empty
    pass

num = int(input("Enter a number:"))

# Sum = 0
# i = 0
# while i <= num:
#     Sum += i
#     i += 1

# print(Sum)

fact = 1
for i in range(1, (num + 1)):
    fact *= i

print(fact)