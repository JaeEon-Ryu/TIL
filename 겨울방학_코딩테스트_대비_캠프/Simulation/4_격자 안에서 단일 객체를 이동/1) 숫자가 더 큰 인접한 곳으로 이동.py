'''
우선순위 : 상하좌우

'''


def in_range(x, y): # 틀 안에 있는지
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y, curr_num): # 기존 값보다 더 큰지
    return in_range(x, y) and grid[x][y] > curr_num


n, r, c = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for i in range(n)
]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dir = 0
x, y = r - 1, c - 1
curr_num = grid[x][y]
print(curr_num, end=' ')

while dir < 4: # 상하좌우를 다 돌았는데도 없다면 중지

    new_x, new_y = x + dx[dir], y + dy[dir]

    if can_go(new_x, new_y, curr_num):
        x, y, curr_num = new_x, new_y, grid[new_x][new_y]
        dir = 0
        print(curr_num, end=' ')
    else:
        dir += 1