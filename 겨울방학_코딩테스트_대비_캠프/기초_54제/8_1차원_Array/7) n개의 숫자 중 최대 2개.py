N = int(input())
nums = list(map(int,input().split()))

nums.sort(reverse=True)
print(nums[0],nums[1])