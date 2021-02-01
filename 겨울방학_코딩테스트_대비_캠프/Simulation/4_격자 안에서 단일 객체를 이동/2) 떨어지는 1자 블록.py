'''
k번째 열 부터 k + m - 1 번째 열까지의 공간을 차지함
'''

n, m, k = map(int,input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

def can_go(x,y):
    new_x = x + 1
    return new_x < n and grid[new_x][y] == 0

dropped_position = 0
break_point = False

# 떨어지는 것이 멈출때까지 반복
for i in range(n):
    for j in range(n):

        if k-1 <= j <= k+m-2:
            if not can_go(i,j):
                dropped_position = i
                break_point = True
                break

    if break_point:
        break

# 떨어진 위치 활성화
for j in range(n):
    if k-1 <= j <= k+m-2:
        grid[dropped_position][j] = 1

# 출력
for i in range(n):
    for j in range(n):
        print(grid[i][j],end=' ')
    print()