'''
손해를 보지 않으면서 채굴할 수 있는 가장 많은 금의 개수
 K*K + (K+1) * (K+1) <= m * cnt 의 조건 속 cnt의 max값
'''

n,m = map(int,input().split())
golds = [
    list(map(int,input().split()))
    for _ in range(n)
]


def count_gold(x,y):
    k = 0
    max_gold = 0

    while k != n: # n크기 배열에 있어서 마름모 모든 경우의 수
        gold = 0

        for i in range(n):
            for j in range(n):

                if abs(i-x) + abs(j-y) <= k: # 원점에서 벗어난 오차가 k 이하라면
                    if golds[i][j] == 1: # 골드를 찾도록 하기
                        gold += 1

        if k*k + (k+1) * (k+1) <= m * gold:
            max_gold = gold

        k += 1

    return max_gold


max_val = 0
for i in range(n):
    for j in range(n):
       max_val = max(max_val, count_gold(i,j))

print(max_val)
