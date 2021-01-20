'''
쌍 찾을 때 : 배열 통째로 반복문 -> 각 원소 오른쪽과 아래쪽만 보도록 하기

'''

n = int(input())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

dx, dy = [0,0,1,-1],[1,-1,0,0]


def can_go(x,y):
    return 0 <= x < n and 0 <= y < n

# 십자가 모양 터트리기
def burst(c_grid,x,y):
    depth = c_grid[x][y]
    c_grid[x][y] = 0
    dir = 0

    for i in range(4):
        new_x, new_y = x + dx[dir], y + dy[dir]
        cnt = 1

        while can_go(new_x,new_y) and cnt < depth:
            c_grid[new_x][new_y] = 0
            new_x, new_y = new_x + dx[dir], new_y + dy[dir]
            cnt+=1
        dir += 1

# 터트린 후 정리하기
def arrangement(c_grid):
    temp = [
        [0 for i in range(n)]
        for j in range(n)
    ]

    for j in range(n):
        r = n-1
        for i in range(n - 1, -1, -1):
            if c_grid[i][j] != 0:
                temp[r][j] = c_grid[i][j]
                r -= 1

    return temp

# 짝 세기
def count_pair(c_grid):
    cnt = 0

    for i in range(n):
        for j in range(n):
            if c_grid[i][j] != 0:

                if can_go(i,j+1):
                    if c_grid[i][j] == c_grid[i][j+1]:
                        cnt += 1
                if can_go(i-1,j):
                    if c_grid[i][j] == c_grid[i-1][j]:
                        cnt +=1

    return cnt


max_val = 0
for i in range(n):
    for j in range(n):

        copy = []
        for _ in grid:
            copy.append(_[:])

        burst(copy,i,j)
        new_grid = arrangement(copy)
        val = count_pair(new_grid)

        max_val = max(val,max_val)

print(max_val)


