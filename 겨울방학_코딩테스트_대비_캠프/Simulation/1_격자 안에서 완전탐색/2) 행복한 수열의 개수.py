n,m = map(int,input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 연속되는 수가 m개 이상인지 확인
def is_happy_sequence(nums):
    num = nums[0]
    cnt = 1
    if m == 1:
        return True

    for i in range(1,len(nums)):
        if nums[i] == num:
            cnt += 1
            if cnt == m:
                return True
        else:
            num = nums[i]
            cnt = 1

    return False

number_of_sequence = 0

# 가로 수열 구하기
for row in grid:
    if is_happy_sequence(row):
        number_of_sequence += 1

# 세로 수열 구하기
for j in range(n):
    col = []

    for i in range(n):
        col.append(grid[i][j])

    if is_happy_sequence(col):
        number_of_sequence += 1

print(number_of_sequence)