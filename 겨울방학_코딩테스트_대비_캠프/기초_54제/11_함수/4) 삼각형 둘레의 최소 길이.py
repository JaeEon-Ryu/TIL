import math,itertools

# 피타고라스 정의를 이용한 거리 구하기
def triangle_distance(x1,y1,x2,y2,x3,y3):
    d = 0

    a = abs(x2-x1)
    b = abs(y2-y1)
    d += math.sqrt(a ** 2 + b ** 2)

    a = abs(x3-x2)
    b = abs(y3-y2)
    d += math.sqrt(a ** 2 + b ** 2)

    a = abs(x3 - x1)
    b = abs(y3 - y1)
    d += math.sqrt(a ** 2 + b ** 2)

    return round(d,2)

n = int(input())
coordinate = []

# 좌표 생성
for i in range(n):
    x,y = map(int,input().split())
    coordinate.append([x, y])

# 좌표에 대한 삼각형 조합 생성
triangle_list = list(itertools.combinations(coordinate,3))
min_distance = 4000

# 최단 거리 구하기
for triangle in triangle_list:
    dist = triangle_distance(triangle[0][0], triangle[0][1], triangle[1][0],
                        triangle[1][1], triangle[2][0], triangle[2][1])
    if min_distance > dist:
        min_distance = dist

print('%.2f'%(min_distance)) # 이 부분 쓰지 않으면 7번 테스트 케이스 틀림