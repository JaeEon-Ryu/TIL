#
# def find_rectangle(x,y):
#     end_x = x+1
#     for j in range(x,m):
#         if grid[x][j] < 1:
#             break
#         end_x = j
#     else:
#         for i in range(x,n):
#             if grid[i][end_x]:
#
#
#
# n,m = map(int,input().split())
#
# grid = [
#     list(map(int,input().split()))
#     for i in range(n)
# ]
#
# for i in range(n):
#     for j in range(m):

n,m = map(int,input().split())

grid = [
    list(map(int,input().split()))
    for i in range(n)
]

def get_max(row_s,col_s):

    # 우측
    right_size = 1
    new_c = col_s + 1

    while new_c < m and grid[row_s][new_c] >= 1:
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

    while new_r < n and grid[new_r][col_s] >= 1:
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
        if grid[i][j] >= 1:
            max_val = max(max_val,get_max(i,j))

print(max_val)


'''
5 6
1 1 1 1 1 1
0 1 1 1 0 0
0 1 1 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
'''