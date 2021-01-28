n,m,q = map(int,input().split())

matrix = [
    list(map(int,input().split()))
    for _ in range(n)
]

wind = [
    list(input().split())
    for _ in range(q)
]


def shift(r,h,v): # r = row, h = horizontal, v = vertical
    opposite_h = ''

    if h == 'L':
        matrix[r] = [matrix[r][-1]] + matrix[r][:-1]
        opposite_h = 'R'
    else:
        matrix[r] = matrix[r][1:] + [matrix[r][0]]
        opposite_h = 'L'

    if v == 'bidirection': # 최초의 경우 ( 양방향 )
        if 0 <= r-1 : # 위로 올라가기
            for j in range(m):
                if matrix[r-1][j] == matrix[r][j]:
                    shift(r - 1, opposite_h, 'U')
                    break
        if r+1 < n : # 아래로 내려가기
            for j in range(m):
                if matrix[r][j] == matrix[r+1][j]:
                    shift(r + 1, opposite_h, 'D')
                    break
    elif v == 'U':
        if 0 <= r-1 : # 위로 올라가기
            for j in range(m):
                if matrix[r-1][j] == matrix[r][j]:
                    shift(r - 1, opposite_h, 'U')
                    break
    else: # v == 'D'
        if r+1 < n : # 아래로 내려가기
            for j in range(m):
                if matrix[r][j] == matrix[r+1][j]:
                    shift(r + 1, opposite_h, 'D')
                    break

# Q개의 바람
for row, dir in wind:
    shift(int(row)-1,dir,'bidirection')

# 출력
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end=' ')
    print()

