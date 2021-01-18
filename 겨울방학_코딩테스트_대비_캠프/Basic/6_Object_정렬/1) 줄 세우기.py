N = int(input())
height = []
weight = []
order = []

for i in range(N):
    h, w = map(int, input().split())
    height.append(h)
    weight.append(w)
    order.append(i + 1)

info = [
    (height[i], weight[i], order[i])
    for i in range(N)
]
info.sort(key=lambda x: (-x[0], -x[1]))

for info_tup in info:
    for info in info_tup:
        print(info, end=' ')
    print()