n,m,r,c = map(int,input().split())
dirs = list(input().split())
r,c = r-1,c-1

grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dice = [1,2,3] # 상단, 측면-정면, 측면-우측
dx,dy = [1,-1,0,0],[0,0,-1,1] # 남,북,서,동
dir = ['D','U','L','R']

# 격자 범위 체크
def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

# 주사위 모양 변경하기
def change_dice(d,i): # dice, idx
    if i == 0: # 'D'
        return [7-d[1],d[0],d[2]]
    elif i == 1: # 'U'
        return [d[1],7-d[0],d[2]]
    elif i == 2: # 'L'
        return [d[2],d[1],7-d[0]]
    else: # 'R'
        return [7-d[2],d[1],d[0]]

# 격자 내 숫자들의 합
def grid_sum(g): # grid
    s = 0
    for _ in g:
        s += sum(_)
    return s

grid[r][c] = 7-dice[0]

for d in dirs:
    dir_idx = dir.index(d) # 방향 인덱스
    new_r, new_c = r + dx[dir_idx], c + dy[dir_idx]

    if in_range(new_r,new_c): # 굴린 곳이 범위 안이라면 작동
        dice = change_dice(dice, dir_idx)
        r, c = new_r, new_c
        grid[r][c] = 7-dice[0]

result = grid_sum(grid)

print(result)