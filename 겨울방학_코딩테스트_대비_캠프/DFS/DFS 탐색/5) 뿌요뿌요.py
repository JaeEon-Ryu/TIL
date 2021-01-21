
n = int(input())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num_of_bursted = 0
global size_of_block
size_of_block = 1
global curr_num

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def can_go(x,y):
    global curr_num

    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] != curr_num:
        return False
    return True

def DFS(x,y):
    global size_of_block
    dx,dy = [1,-1,0,0],[0,0,1,-1]

    for i in range(4): # 방향조절
        new_x, new_y = x+dx[i], y+dy[i]

        if can_go(new_x,new_y):
            size_of_block += 1
            visited[new_x][new_y] = 1
            DFS(new_x,new_y)


max_size = 1
for i in range(n):
    for j in range(n):

        if visited[i][j] == 0: # 방문하지 않았을때만 DFS동작
            visited[i][j] = 1
            curr_num = grid[i][j]
            DFS(i,j)

            if size_of_block >= 4:
                num_of_bursted += 1

            if max_size < size_of_block:
                max_size = size_of_block

            size_of_block = 1 # 블럭 크기 초기화

print(num_of_bursted,max_size)


