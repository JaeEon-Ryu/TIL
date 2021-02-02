n = int(input())
x,y = map(int,input().split())
x,y = x-1,y-1

grid = [
    list(input())
    for _ in range(n)
]

dx,dy = [0,1,0,-1],[1,0,-1,0]
dir = 0

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

result = 0
cnt = 0 # 무한루프 방지

while True:
    new_x,new_y = x+dx[dir],y+dy[dir]
    result += 1
    cnt += 1

    if not in_range(new_x,new_y):
        break

    if cnt > n**3: # 미로를 계속 돌고있으면 탈출 불가능
        result = -1
        break

    if grid[new_x][new_y] == '#': # 막히면 반 시계 방향
        result -= 1 # 방향만 바꿨으므로 진행 -1
        if dir == 0:
            dir = 3
        else :
            dir -= 1
    else: # 막히지 않으면 이동
        if not in_range(new_x, new_y):
            break
        else:
            x,y = new_x,new_y

            # 시계방향
            if dir == 3:
                dir = 0
            else:
                dir += 1
            new_x, new_y = x+dx[dir], y+dy[dir]

            # 시계방향으로 보낸 값 확인
            if grid[new_x][new_y] == '#':
                # 벽이 있다면 바꿨던 시계방향을 다시 반시계로 진행
                if dir == 0:
                    dir = 3
                else:
                    dir -= 1
            else:
                # 벽이 없다면 방향을 시계방향으로 바꾼 그대로 진행
                continue

print(result)

'''
5
2 2
#####
.....
##...
##...
.....

7
'''







