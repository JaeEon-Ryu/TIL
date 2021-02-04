'''
문제에서는 각 위치에서 여덟방향으로 인접한 칸들 중 가장 큰 숫자와 가운데 칸의 숫자를 교환하라고 나와있는데,
예제1과 예제2에 대한 입출력은 여덟방향이 아닌, 상하좌우 네가지 방향으로 풀어야 정답이 나오는 듯함

추가적으로 테스트케이스3에서는 1 ~ n * n 사이의 숫자들이 한번씩 등장하는 것이 아닌
0 ~ n*n-1 의 숫자들이 등장함

질의 게시판에 올림.

-> 문제 수정되었음 ( Passed )
'''

import itertools
n,m = map(int,input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

# dirs에 방향 8개 저장
dirs = [-1,0,1]
dirs = list(itertools.permutations(dirs,2))
dirs.append((-1,-1))
dirs.append((1,1))

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def change_nums(x,y):
    max_x,max_y = x,y
    max_val = 0

    # 8방향 탐색
    for dir_x,dir_y in dirs:
        new_x,new_y = x+dir_x, y+dir_y
        if in_range(new_x,new_y):

            if max_val < grid[new_x][new_y]:
                max_val = grid[new_x][new_y]
                max_x, max_y = new_x,new_y

    grid[x][y],grid[max_x][max_y] = grid[max_x][max_y],grid[x][y]

    return

# m번반복
for _ in range(m):

    # 1에서 n**2까지
    for num in range(n**2+1):
        break_loop = False

        for i in range(n):
            for j in range(n):
                if grid[i][j] == num:
                    change_nums(i,j)
                    break_loop = True
                    break

            if break_loop:
                break

# 출력
for i in range(n):
    for j in range(n):
        print(grid[i][j],end=' ')
    print()

