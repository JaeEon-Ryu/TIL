
from collections import deque

n, k = map(int,input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 결과를 담아둘 리스트
# 끝까지 상하지 않는 귤을 위해서 처음부터 -2로 초기화
result = [
    [-2 for _ in range(n)]
    for _ in range(n)
]

dx, dy = [-1,1,0,0],[0,0,-1,1]


def visited_initialization():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

def in_range(x,y):
    return 0 <= x < n  and 0 <= y < n

def can_go(x,y,s):
    global second

    if not in_range(x,y):
        return False
    # 방문했거나 귤이 없거나 상한 귤일 경우
    if visited[x][y] == 1 or grid[x][y] in (0,2):
        return False
    # 초기화된 상태가 아닌 경우 ( 방문을 해서 값이 바뀐 경우 )
    if result[x][y] != -2:
        # 이미 기록된 시간보다 현재 시간이 더 클 경우 가면 안됨
        if s > result[x][y]:
            return False

    return True

def bfs():
    global second

    while q:
        x,y,s = q.popleft() # 행, 열, 시간
        s += 1 # 시간 1초 추가
        for i in range(4):
            new_x,new_y = x + dx[i], y + dy[i]

            if can_go(new_x, new_y,s):
                visited[new_x][new_y] = 1
                result[new_x][new_y] = s # 시간 기록
                q.append([new_x, new_y, s])


q = deque()

for i in range(n):
    for j in range(n):

        if grid[i][j] == 0: # 아무것도 없을 때
            result[i][j] = -1
        elif grid[i][j] == 1: # 귤이 존재할 때
            continue
        else: # 상한귤이 존재할 때
            result[i][j] = 0
            visited[i][j] = 1
            second = 1
            q.append([i,j,0])
            bfs()

            # 또 다른 상한 귤을 만날 확률이 있으므로
            # visited 초기화
            visited_initialization()


for i in range(n):
    for j in range(n):
        print(result[i][j],end=' ')
    print()


'''
4 3
1 1 1 1
1 0 2 1
0 1 2 1
2 1 0 0


3 2 1 2
4 -1 0 1
-1 1 0 1
0 1 -1 -1

'''

