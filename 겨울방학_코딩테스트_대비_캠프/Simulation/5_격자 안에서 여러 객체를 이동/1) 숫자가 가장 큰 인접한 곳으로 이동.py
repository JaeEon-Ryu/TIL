def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


n, m, t = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

num_of_marble = [
    [0 for _ in range(n)]
    for _ in range(n)
]

coordinate_of_marble = []

for _ in range(m):
    x, y = list(map(int, input().split()))
    num_of_marble[x-1][y-1] = 1
    coordinate_of_marble.append([x,y])


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dir = 0

for _ in range(t):

    # 구슬의 좌표가 있다면 실행
    if not coordinate_of_marble:
        break

    moved_x = 0
    moved_y = 0
    for marble in coordinate_of_marble:
        marble_x = marble[0] - 1
        marble_y = marble[1] - 1
        max_value = 0
        dir = 0

        # 이동하기 전에 원래 있었던 좌표의 기록 지우기
        num_of_marble[marble_x][marble_y] -= 1

        # 4방향 모두 탐색 후 최대값으로 이동
        while dir < 4:
            new_x, new_y = marble_x + dx[dir], marble_y + dy[dir]
            if in_range(new_x, new_y) and grid[new_x][new_y] > max_value:
                moved_x = new_x
                moved_y = new_y
                max_value = grid[moved_x][moved_y]
            dir += 1

        # 이동 후 해당 좌표에 구슬 개수 기록
        num_of_marble[moved_x][moved_y] += 1

    # 2개 이상의 구슬 지우기 및 구슬 좌표 초기화
    coordinate_of_marble = []
    for i in range(n):
        for j in range(n):
            if num_of_marble[i][j] >= 2:
                num_of_marble[i][j] = 0
            elif num_of_marble[i][j] == 1:
                coordinate_of_marble.append([i+1,j+1])

print(len(coordinate_of_marble))