'''
코드 리팩토링 필요 ( 문제는 passed 처리되었음 )
리팩토링 해봤자 L,R 끼리 그리고 U,D 끼리 함수처리 가능 할 것으로 보임
'''

grid = [
    list(map(int,input().split()))
    for _ in range(4)
]

dir = input()

dirs = ['L','R','U','D']
dx,dy = [0,0,-1,1],[-1,1,0,0]

dir_idx = dirs.index(dir)

result_grid = [
    [0 for _ in range(4)]
    for _ in range(4)
]

temp_grid = []


if dir == 'L':
    for i in range(4):
        temp = []
        origin_num = False
        compare_num = False
        for j in range(4):
            if grid[i][j] == 0: # 비어있는 공간
                continue

            if not origin_num:
                origin_num = grid[i][j]
            else:
                if not compare_num:
                    compare_num = grid[i][j]

                if origin_num == compare_num:
                    temp.append(origin_num + compare_num)
                    origin_num = False
                    compare_num = False
                else:
                    temp.append(origin_num)
                    origin_num = compare_num
                    compare_num = False

        if origin_num : temp.append(origin_num)
        if compare_num : temp.append(compare_num)

        temp_grid.append(temp)

    for i in range(4):
        for j in range(4):
            if temp_grid[i]:
                result_grid[i][j] = temp_grid[i].pop(0)
            else:
                break

if dir == 'R':
    for i in range(4):
        temp = []
        origin_num = False
        compare_num = False
        for j in range(3,-1,-1):
            if grid[i][j] == 0: # 비어있는 공간
                continue

            if not origin_num:
                origin_num = grid[i][j]
            else:
                if not compare_num:
                    compare_num = grid[i][j]

                if origin_num == compare_num:
                    temp.append(origin_num + compare_num)
                    origin_num = False
                    compare_num = False
                else:
                    temp.append(origin_num)
                    origin_num = compare_num
                    compare_num = False

        if origin_num : temp.append(origin_num)
        if compare_num : temp.append(compare_num)

        temp_grid.append(temp)

    for i in range(4):
        for j in range(3,-1,-1):
            if temp_grid[i]:
                result_grid[i][j] = temp_grid[i].pop(0)
            else:
                break

if dir == 'U':
    for j in range(4):
        temp = []
        origin_num = False
        compare_num = False
        for i in range(4):
            if grid[i][j] == 0: # 비어있는 공간
                continue

            if not origin_num:
                origin_num = grid[i][j]
            else:
                if not compare_num:
                    compare_num = grid[i][j]

                if origin_num == compare_num:
                    temp.append(origin_num + compare_num)
                    origin_num = False
                    compare_num = False
                else:
                    temp.append(origin_num)
                    origin_num = compare_num
                    compare_num = False

        if origin_num : temp.append(origin_num)
        if compare_num : temp.append(compare_num)

        temp_grid.append(temp)

    for j in range(4):
        for i in range(4):
            if temp_grid[j]:
                result_grid[i][j] = temp_grid[j].pop(0)
            else:
                break

if dir == 'D':
    for j in range(4):
        temp = []
        origin_num = False
        compare_num = False
        for i in range(3,-1,-1):
            if grid[i][j] == 0: # 비어있는 공간
                continue

            if not origin_num:
                origin_num = grid[i][j]
            else:
                if not compare_num:
                    compare_num = grid[i][j]

                if origin_num == compare_num:
                    temp.append(origin_num + compare_num)
                    origin_num = False
                    compare_num = False
                else:
                    temp.append(origin_num)
                    origin_num = compare_num
                    compare_num = False

        if origin_num : temp.append(origin_num)
        if compare_num : temp.append(compare_num)

        temp_grid.append(temp)

    for j in range(4):
        for i in range(3,-1,-1):
            if temp_grid[j]:
                result_grid[i][j] = temp_grid[j].pop(0)
            else:
                break



for i in range(4):
    for j in range(4):
        print(result_grid[i][j],end=' ')
    print()



