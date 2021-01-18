import string

def in_range(x,y,n,m):
    return 0<=x and x<n and 0<=y and y<m

n, m = map(int,input().split())

grid = [[0 for i in range(m)] for j in range(n)]
dx,dy = [0,1,0,-1],[1,0,-1,0]
dir,num = 0, 1

x, y = 0, 0
while num < n*m+1:
    grid[x][y] = string.ascii_uppercase[(num-1)%26]
    num += 1

    new_x, new_y = x + dx[dir], y + dy[dir]
    if not in_range(new_x, new_y,n,m):
        dir += 1
    else:
        if grid[new_x][new_y] != 0:
            dir += 1
            dir %= 4

    x,y = x+dx[dir], y+dy[dir]

for i in range(n):
    for j in range(m):
        print(grid[i][j],end=' ')
    print()
