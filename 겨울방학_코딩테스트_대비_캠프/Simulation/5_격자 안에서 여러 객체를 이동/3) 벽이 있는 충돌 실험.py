'''
기존 방법 - TK당 O(n^4)
구슬을 움직일 때 격자를 활용한다.
( N*N 격자에 구슬의 개수만큼 숫자를 새김 )
모든 구슬을 움직였다면 격자에 저장된 값들을 중심으로 구슬 제거를 시작한다.
( 구슬의 개수가 2개 이상인 좌표를 찾았다면, 해당 좌표가 모두 없어질 때까지 반복문을 돌며 제거 )

개선한 방법 - TK당 O(n^3)
구슬을 움직일 떄 딕셔너리를 활용한다.
( key값을 좌표값으로, value값을 좌표값에 대한 중복 횟수로 저장 )
모든 구슬을 움직였다면 딕셔너리에 저장된 value 값을 중심으로 구슬 제거를 시작한다.
( value가 2 이상이라면 제거 )
'''

def in_range(x,y):
    return 0 <= x < N and 0 <= y < N

def make_dict(x,y):
    if (x,y) in temp_cdn:
        temp_cdn[(x,y)] += 1
    else:
        temp_cdn[(x,y)] = 1

T = int(input())

dir_index = ['U','L','D','R']
dx,dy = [-1,0,1,0],[0,-1,0,1]


# T개의 테스트 케이스
for _ in range(T):
    N,M = map(int,input().split())

    dirs = []
    marble_info = []

    # M개의 구슬들 입력받기
    for m in range(M):
        x,y,d = input().split()
        x,y = int(x) - 1, int(y) - 1
        marble_info.append([x, y, d])

    # 임의의 시간 흘려보내기
    for _ in range(N*2):

        temp = [] # marble_info의 1초 후 구슬 위치들을 담아둘 곳
        temp_cdn = dict() # 1초 후 구슬 위치 ( x,y 좌표값만 )

        for x,y,d in marble_info:

            i = dir_index.index(d) # 방향에 따라 dx, dy값을 찾기 위함
            new_x,new_y = x+dx[i], y+dy[i]

            if in_range(new_x,new_y):
                temp.append([new_x,new_y,d])
                make_dict(new_x,new_y)
            else:
                temp.append([x,y,dir_index[(i+2)%4]]) # 반대방향 저장
                make_dict(x,y)

        marble_info = temp

        # 겹쳐진 구슬들 제거하기
        for key,val in temp_cdn.items(): # key = x,y 좌표값, value = 겹쳐진 수

            if val >= 2:
                rv_x,rv_y = key[0], key[1]
                idx = 0

                while idx < len(marble_info):
                    if marble_info[idx][0] == rv_x and marble_info[idx][1] == rv_y:
                        del marble_info[idx]
                    else:
                        idx += 1


    # 남아있는 구슬의 개수 세기
    print(len(marble_info))

'''
# 시간 초과가 났던 코드

def in_range(x,y):
    return 0 <= x < N and 0 <= y < N

T = int(input())

dir_index = ['U','L','D','R']
dx,dy = [-1,0,1,0],[0,-1,0,1]

# T개의 테스트 케이스
for _ in range(T):
    N,M = map(int,input().split())

    grid = [
        [0 for _ in range(N)]
        for _ in range(N)
    ]

    coordinates = []
    dirs = []

    # M개의 구슬들 입력받기
    for m in range(M):
        x,y,d = input().split()
        x,y = int(x) - 1, int(y) - 1

        coordinates.append([x,y]) # 좌표값들
        dirs.append(d) # 방향값들

        grid[x][y] = 1 # 최초의 격자 상태 처리

    # 임의의 시간 흘려보내기
    for _ in range(N*2):

        # M개의 구슬들 시간에 따라 이동 처리하기
        for m in range(M):
            x,y = coordinates[m][0], coordinates[m][1] # 좌표
            d = dirs[m] # 방향
            i = dir_index.index(d) # 방향에 따라 dx, dy값을 찾기 위함
            new_x,new_y = x+dx[i], y+dy[i]

            if in_range(new_x,new_y):
                grid[x][y] -= 1
                grid[new_x][new_y] += 1
                coordinates[m] = [new_x,new_y]
            else:
                dirs[m] = dir_index[(i+2)%4] # 반대방향 저장

        # 격자 안에 구슬개수가 2개 이상인 것 제거
        for i in range(N):
            for j in range(N):
                if grid[i][j] >= 2:

                    while [i,j] in coordinates:
                        remove_index = coordinates.index([i,j])
                        coordinates.remove([i,j])
                        del dirs[remove_index]
                        grid[i][j] -= 1
                        M -= 1

    # 남아있는 구슬의 개수 세기
    cnt = 0
    for i in range(N):
        for j in range(N):
            cnt += grid[i][j]

    print(cnt)
'''