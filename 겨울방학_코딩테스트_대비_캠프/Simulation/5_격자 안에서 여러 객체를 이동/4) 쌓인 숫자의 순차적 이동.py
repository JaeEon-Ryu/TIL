'''
TK11번에 숫자 0이 등장함 - 수정 요청했음
'''

n,m = map(int,input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

orders = map(int,input().split())

def list_setting():
    for i in range(n):
        for j in range(n):
            grid[i][j] = [grid[i][j]]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]] # 방향 8가지
list_setting() # 3차원 리스트 제작

# 움직임의 횟수만큼 반복
for order in orders:

    break_point = False
    # 움직일 숫자 찾기
    for i in range(n):
        for j in range(n):

            # 움직일 숫자가 있는 리스트
            if order in grid[i][j]:

                order_index = grid[i][j].index(order) # 움직일 숫자 리스트 슬라이싱
                order_list = grid[i][j][:order_index+1] # 움직일 숫자들

                max_val = -1
                max_x = None
                max_y = None
                # 8방향 최대값 찾기
                for dx,dy in dirs:
                    new_x, new_y = i+dx, j+dy

                    if in_range(new_x,new_y):
                        if grid[new_x][new_y] == []: # 리스트가 비어있다면 수행 x
                            val = -1
                        else:
                            val = max(grid[new_x][new_y])

                        if max_val < val:
                            max_val = val
                            max_x = new_x
                            max_y = new_y

                # 숫자 옮기기 ( 주변에 값이 있다면 옮기기 , 최대값으로 )
                if max_x != None and max_y != None:
                    grid[max_x][max_y] = order_list + grid[max_x][max_y] # 옮김 완료
                    del grid[i][j][:order_index+1] # 출발점 제거

                break_point = True
                break

        if break_point:
            break

# 출력
for i in range(n):
    for j in range(n):
        if grid[i][j] == []:
            print('None')
        else:
            for num in grid[i][j]:
                print(num,end=' ')
            print()
