import copy

n,m,r,c = map(int,input().split())
r,c = r-1, c-1
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dx,dy = [1,-1,0,0],[0,0,1,-1]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

# 폭탄 놓기
def drop_bombs(row, col, t):

    dist = 2**(t-1)
    for dir in range(4):
        new_x, new_y = row + dx[dir] * dist, col + dy[dir] * dist

        if in_range(new_x,new_y):
            grid[new_x][new_y] = 1

# 최초의 지점에 폭탄 놓기
grid[r][c] = 1

# 시간의 흐름에 따라 폭발이 연쇄적으로 일어날 수 있게끔 함
for result in range(1, m + 1):
    temp_grid = copy.deepcopy(grid)

    for i in range(n):
        for j in range(n):

            # 폭탄이 있는 곳으로부터 연쇄적인 폭발하기
            if temp_grid[i][j] == 1:
                drop_bombs(i, j, result)

# 폭탄의 개수 세기
result = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            result += 1

# 출력
print(result)

