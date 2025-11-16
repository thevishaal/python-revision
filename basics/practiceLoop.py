import math
# q1
# for i in range(1,6):
#     print(i*i, end=" ")
#q2
# for i in range(1,11):
    # if(i%2 == 0):
    #     print(i, end=" ")
# q3
# s=0
# for i in range(1,11):
#    s += i
# print(s) 
#q4
# string = "Python"
# for i in range(len(string)-1,-1,-1):
#     print(string[i], end='')
# count = 0
# const = 0
# word = "education"
# for char in word:
#     v = "aeiou"
#     if (char in v):
#         count += 1
#     else:
#         const += 1 
# print(count)
# print(const)

#fibonacci
# a = 0
# b = 1
# print(a, b, end=" ")

# for _ in range(10):
#     next_term = a + b
#     print(next_term , end= " ")
#     a, b = b, next_term

#factorial

# fact = 1
# for i in range(1,11):
#     fact *= i
# print(fact)

#prime or not 
# num = 25
# is_prime = True

# for i in range(2, int(num ** 0.5)+1):
#     if (num % i == 0):
#         is_prime = False
#         break

# if is_prime and num>1:
#     print(num , "is a prime number")
# else:
#     print("not a prime number")

#coun occurences of Each character in a string 
# word = "programming"
# d = {}
# for char in word:
#     if char in d:
#         d[char] += 1
#     else: 
#         d[char] = 1
# for char, count in d.items():
#     print(char + ":", count)

word = "pythonLanguage"
dictionary = {}
for char in word:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

for char, count in dictionary.items():
    print(char + ":" , count)