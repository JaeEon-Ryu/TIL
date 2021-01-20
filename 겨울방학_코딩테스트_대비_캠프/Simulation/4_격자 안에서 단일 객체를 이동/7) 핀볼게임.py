'''
1을 만났을 때 ( ' / ' ) :
    진행방향
        상 : ( -1, 0 ) -> ( 0, 1 )
        하 : ( 1, 0 ) -> ( 0, -1 )
        좌 : ( 0, 1 ) -> ( -1, 0 )
        우 : ( 0, -1 ) -> ( 1, 0 )
     => x,y = -y,-x

2를 만났을 때 ( ' \ ' ) :
    진행방향
        상 : ( -1, 0 ) -> ( 0, -1 )
        하 : ( 1, 0 ) -> ( 0, 1 )
        좌 : ( 0, 1 ) -> ( -1, 0 )
        우 : ( 0, -1 ) -> ( 1, 0 )
    => 2가지
'''

n = int(input())

grid = [
    list(map(int,input().split()))
    for i in range(n)
]

def can_go(x, y):
    return 0 <= x < n and 0 <= y < n


def time_calculation(x, y, move_x, move_y):
    cnt = 0
    new_x,new_y = x,y

    while can_go(new_x, new_y):

        if grid[new_x][new_y] == 1:
            move_x,move_y = -move_y,-move_x

        elif grid[new_x][new_y] == 2:
            if move_x == -1 or move_x == 1:
                move_x,move_y = move_y, move_x
            else:
                move_x, move_y = move_y, -move_x

        new_x += move_x
        new_y += move_y
        cnt += 1

    return cnt+1

def start_from_north():
    max_val = 2
    for j in range(n):
        time = time_calculation(0,j,1,0)
        if max_val < time:
            max_val = time

    return max_val


def start_from_south():
    max_val = 2
    for j in range(n):
        time = time_calculation(n-1, j, -1, 0)
        if max_val < time:
            max_val = time

    return max_val


def start_from_west():
    max_val = 2
    for i in range(n):
        time = time_calculation(i, 0, 0, 1)
        if max_val < time:
            max_val = time

    return max_val


def start_from_east():
    max_val = 2
    for i in range(n):
        time = time_calculation(i, n-1, 0, -1)
        if max_val < time:
            max_val = time

    return max_val

def get_maximum_time():
    return max(start_from_north(), start_from_west()
               , start_from_south(), start_from_east())

print(get_maximum_time())


