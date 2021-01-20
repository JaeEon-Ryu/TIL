def get_num_of_gold(row_s, col_s, row_e, col_e):
    num_of_gold = 0

    for r in range(row_s, row_e + 1):
        for c in range(col_s, col_e + 1):
            num_of_gold += grid[r][c]

    return num_of_gold


N = int(input())

grid = []
for i in range(N):
    grid.append(list(map(int, input().split())))

max_gold = 0

for row in range(N):
    for col in range(N):
        if row + 2 >= N or col + 2 >= N:
            continue

        num_of_gold = get_num_of_gold(row, col, row + 2, col + 2)

        max_gold = max(max_gold, num_of_gold)

print(max_gold)