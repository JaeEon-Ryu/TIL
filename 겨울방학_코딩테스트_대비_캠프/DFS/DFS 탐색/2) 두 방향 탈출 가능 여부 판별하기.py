n,m = map(int,input().split())
grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def DFS(x,y):
    dx,dy = [1,0],[0,1]

    for i in range(2):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if can_go(new_x,new_y):
            visited[new_x][new_y] = 1
            DFS(new_x,new_y)

visited[0][0] = 1
DFS(0,0)

print(visited[-1][-1])