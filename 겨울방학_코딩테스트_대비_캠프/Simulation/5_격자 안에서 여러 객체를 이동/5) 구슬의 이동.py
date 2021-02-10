n,m,t,k = map(int,input().split())

global grid
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]

for _ in range(1,m+1):
    r,c,d,v = input().split()
    r,c,v = int(r)-1,int(c)-1,int(v)
    grid[r][c].append([d,v,_])

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

mapper = {'U' : 0, 'R' : 1, 'D' : 2, 'L' : 3}
num_to_char_mapper = {0 :  'U', 1 : 'R', 2 : 'D', 3 : 'L'}
dx,dy = [-1,0,1,0],[0,1,0,-1]


# for i in range(n):
#     for j in range(n):
#         print(grid[i][j],end=' ')
#     print()
# print()

# 구슬 움직이기
def move_marbles():
    global grid

    temp_grid = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):

            if grid[i][j]:
                for _ in range(len(grid[i][j])):

                    # 원래 있던 자리의 구슬 제거
                    m_info = grid[i][j].pop()
                    d,v,num = m_info[0], m_info[1], m_info[2]

                    x,y = i,j

                    # 구슬 움직이기
                    for _ in range(v):
                        new_x, new_y = x + dx[mapper[d]] , y + dy[mapper[d]]

                        if not in_range(new_x,new_y): # 방향 전환
                            d = num_to_char_mapper[(mapper[d]+2)%4]
                            x,y = x+dx[mapper[d]], y+dy[mapper[d]]

                        else: # 그대로 이동
                            x,y = new_x, new_y

                    # 구슬 위치 갱신
                    temp_grid[x][y].append([d,v,num])

    grid = temp_grid


# 겹쳐진 구슬 제거하기
def remove_overlapped_marbles():
    global grid

    for i in range(n):
        for j in range(n):

            if grid[i][j]:
                if k >= len(grid[i][j]):
                    continue
                else:

                    # 번호 기준 오름차순 정렬
                    grid[i][j].sort(key=lambda x:x[2],reverse=True)

                    # 숫자 작은 것 부터 순차적으로 삭제
                    while k < len(grid[i][j]):
                        grid[i][j].pop()
                    #for _ in range(len(grid[i][j]) - k):


# 남아 있는 구슬의 개수 출력하기
def print_the_number_of_marbles():
    global grid

    result = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                #print(grid[i][j],len(grid[i][j]))
                result += len(grid[i][j])

    print(result)

for _ in range(t):
    move_marbles()
    remove_overlapped_marbles()

    # for i in range(n):
    #     for j in range(n):
    #         print(grid[i][j], end=' ')
    #     print()
    # print()



print_the_number_of_marbles()

'''
tk3

33 541 23 2
17 3 R 8
20 4 L 9
8 29 D 6
13 32 U 2
26 20 L 6
25 2 L 3
8 14 L 8
9 23 U 10
14 21 U 6
33 2 U 3
30 8 L 2
23 12 U 4
16 22 D 8
1 31 U 10
8 13 U 7
28 16 U 1
33 26 D 2
3 15 R 3
2 17 L 3
19 9 D 9
33 10 L 4
19 14 D 6
17 12 D 6
5 10 D 3
10 28 D 2
1 23 D 3
31 22 U 5
10 8 L 10
17 18 R 7
31 24 R 2
6 9 R 4
24 15 D 9
27 17 U 6
6 33 R 6
20 30 U 1
13 20 D 7
6 17 L 3
33 27 R 10
32 7 R 9
8 16 D 8
33 33 U 5
31 17 U 10
4 14 L 9
10 6 R 10
10 23 L 4
1 32 D 2
27 10 L 8
5 11 L 8
33 22 R 1
4 33 U 8
2 8 U 5
29 8 L 10
20 7 R 2
23 16 R 8
24 20 R 1
8 31 U 1
18 14 D 5
20 28 D 9
22 8 D 1
3 29 L 10
29 21 D 8
19 24 U 5
31 4 D 6
23 21 U 10
11 29 R 3
9 32 L 9
6 25 R 7
13 17 L 4
1 18 D 3
27 33 U 5
15 6 L 5
5 25 U 9
16 31 L 9
13 23 U 9
13 29 U 4
10 17 L 6
1 11 L 8
14 12 R 4
29 4 R 4
17 4 L 2
14 15 R 4
1 8 D 6
15 12 R 5
31 5 R 10
6 31 R 4
16 16 L 6
4 23 L 7
22 32 R 7
30 29 L 1
17 25 U 1
22 5 U 6
10 2 L 6
21 28 D 6
28 13 R 3
7 11 L 7
26 18 D 6
17 7 L 4
29 3 D 4
4 17 L 10
6 7 R 6
25 9 R 6
3 9 R 1
32 5 U 10
30 32 D 5
10 20 U 2
12 24 D 2
32 20 U 5
4 18 L 1
17 13 R 4
9 14 R 8
17 5 R 2
8 1 U 8
27 6 U 8
12 13 R 6
24 19 U 3
1 1 R 10
5 7 D 5
19 31 R 4
12 23 L 10
28 18 R 3
25 32 U 10
21 25 R 3
12 16 U 6
16 25 D 3
2 13 D 2
26 25 U 4
6 29 U 10
8 18 D 2
30 22 U 4
2 19 L 1
32 9 U 2
16 9 L 7
13 30 R 8
15 2 L 4
7 31 U 3
8 5 D 3
2 11 L 6
32 1 U 2
8 33 D 6
10 16 R 4
20 9 U 10
16 15 U 1
7 14 U 10
14 23 D 5
1 17 D 1
6 20 U 9
16 11 R 10
16 8 R 3
3 1 U 3
23 19 U 3
19 4 R 9
10 10 U 10
23 14 L 10
28 4 U 10
8 3 U 4
25 31 L 2
9 10 D 7
5 9 U 5
20 10 D 5
31 21 R 3
13 14 D 7
27 2 R 8
11 17 D 1
19 11 L 4
23 33 L 3
3 31 D 7
15 20 L 5
13 15 R 10
22 29 U 8
3 28 U 5
15 5 D 4
8 30 R 8
13 7 R 4
15 24 L 1
31 18 D 5
7 28 D 7
5 17 R 3
16 29 D 8
31 1 R 3
22 1 L 4
19 21 U 1
12 7 U 3
27 9 L 1
2 9 D 3
14 18 L 6
4 2 R 7
9 11 U 7
13 8 D 8
22 26 D 1
5 23 U 3
23 31 D 10
32 27 L 4
30 10 R 8
4 30 D 7
15 31 L 6
20 13 U 4
30 9 D 5
19 18 R 4
32 3 D 5
16 5 L 4
32 25 D 1
2 31 R 7
17 32 L 5
1 13 L 10
10 9 L 5
13 11 R 4
26 10 D 7
2 1 U 8
5 22 R 7
1 15 R 4
18 5 U 2
28 7 L 5
21 2 R 3
29 32 D 5
5 28 R 6
30 18 D 7
21 13 R 7
29 19 D 6
23 20 U 8
28 27 R 2
31 25 D 5
29 9 U 8
14 4 L 5
22 13 R 5
16 12 D 7
18 10 U 9
1 30 R 2
6 22 L 7
15 1 L 5
16 27 D 6
18 11 L 5
19 10 R 8
31 11 R 9
26 22 U 10
11 28 U 4
4 9 L 9
32 16 L 1
26 6 U 5
9 4 D 8
27 12 U 7
32 13 D 5
1 33 D 9
17 2 U 5
5 26 U 9
10 14 L 9
6 14 L 2
22 18 L 9
13 19 L 3
28 32 D 2
12 2 R 5
12 5 D 3
11 5 R 1
11 8 D 6
24 25 R 3
1 16 R 1
15 4 U 4
33 31 D 4
7 24 R 4
30 16 R 4
17 16 R 2
16 7 L 5
24 8 L 5
30 7 R 2
16 28 R 1
22 20 U 2
30 30 R 5
11 4 D 6
8 7 L 4
15 11 D 10
4 15 D 9
25 12 L 8
24 6 R 1
24 7 R 3
20 31 L 9
7 20 L 8
12 30 L 9
27 4 U 2
3 6 L 10
32 18 U 9
30 17 L 2
29 25 L 9
28 21 L 6
20 21 U 4
2 7 L 3
27 22 U 5
13 12 L 10
12 21 U 7
12 18 D 3
32 29 L 4
5 24 L 5
26 16 U 2
7 10 L 10
21 1 U 10
18 31 L 3
26 2 R 10
10 26 L 1
6 16 L 8
21 31 R 6
7 23 L 4
4 25 D 6
12 15 U 3
27 13 R 8
28 25 R 10
1 14 L 2
28 29 U 9
3 25 L 3
26 9 R 8
24 28 D 4
29 28 U 10
24 18 R 4
14 22 R 7
26 24 U 8
5 3 U 6
4 5 U 6
11 9 L 1
12 25 D 6
15 30 U 3
15 9 D 8
12 14 R 1
15 10 U 9
4 27 D 4
9 9 D 5
4 16 U 8
29 11 D 8
25 16 U 4
12 19 L 1
26 14 L 2
31 2 R 8
24 32 U 2
18 24 D 5
18 16 U 6
3 30 D 1
23 6 R 7
6 26 L 4
2 16 U 1
21 12 R 10
21 20 L 7
28 12 R 2
16 3 L 9
14 32 D 6
19 26 L 4
20 19 R 5
29 7 R 9
3 21 U 10
31 6 D 5
28 15 U 3
6 5 D 8
2 2 D 6
28 20 L 9
19 27 D 5
25 26 R 2
19 7 R 3
33 20 D 5
21 16 R 3
23 11 U 1
29 24 R 5
17 33 L 3
13 18 L 1
20 27 D 6
23 30 D 1
25 27 R 8
28 5 L 5
6 19 U 1
18 29 U 2
20 32 U 10
30 23 D 7
24 29 L 4
2 6 L 10
18 4 D 5
16 33 D 7
23 28 R 4
4 6 L 8
3 17 R 2
23 17 D 8
30 13 D 10
6 21 R 9
3 18 U 3
19 33 L 4
6 10 L 9
30 19 D 9
13 9 D 10
27 16 D 7
32 4 U 4
17 28 R 4
10 12 R 3
13 5 L 10
23 15 U 4
32 8 U 8
30 6 R 6
26 31 D 7
18 20 R 10
8 10 U 2
18 13 R 6
29 15 L 2
2 29 D 10
9 8 L 4
10 30 L 2
14 13 D 4
24 3 U 5
19 25 D 4
26 21 U 7
3 27 L 1
4 12 R 1
12 3 U 8
11 24 U 1
31 12 U 7
23 24 U 9
5 31 U 2
14 11 D 2
31 31 D 3
13 26 L 1
22 31 R 3
30 31 D 3
17 26 U 1
7 2 L 1
31 28 R 2
20 2 L 2
12 27 R 2
5 14 U 4
2 33 R 3
1 20 L 4
3 2 L 5
11 25 U 5
33 18 U 2
12 9 D 9
9 13 D 6
26 3 U 9
24 24 L 4
5 20 R 8
19 19 L 7
14 6 R 5
15 25 L 4
7 5 U 6
30 24 L 7
11 20 D 1
20 29 U 10
27 23 U 1
22 22 D 5
19 15 L 6
4 4 L 10
6 27 R 1
1 6 D 3
30 27 R 7
25 8 L 4
32 11 U 9
12 20 D 9
11 14 R 6
27 8 D 1
3 5 D 5
11 19 R 2
32 32 D 7
12 1 U 4
5 18 D 4
22 7 R 7
11 21 R 9
8 8 U 3
18 12 U 9
9 25 R 1
14 3 U 5
16 17 L 6
2 5 D 8
23 4 R 10
20 11 U 8
29 10 U 1
2 3 U 1
22 30 R 5
21 30 L 7
16 14 L 1
15 33 D 6
6 8 R 7
12 10 R 6
20 33 R 9
3 4 R 7
27 20 D 8
29 17 L 7
14 25 L 7
21 24 D 9
29 22 R 2
5 27 U 6
17 6 L 1
2 12 R 1
26 8 D 3
10 29 D 6
30 4 D 7
27 25 R 9
17 17 L 7
12 22 U 7
6 2 R 10
17 11 R 6
10 22 U 4
19 2 D 1
9 26 U 4
31 7 R 2
15 23 R 5
23 9 R 3
27 15 U 7
5 8 D 6
11 32 L 2
27 19 R 1
5 32 U 2
9 27 R 9
24 5 L 6
1 27 R 7
20 17 L 5
10 5 L 4
4 20 D 3
8 15 R 2
11 6 U 8
7 15 U 9
10 32 R 7
12 12 D 4
24 22 R 7
18 21 D 5
33 19 U 9
27 3 L 5
25 11 U 10
17 10 U 7
7 6 R 7
25 15 U 2
9 22 L 3
18 26 L 9
25 6 L 2
24 21 L 9
11 15 U 7
14 19 L 6
2 21 L 8
14 20 L 6
7 12 U 10
27 29 D 4
24 12 R 3
32 21 L 1
10 4 D 7
27 28 R 9
24 11 U 6
32 31 L 10
3 13 U 5
7 26 D 3
9 15 D 2
28 19 D 3
31 27 R 10
13 25 U 9


343 이 나와야함
( 현재 345 나오는 중 )
기존의 답보다 답이 더 크게 나왔다는 것은
지워져야 할 구슬이 다 지워지지 않았다는 뜻임

'''