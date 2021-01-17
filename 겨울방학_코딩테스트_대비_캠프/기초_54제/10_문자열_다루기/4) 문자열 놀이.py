s, q = input().split()
s = list(s)

for i in range(int(q)):
    target, a, b = input().split()

    if target == '1':
        a = int(a)
        b = int(b)
        s[a - 1], s[b - 1] = s[b - 1], s[a - 1]
    else:
        for j in range(len(s)):
            s[j] = s[j].replace(a, b)

    print(''.join(s))