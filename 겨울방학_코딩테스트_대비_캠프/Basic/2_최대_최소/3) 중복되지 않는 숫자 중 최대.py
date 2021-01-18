import sys

N = int(input())
nums = list(map(int,input().split()))
nums.sort(reverse=True)

for n in nums:
    if nums.count(n) == 1:
        print(n)
        sys.exit()

print(-1)