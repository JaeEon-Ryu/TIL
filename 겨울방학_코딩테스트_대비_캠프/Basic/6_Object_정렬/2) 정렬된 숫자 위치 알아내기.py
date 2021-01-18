N = int(input())
nums = list(map(int,input().split()))
nums_index = [i for i in range(1,N+1)]

sequence = [
    (nums[i], nums_index[i])
    for i in range(N)
]
sequence.sort(key=lambda x:x[0])

sequence = [
    sequence[i] + (nums_index[i],)
    for i in range(N)
]
sequence.sort(key=lambda x:x[1])

for s in sequence:
    print(s[2], end=' ')
