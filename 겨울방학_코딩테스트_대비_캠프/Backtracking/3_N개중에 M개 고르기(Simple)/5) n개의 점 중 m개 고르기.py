import sys
global INT_MIN
INT_MIN = sys.maxsize
global INT_MAX
INT_MAX = -sys.maxsize

n, m = map(int, input().split())
coordinates = []
for _ in range(n):
    coordinates.append(list(map(int,input().split())))
points = []
final_points = []


# 점 n개중 m개 선택하기 ( combination )
def select_m_points(curr_num, cnt):
    global INT_MAX
    global INT_MIN

    if curr_num == n:
        if cnt == m:
            select_two_points(len(points),0,0,points)
            INT_MIN = min(INT_MAX, INT_MIN)
            INT_MAX = -sys.maxsize

        return

    points.append(curr_num)
    select_m_points(curr_num + 1, cnt + 1)
    points.pop()

    select_m_points(curr_num + 1, cnt)

# 선택된 m개 중 2개 선택하기 ( combination )
def select_two_points(nop,curr_num, cnt,m_list):
    if curr_num == nop:
        if cnt == 2:
            cal_distance(m_list)

        return

    final_points.append(curr_num)
    select_two_points(nop,curr_num + 1, cnt + 1,m_list)
    final_points.pop()

    select_two_points(nop,curr_num + 1, cnt,m_list)

# 거리 계산
def cal_distance(m_list):
    global INT_MAX

    i_1 = m_list[final_points[0]]
    i_2 = m_list[final_points[1]]

    x = coordinates[i_2][0] - coordinates[i_1][0]
    y = coordinates[i_2][1] - coordinates[i_1][1]

    # 선택된 m개중 두 점 사이의 거리가 가장 먼 것
    INT_MAX = max(INT_MAX,x**2 + y**2)


select_m_points(0, 0)
print(INT_MIN)


'''
5 3
1 1
2 2
3 3
4 4
5 5

입력:
3 2
1 1
4 4
3 5

출력: 
2
'''