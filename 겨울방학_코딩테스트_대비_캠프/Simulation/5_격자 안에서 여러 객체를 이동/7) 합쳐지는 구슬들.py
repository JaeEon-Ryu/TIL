'''
진행중

'''

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def opposite_dir(char):
    if char == 'U':
        return 'D'
    elif char == 'D':
        return 'U'
    elif char == 'L':
        return 'R'
    else:
        return 'L'

def combine_marble(x,y,marble_info):
    marble_temp = []
    combine_temp = []

    # 합쳐야 할 리스트 떼어내기
    for marble in marble_info:
        if marble[0] == x and marble[1] == y:
            combine_temp.append(marble) # 합쳐야할 리스트
        else:
            marble_temp.append(marble)

    # 리스트 합치기
    max_d = ''
    max_o = 0
    sum_w = 0
    for r,c,d,w,o in combine_temp:
        sum_w += w
        if max_o < o:
            max_o = o
            max_d = d

    marble_temp.append([r,c,max_d,sum_w,max_o])
    marble_info = []
    for t in marble_temp:
        marble_info.append(t)

    return marble_info

n, m, t = map(int, input().split()) # 격자크기, 구슬 개수, 시간

grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

marble_info = []

for _ in range(m):
    r, c, d, w = list(input().split())
    order = n + 1
    marble_info.append([int(r),int(c),d,int(w),order])
    grid[int(r)-1][int(c)-1] = 1

dir = ['U','D','L','R']
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

temp = []
for _ in range(t):

    # 구슬의 좌표가 있다면 실행
    if not marble_info:
        break

    for marble in marble_info:
        row = marble[0] - 1
        col = marble[1] - 1
        dir_char = marble[2]

        # 이동하기 전에 원래 있었던 좌표의 기록 지우기

        grid[row][col] -= 1

        # 정해진 방향으로 이동
        new_x = row + dx[dir.index(dir_char)]
        new_y = col + dy[dir.index(dir_char)]

        if in_range(new_x, new_y) :
            row = new_x
            col = new_y
        else:
            dir_char = opposite_dir(dir_char)

        # 이동 후 해당 좌표에 구슬 개수 기록
        grid[row][col] += 1
        temp.append([row,col,dir_char,marble[3],marble[4]])

    # 2개 이상의 구슬 합치기 및 구슬 좌표 초기화
    marble_info = []
    for t in temp:
        marble_info.append(t)

    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2:
                combine_marble(i,j,marble_info)
                grid[i][j] = 1
    for i in range(n):
        for j in range(n):
            print(grid[i][j],end=' ')
        print()
    print()

max_w = 0
for info in marble_info:
    #print(info)
    if max_w < info[3]:
        max_w = info[3]


print(len(marble_info),max_w)

