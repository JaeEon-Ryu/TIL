n, t = map(int, input().split())

convey1, convey2 = [], []
convey1 = list(map(int, input().split()))
convey2 = list(map(int, input().split()))

for _ in range(t):

    temp = convey1[n - 1]

    for i in range(n - 1, 0, -1):
        convey1[i] = convey1[i - 1]
    convey1[0] = convey2[n - 1]

    for i in range(n - 1, 0, -1):
        convey2[i] = convey2[i - 1]
    convey2[0] = temp

for i in range(n):
    print(convey1[i], end=' ')
print()
for i in range(n):
    print(convey2[i], end=' ')