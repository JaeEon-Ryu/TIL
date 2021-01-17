n, m = map(int, input().split())  # 격자의 크기, 점의 개수
grid = []

for i in range(n): # 좌표 미리 그려놓기
    grid.append([0 for i in range(n)])

for i in range(1, m + 1): # 번호 순서대로 표시
    x, y = map(int, input().split())
    grid[x - 1][y - 1] = i

for rows in grid: # 출력
    for c in rows:
        print(c, end=' ')
    print()
