'''
7-2 문제와 풀이 방법이 비슷함
'''

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append([0 for j in range(m)])

val = 0

for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            arr[j][i] = val
            val += 1
    else:
        for j in range(n - 1, -1, -1):
            arr[j][i] = val
            val += 1

for row in arr:
    for c in row:
        print(c, end=' ')
    print()
