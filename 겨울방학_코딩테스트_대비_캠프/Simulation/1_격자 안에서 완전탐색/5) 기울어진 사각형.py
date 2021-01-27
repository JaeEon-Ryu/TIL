'''
a. 오른쪽 대각선 방향 (-1, +1) 한칸씩 while문 (in_range 일때까지)
    b. 왼쪽 대각선 방향 (-1, -1) 한칸씩 while문 (in_range 일때까지)
        c. a에서 갔던 거리만큼 왼쪽아래 대각선 이동 ( 이때도 in_range 검사 )
        d. c에서 break이 일어나지 않았다면 b에서 갔던 거리만큼 오른쪽 아래 대각선 이동
'''

n = int(input())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def get_max_from_current_point(x, y):

    result = 0
    path_sum_1 = 0

    # 1번,2번 방향을 탐색한 후 in_range의 경우라면
    # 반복 횟수를 대각선 길이로 만들어
    # 경로에 속한 값들을 갖고오기 위함
    right_diagonal_line = 1 # 오른쪽 대각선 길이
    left_diagonal_line = 1 # 왼쪽 대각선 길이

    tr_x, tr_y = x-1,y+1 # head to the top right
    while in_range(tr_x,tr_y): # 1번 방향으로 진행

        path_sum_1 += grid[tr_x][tr_y]
        tl_x, tl_y = tr_x-1, tr_y-1 # head to the top left
        path_sum_2 = path_sum_1
        left_diagonal_line = 1

        while in_range(tl_x,tl_y): # 2번 방향으로 진행

            path_sum_2 += grid[tl_x][tl_y]
            bl_x,bl_y = tl_x, tl_y # head to the bottom left
            path_sum_3 = path_sum_2

            for _ in range(right_diagonal_line): # 3번 방향으로 진행
                bl_x,bl_y = bl_x+1, bl_y-1

                if not in_range(bl_x,bl_y):
                    break
                else:
                    path_sum_3 += grid[bl_x][bl_y]
            else: # 3번 방향을 진행을 완료했을 때 break이 일어나지 않았다면 실행

                br_x, br_y = bl_x, bl_y # head to the bottom right
                path_sum_4 = path_sum_3

                for _ in range(left_diagonal_line): # 4번 방향으로 진행
                    br_x, br_y = br_x + 1, br_y + 1
                    path_sum_4 += grid[br_x][br_y]

                result = max(result, path_sum_4)

            tl_x, tl_y = tl_x - 1, tl_y - 1
            left_diagonal_line += 1

        tr_x, tr_y = tr_x - 1, tr_y + 1
        right_diagonal_line += 1

    return result


max_val = 4

# 직사각형을 여러개의 모양으로 나누어서 계산할 것이기 때문에 size별로 나눠준다
for size in range(3,n+1):
    for i in range(n):
        for j in range(n):
            max_val = max(max_val, get_max_from_current_point(i, j))

print(max_val)

