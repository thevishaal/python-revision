x = 1
y = 1
z = 1
n = 2
final = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k)!=2:
                li = [i,j,k]
                final.append(li)

print(final)
