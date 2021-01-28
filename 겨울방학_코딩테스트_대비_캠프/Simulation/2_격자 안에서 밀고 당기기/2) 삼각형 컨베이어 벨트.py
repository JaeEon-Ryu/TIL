n,t = map(int,input().split())
triangle = [
    list(map(int,input().split()))
    for _ in range(3)
]

for _ in range(t):
    side_1 = [triangle[2][-1]] + triangle[0][:n-1]
    side_2 = [triangle[0][-1]] + triangle[1][:n-1]
    side_3 = [triangle[1][-1]] + triangle[2][:n-1]

    triangle[0] = side_1
    triangle[1] = side_2
    triangle[2] = side_3

for i in range(3):
    for j in range(n):
        print(triangle[i][j],end=' ')
    print()