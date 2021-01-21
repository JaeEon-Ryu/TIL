'''
기존 격자 탐색문제에서 조건 추가 ( 높이 u 이상 d 이하 )
어느 입구로 찾아가던 상관없음 ( 모두 이어지기 때문에 )
-> k개의 도시를 적절히 선택하지 않아도 된다는 소리 ( 순열, 조합 X )
-> 찾아간 곳 visited 표시 ( 중요 )


'''

from collections import deque

n,k,u,d = map(int,input().split())
grid = [
    list(map(int,input().split()))
    for i in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dx,dy = [0,0,1,-1],[1,-1,0,0]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def can_go(x,y,prev_x,prev_y):
    if not in_range(x,y):
        return False
    if visited[x][y] == 1:
        return False
    # 도시사이의 높이가 u이상, d이하면 지나가도록 함
    if u <= abs(grid[x][y] - grid[prev_x][prev_y]) <= d:
        return True
    else:
        return False

def bfs():
    global cnt_area

    while q:
        x,y = q.popleft()

        for i in range(4): # 방향 전환
            new_x, new_y = x+dx[i], y+dy[i]

            if can_go(new_x,new_y,x,y):
                cnt_area += 1
                q.append([new_x,new_y])
                visited[new_x][new_y] = 1

q = deque()
area_list = []
global cnt_area
cnt_area = 1

for i in range(n):
    for j in range(n):

        if visited[i][j] == 0:
            visited[i][j] = 1
            q.append([i,j])

            bfs()
            area_list.append(cnt_area)
            cnt_area = 1 # 지역 개수 초기화

area_list.sort(reverse=True)
result = sum(area_list[:k]) # k개의 도시로부터 고른 것들
print(result)


