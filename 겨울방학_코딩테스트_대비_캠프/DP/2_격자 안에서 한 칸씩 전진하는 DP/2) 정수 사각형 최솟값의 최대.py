'''
경로를 지나갈 때마다 바로 이전 경로(왼쪽경로, 위쪽경로)의 최대값을
현재 경로와 비교하여 더 작은것을 현재 경로에 저장한다
-> 결국 마지막에 최솟값을 죄대로 끌어올린 값을 얻을 수 있다
'''

n = int(input())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

def dp_setting(): # 초기 조건 설정

    for i in range(1,n):
        grid[i][0] = min(grid[i-1][0], grid[i][0])
    for j in range(1,n):
        grid[0][j] = min(grid[0][j-1], grid[0][j])

dp_setting()


for i in range(1,n):
    for j in range(1,n):
        grid[i][j] = min(max(grid[i-1][j],grid[i][j-1]),grid[i][j]) # 점화식

print(grid[-1][-1])


