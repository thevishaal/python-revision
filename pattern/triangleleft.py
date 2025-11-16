num = int(input("Enter a random number:"))
for i in range(1,num+2):
    for j in range(1, i):
        print("*", end=" ")
    print(" ")