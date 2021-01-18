import sys

def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n

n = int(input())
if n == 1:
    print(1)
    sys.exit()

grid = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
dir, num = 0, 1

x, y = n // 2, n // 2
while num < n ** 2 + 1:
    grid[x][y] = num
    num += 1

    new_x, new_y = x + dx[dir], y + dy[dir]

    if grid[new_x][new_y] != 0:
        dir -= 1

    x, y = x + dx[dir], y + dy[dir]
    dir += 1
    dir %= 4

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()
