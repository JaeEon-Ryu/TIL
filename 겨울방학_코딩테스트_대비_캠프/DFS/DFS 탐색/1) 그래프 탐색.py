N, M = map(int,input().split())
graph = [[0 for i in range(N+1)] for i in range(N+1)]

visited = [0 for i in range(N+1)]
global cnt
cnt = 0

def DFS(vertex):
    global cnt

    for i in range(1,N+1):
        if graph[vertex][i] and not visited[i]:
            visited[i] = 1
            cnt += 1
            DFS(i)


for i in range(M):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

root_vertex = 1

visited[root_vertex] = 1
DFS(root_vertex)

print(cnt)


''' 인접 리스트 활용
# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

#index를 1번 부터 사용하기 위해 m+1만큼 할당합니다.
graph = [[] for _ in range(n + 1)]

visited = [False for _ in range(n + 1)]
vertex_cnt = 0

def dfs(vertex):
    global vertex_cnt
    global visited
    
    # 해당 정점에서 이어져있는 모든 정점을 탐색해줍니다.
    for i in range(len(graph[vertex])):
        curr_v = graph[vertex][i]
        # 아직 간선이 존재하고 방문한 적이 없는 정점에 대해서만 탐색을 진행합니다.
        if not visited[curr_v]:
            visited[curr_v] = True
            vertex_cnt += 1
            dfs(curr_v)
    
for i in range(m):
    v1, v2 = tuple(map(int, input().split()))

    # 각 정점이 서로 이동이 가능한 양방향 그래프이기 때문에
    # 각 정점에 대한 간선을 각각 저장해줍니다.
    graph[v1].append(v2)
    graph[v2].append(v1)

visited[1] = True
dfs(1)

print(vertex_cnt)

'''



