''' 테스트케이스 10번 틀림
크기 구하기 방향
1. 오른쪽으로 쭉 구하기
2. 1번의 가로축을 그대로 내리기
- 배열 끝까지 다다랐거나, 음수일경우 중지
'''


n,m = map(int,input().split())

grid = [
    list(map(int,input().split()))
    for i in range(n)
]

def get_max(row_s,col_s):

    # 우측
    right_size = 1
    new_c = col_s + 1

    while new_c < m and grid[row_s][new_c] > 0:
        right_size += 1
        new_c += 1
    original_size = right_size

    # 우측하단
    new_r = row_s + 1
    flag = True
    while new_r < n and flag:
        for col in grid[new_r][col_s:new_c]:
            if col < 1:
                flag = False
                break
        else:
            right_size += original_size
        new_r += 1

    # 좌측
    left_size = 1
    new_r = row_s + 1

    while new_r < n and grid[new_r][col_s] > 0:
        left_size += 1
        new_r += 1
    original_size = left_size

    # 좌측하단
    new_c = col_s + 1
    flag = True
    while new_c < m and flag:
        for r in range(row_s,new_r):
            if grid[r][new_c] < 1:
                flag = False
                break
        else:
            left_size += original_size
        new_c += 1

    return max(left_size,right_size)


max_val = -1
for i in range(n):
    for j in range(m):
        if grid[i][j] > 0:
            max_val = max(max_val,get_max(i,j))

print(max_val)

'''
input
3 3
1 2 3
3 4 5
6 7 8

output
9
'''

'''
input
5 6
1 1 1 0 1 1
1 1 1 1 1 1
1 1 1 1 1 1
0 1 1 1 1 1
0 1 1 0 0 0

5

4 5
6 -2 4 -3 1
3 6 7 -4 1
6 1 8 15 -5
3 -5 1 16 3

6
'''