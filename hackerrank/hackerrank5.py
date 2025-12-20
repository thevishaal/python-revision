n = int(input())

li = []
for _ in range(n):
    cmd, *value = input().split()
    value = list(map(int, value))

    if cmd =="append":
        for i in range(len(value)):
            li.append(value[i])

    elif cmd == 'print':
        print(li)

    elif cmd == 'remove':
        for i in range(len(value)):
            li.remove(value[i])

    elif cmd == 'pop':
        li.pop()

    elif cmd == 'reverse':
        li.sort(reverse = True)

    elif cmd == 'insert':
        li.insert(value[0], value[1])

    elif cmd == 'sort':
        li.sort()
