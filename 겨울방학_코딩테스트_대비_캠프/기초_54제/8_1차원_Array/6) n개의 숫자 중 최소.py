N = int(input())
nums = list(map(int,input().split()))

print(min(nums),nums.count(min(nums)))