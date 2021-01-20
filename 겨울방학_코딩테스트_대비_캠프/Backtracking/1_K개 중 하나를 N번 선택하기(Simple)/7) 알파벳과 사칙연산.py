'''
완전탐색으로 푸는 방법 - (모든 경우의 수)
O(N)으로 푸는 방법 - 기호에 따른 숫자 변화
'''

'''
완전탐색 풀이
'''

def calculation(a,op,b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    else:
        return a*b

s = list(input().split())

while len(s) > 1 :
    s = calculation(s[0],s[1],s[2]) + s[:]