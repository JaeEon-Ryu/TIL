n,m,q = map(int,input().split())
building = [
    list(map(int,input().split()))
    for _ in range(n)
]

wind = [
    list(map(int,input().split()))
    for _ in range(q)
]

dx, dy = [0,0,1,-1],[1,-1,0,0]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def building_rotation(r1, c1, r2, c2):

    # 1행1열 크기일 경우
    if r1 == 1 and c1 == 1 and r2 == 1 and c2 == 1 : return

    # 2행1열 크기일 경우
    if r1 == 1 and c1 == 1 and r2 == 2 and c2 == 1 :
        building[r1][c1], building[r2][c2] = building[r2][c2], building[r1][c1]
        return

    # 1행2열 크기일 경우
    if r1 == 1 and c1 == 1 and r2 == 1 and c2 == 2 :
        building[r1][c1], building[r2][c2] = building[r2][c2], building[r1][c1]
        return

    first_value = building[r1][c1]
    for i in range(r2-r1): # 왼쪽 사이드
        building[r1+i][c1] = building[r1+i+1][c1]
    for j in range(c2-c1): # 아래쪽 사이드
        building[r2][c1+j] = building[r2][c1+j+1]
    for i in range(r2-r1): # 오른쪽 사이드
        building[r2-i][c2] = building[r2-i-1][c2]
    for j in range(c2-c1-1): # 위쪽 사이드
        building[r1][c2-j] = building[r1][c2-j-1]
    building[r1][c1+1] = first_value


def building_condition_after_calulation(r1, c1, r2, c2):

    building_temp = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(m):

            if r1 <= i <= r2 and c1 <= j <= c2:

                sum_of_the_4_directions = building[i][j]
                cnt = 1

                for d in range(4): # 동서남북 방향으로 계산
                    new_x, new_y = i + dx[d], j + dy[d]

                    if in_range(new_x,new_y):
                        sum_of_the_4_directions += building[new_x][new_y]
                        cnt += 1

                # 결과값들을 한꺼번에 바꿔야 하므로 임시 배열에 저장
                building_temp[i][j] = sum_of_the_4_directions//cnt

    # 임시 배열에 저장된 값들을 모두 원래 배열에 복사
    for i in range(n):
        for j in range(m):
            if r1 <= i <= r2 and c1 <= j <= c2:
                building[i][j] = building_temp[i][j]



for start_i,start_j,end_i,end_j in wind:
    building_rotation(start_i - 1, start_j - 1, end_i - 1, end_j - 1)
    building_condition_after_calulation(start_i - 1, start_j - 1, end_i - 1, end_j - 1)

for i in range(n):
    for j in range(m):
        print(building[i][j],end=' ')
    print()
