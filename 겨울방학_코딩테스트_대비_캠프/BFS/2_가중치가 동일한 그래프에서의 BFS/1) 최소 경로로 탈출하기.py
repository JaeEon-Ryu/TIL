from collections import deque

n,m = map(int,input().split())
grid = []
for i in range(n):
    grid.append(list(map(int,input().split())))

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

step = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = 1
    q.append([x,y])

def BFS():

    while q:

        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
        x,y = q.popleft()

        for i in range(4):
            new_x,new_y = x + dx[i], y + dy[i]

            if can_go(new_x,new_y):
                push(new_x,new_y,step[x][y]+1)

q = deque()
push(0,0,0)
BFS()
if visited[-1][-1]:
    print(step[-1][-1])
else:
    print(-1)


