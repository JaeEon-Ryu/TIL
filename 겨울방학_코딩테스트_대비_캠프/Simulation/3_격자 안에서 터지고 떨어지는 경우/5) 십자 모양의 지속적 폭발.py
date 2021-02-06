n,m = map(int,input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

dx,dy = [1,-1,0,0],[0,0,-1,1]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def burst_grid(x, y):

    len_num = grid[x][y]

    # 선택한 곳 터트리기
    grid[x][y] = 0

    # 인접한 곳 터트리기
    for depth in range(1,len_num): # 깊이

        for dir in range(4): # 방향
            new_x,new_y = x+ dx[dir] * depth, y+dy[dir] * depth

            if in_range(new_x,new_y):
                grid[new_x][new_y] = 0

# temp_grid를 만들어서 0이 아닌 경우에만 값 복사하기
def clear_grid():

    temp_grid = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for j in range(n):
        temp_row = n-1

        for i in range(n-1,-1,-1):
            if grid[i][j] != 0:
                temp_grid[temp_row][j] = grid[i][j]
                temp_row -= 1

    return temp_grid



# m개의 줄에 걸쳐 폭탄 터트리기
for _ in range(m):

    target_column = int(input()) - 1

    for i in range(n):
        if grid[i][target_column] != 0:
            burst_grid(i,target_column)
            grid = clear_grid()
            break

# 출력
for i in range(n):
    for j in range(n):
        print(grid[i][j],end=' ')
    print()
