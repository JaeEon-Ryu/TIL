N = int(input())
nums = list(map(int,input().split()))

while nums:
    max_index = nums.index(max(nums))
    print(max_index+1,end=' ')
    nums = nums[:max_index] # 리스트 초기화