n,m = map(int,input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x < n and 0 <= y <m

# 첫 번째 종류의 케이스 ( 북, 동, 서, 남 )
def block_case_1(x,y):
    sum_of_blocks = [0]

    if in_range(x-1,y) and in_range(x,y) and in_range(x,y+1):
        sum_of_blocks.append(grid[x-1][y] + grid[x][y] + grid[x][y+1])

    if in_range(x,y) and in_range(x,y+1) and in_range(x+1,y):
        sum_of_blocks.append(grid[x][y] + grid[x][y+1] + grid[x+1][y])

    if in_range(x,y-1) and in_range(x,y) and in_range(x+1,y):
        sum_of_blocks.append(grid[x][y-1] + grid[x][y] + grid[x+1][y])

    if in_range(x-1,y) and in_range(x,y-1) and in_range(x,y):
        sum_of_blocks.append(grid[x-1][y] + grid[x][y-1] + grid[x][y])

    return max(sum_of_blocks)

# 두 번째 종휴의 케이스 ( 가로, 세로 )
def block_case_2(x,y):
    sum_of_blocks = [0]

    if in_range(x,y-1) and in_range(x,y) and in_range(x,y+1):
        sum_of_blocks.append(grid[x][y-1] + grid[x][y] + grid[x][y+1])

    if in_range(x-1,y) and in_range(x,y) and in_range(x+1,y):
        sum_of_blocks.append(grid[x-1][y] + grid[x][y] + grid[x+1][y])

    return max(sum_of_blocks)


max_of_sum = 0

for i in range(n):
    for j in range(m):
        max_of_sum = max(max_of_sum,block_case_1(i,j),block_case_2(i,j))

print(max_of_sum)