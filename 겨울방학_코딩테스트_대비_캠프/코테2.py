'''
풀다가 엇나감
긴 코드를 함수로 자르는 연습 더 해야함
'''

from collections import deque
import sys
global INT_MAX
INT_MAX = sys.maxsize

n,m = map(int,input().split()) # m = 병원
grid =[
    list(map(int,input().split()))
    for _ in range(n)
]

# 빈칸인 경우 0, 사람인 경우 1, 병원인 경우 2

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

result = [
    [INT_MAX for _ in range(n)]
    for _ in range(n)
]

dx, dy = [-1,1,0,0],[0,0,-1,1]

def visited_initialization():

    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

def result_initialization():
    global INT_MAX
    for i in range(n):
        for j in range(n):
            result[i][j] = INT_MAX

def in_range(x,y):
    return 0 <= x < n  and 0 <= y < n

def can_go(x, y, dist):

    if not in_range(x,y):
        return False
    if visited[x][y] == 1 :
        return False
    if dist > result[x][y]:
        return False

    return True

def bfs():

    while q:
        x,y,dist = q.popleft() # 행, 열, 거리
        dist += 1 # 길이 1 추가
        for i in range(4):
            new_x,new_y = x + dx[i], y + dy[i]
            if can_go(new_x, new_y,dist):
                visited[new_x][new_y] = 1
                result[new_x][new_y] = dist # 거리 기록
                q.append([new_x, new_y, dist])


def cal_dist(grid,result):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                cnt += result[i][j]

    return cnt

def choice_hospital(grid):
    global min_val

    hospital_info = []
    hospitals = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                hospital_info.append([i,j])

    #print(hospital_info)
   # print("?")
    combination = []

    def print_combination():
        global min_val
        #print(combination)
        hospitals = []
        temp = []
        for c in combination:
            temp.append(hospital_info[c-1])
        #print(temp)
        grid_copied = [0 for _ in range(n) for _ in range(n)]
        for i in range(n):
            grid_copied[i] = grid[i][:]

        for x,y in temp:
            grid_copied[x][y] = 3
            #print(x,y)

        for i in range(n):
            for j in range(n):
                if grid_copied[i][j] == 3:  # 출발점
                    print('start',i,j)
                    visited[i][j] = 1
                    dist = 1
                    q.append([i, j, 0])
                    bfs()

                    for k in range(n):
                        for kk in range(n):
                            print(result[k][kk],end=' ')
                        print()

                    min_val = min(cal_dist(grid_copied, result), min_val)
                    visited_initialization()
        result_initialization()

        print(min_val)

            #print(temp)
            #print(hospital_info[c-1], end=' ')

        #hospitals.append(temp)
        #print(hospitals)
        #return hospitals
      #  print()

    def find_combination(curr_num, cnt):
        if curr_num == len(hospital_info) + 1:
            if cnt == m:
                print_combination()
            return

        combination.append(curr_num)
        find_combination(curr_num + 1, cnt + 1)
        combination.pop()

        find_combination(curr_num + 1, cnt)

    find_combination(1, 0)


q = deque()
global min_val
min_val = INT_MAX

choice_hospital(grid)





