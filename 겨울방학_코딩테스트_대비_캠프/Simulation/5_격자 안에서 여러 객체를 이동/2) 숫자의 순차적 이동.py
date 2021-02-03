'''
문제에서는 각 위치에서 여덟방향으로 인접한 칸들 중 가장 큰 숫자와 가운데 칸의 숫자를 교환하라고 나와있는데,
예제1과 예제2에 대한 입출력은 여덟방향이 아닌, 상하좌우 네가지 방향으로 풀어야 정답이 나오는 듯함

추가적으로 테스트케이스3에서는 1 ~ n * n 사이의 숫자들이 한번씩 등장하는 것이 아닌
0 ~ n*n-1 의 숫자들이 등장함

질의 게시판에 올림.

tk 3번
9 79
15 38 19 22 4 60 7 36 5
35 74 1 18 24 53 48 57 16
30 77 14 70 52 12 39 20 37
46 27 72 6 54 71 9 32 65
50 42 17 13 2 55 10 44 41
79 31 11 76 47 33 8 45 29
61 68 34 75 26 28 25 59 43
66 78 3 56 63 80 23 0 62
64 51 73 49 40 58 67 21 69


40 30 1 50 32 34 8 69 13
45 39 76 81 77 73 5 71 70
75 14 29 16 52 58 54 62 22
46 11 68 4 41 25 80 7 63
31 12 47 74 42 38 78 18 64
3 48 15 24 17 56 2 55 59
10 79 36 66 51 57 19 33 9
21 26 49 67 61 23 20 0 6
28 43 37 60 35 53 65 72 27


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

dx,dy = [1,-1,0,0],[0,0,-1,1]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def change_nums(x,y):
    max_x,max_y = x,y
    max_val = 0
    # print('-----------------------')
    # print('바뀌기 전 --------')
    # for i in range(n):
    #     for j in range(n):
    #         print('%3d'%(grid[i][j]), end=' ')
    #     print()
    #
    # print()
    #
    # print(grid[x][y],'의 주위 숫자들')
    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if in_range(new_x, new_y):
            # print(grid[new_x][new_y],end=' ')
            if max_val < grid[new_x][new_y]:
                max_val = grid[new_x][new_y]
                max_x, max_y = new_x, new_y

    # for dir_x,dir_y in dirs:
    #     new_x,new_y = x+dir_x, y+dir_y
    #     if in_range(new_x,new_y):
    #         # print(grid[new_x][new_y],end=' ')
    #         if max_val < grid[new_x][new_y]:
    #             max_val = grid[new_x][new_y]
    #             max_x, max_y = new_x,new_y
    # print('----------')
    # print(grid[max_x][max_y],'선택-----')
    # 인접한 위치중 최대값과 교환
    grid[x][y],grid[max_x][max_y] = grid[max_x][max_y],grid[x][y]


    # for i in range(n):
    #     for j in range(n):
    #         print('%3d'%(grid[i][j]), end=' ')
    #     print()
    #
    # print()
    return

# m번반복
for _ in range(m):

    # 1에서 n**2까지
    for num in range(n**2+1):
        #print('현재 num = ',num)
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

