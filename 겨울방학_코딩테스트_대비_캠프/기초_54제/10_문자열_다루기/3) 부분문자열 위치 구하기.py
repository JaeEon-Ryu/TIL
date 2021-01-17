string = input()
target = input()

if target not in string:
    print(-1)
else:
    print(string.index(target))