n = int(input())
stones = list(map(int,input().split()))
footprint = []
global result,is_passed
result = 11
is_passed = False

def find_permutation(idx):
    global result,is_passed

    if idx >= len(stones) - 1:
        if len(footprint) < result:
            result = len(footprint)
            is_passed = True
        return

    for i in range(stones[idx]):

        footprint.append(idx)
        find_permutation(idx+i+1)
        footprint.pop()

find_permutation(0)
if is_passed:
    print(result)
else:
    print(-1)

