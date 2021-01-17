n, q = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(q):
    line = list(map(int, input().split()))

    if line[0] == 1:
        print(nums[line[1] - 1])

    elif line[0] == 2:
        if line[1] in nums:
            print(nums.index(line[1]) + 1)
        else:
            print(0)

    else:
        for num in nums[line[1] - 1:line[2]]:
            print(num, end=' ')
        print()