# 리브로스코드 해설 참고

import collections

n, m, k = map(int, input().split())
apple = [
    [False for _ in range(n + 1)]
    for _ in range(n + 1)
]

snake = collections.deque([(1, 1)])
snake_pos = set([(1, 1)])

dirs = { 'D': 0, 'U': 1, 'R': 2, 'L': 3 }
ans = 0

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def alreay_visited(new_head):
    return new_head in snake_pos

def push_front(new_head):

    if alreay_visited(new_head):
        return False

    snake.appendleft(new_head)
    snake_pos.add(new_head)

    return True

def pop_back():

    tail = snake.pop()
    snake_pos.remove(tail)

def move_snake(new_x, new_y):

    if apple[new_x][new_y]:
        apple[new_x][new_y] = False

        if not push_front((new_x, new_y)):
            return False
    else:
        pop_back()

        if not push_front((new_x, new_y)):
            return False

    return True


def move(move_dir, num):
    global ans

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    for _ in range(num):
        ans += 1

        (head_x, head_y) = snake[0]
        new_x = head_x + dx[move_dir]
        new_y = head_y + dy[move_dir]

        if not in_range(new_x, new_y):
            return False

        if not move_snake(new_x, new_y):
            return False

    return True


for _ in range(m):
    x, y = tuple(map(int, input().split()))
    apple[x][y] = True

for _ in range(k):
    move_dir, num = tuple(input().split())
    num = int(num)

    if not move(dirs[move_dir], num):
        break

print(ans)


'''
# tk 11번 오답
import sys

n,m,k = map(int,input().split())

grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    x,y = map(int,input().split())
    x,y = x-1,y-1
    grid[x][y] = 'a'
grid[0][0] = 1

direction_conversion = []
for _ in range(k):
    d,p = input().split()
    p = int(p)
    direction_conversion.append([d,p])

dirs = {'U':0, 'D':1, 'R':2, 'L':3}
dx,dy = [-1,1,0,0],[0,0,1,-1]
global result
result = 0

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def already_visited(x,y):
  #  print(x,y)
    return True if grid[x][y] not in (0,'a') else False

def exit_and_print_answer():
    global result
    print(result+1)
    sys.exit()

def remove_min_value():
    min_val = 101
    min_x,min_y = 0,0

    for i in range(n):
        for j in range(n):
            if grid[i][j] in ('a',0):
                continue
            else:
                if min_val > grid[i][j]:
                    min_val = grid[i][j]
                    min_x,min_y = i,j

    grid[min_x][min_y] = 0

def move_from(x,y):
    global result
    global test
    order = 2

    for d,p in direction_conversion:
        new_x,new_y = x+dx[dirs[d]] * p, y+dy[dirs[d]] * p
        #print(dx[dirs[d]], dy[dirs[d]] )
        #print(new_x,new_y)

        apple_cnt = 0
        #print(p)
        #print(d,p)
        # 방향에 따라 뱀 이동하기
        for dist in range(1,p+1):
            step_x,step_y = x + dx[dirs[d]] * dist, y + dy[dirs[d]] * dist
            #print(between_x,between_y)
            if not in_range(step_x,step_y):
                exit_and_print_answer()

            if grid[step_x][step_y] != 'a':
                remove_min_value()
                if already_visited(step_x,step_y):
                    #print(step_x,step_y)
                    #print('?')
                    exit_and_print_answer()

            #print(step_x,step_y)
            #print()
            grid[step_x][step_y] = order
            result += 1
            order += 1

        #for i in range(n):
        #    for j in range(n):
        #        print('%2s'%(grid[i][j]),end=' ')
        #    print()
        #print()

        x,y = new_x,new_y

global first_move
first_move = True

#for i in range(n):
#    for j in range(n):
#        print('%2s'%(grid[i][j]), end=' ')
#    print()
#print()

move_from(0,0)
print(result)

'''

