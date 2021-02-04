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

