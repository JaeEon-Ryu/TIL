'''
tc3 fail

'''

n,m = map(int,input().split())
x,y,d = map(int,input().split())

state = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] == 1 or state[x][y] == 1:
        return False
    return True

# 북 동 남 서
dx, dy = [1,0,-1,0],[0,1,0,-1]

visited[x][y] = 1
dist = 1

while True:

    dir = []
    for i in range(4):
        dir.append((d-i)%4)

    for i in dir:
        new_x, new_y = x + dx[dir[i]], y + dy[dir[i]]

        if can_go(new_x,new_y):
            visited[new_x][new_y] = 1
            dist += 1
            x,y = new_x,new_y
            d = i
            break
    else:
        d = dir[0]
        new_x, new_y = x - dx[d], y - dy[d]

        if state[new_x][new_y] == 1:
            break
        else:
            x,y = new_x,new_y


print(dist)

'''
6 4
4 1 2
1 1 1 1
1 0 0 1
1 1 0 1
1 0 1 1
1 0 0 1
1 1 1 1

'''