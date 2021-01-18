N = int(input())

dist = []
idx_list = [i for i in range(1, N + 1)]

for i in range(N):
    x, y = map(int, input().split())
    dist.append(abs(x) + abs(y))

sequence = [
    (dist[i], idx_list[i])
    for i in range(N)
]
sequence.sort(key=lambda x: x[0])

for s in sequence:
    print(s[1])