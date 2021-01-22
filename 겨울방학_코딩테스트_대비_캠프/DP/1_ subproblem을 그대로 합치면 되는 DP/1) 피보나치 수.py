# 내 풀이
N = int(input())
a,b = 1,1

for i in range(1,N):
    a,b = b,a+b

print(a)

''' for문 방법 1
N = int(input())
li = [
    0 for _ in range(N)
]
li[0],li[1] = 1,1

for i in range(2,N):
    li[i] = li[i-1] + li[i-2]

print(li[N-1])
'''

''' 재귀적 방법 - 메모이제이션 추가 활용
N = int(input())
memo = [
    -1 for _ in range(N+1)
]

def fibo(n):
    if memo[n] != -1:
        return memo[n]

    if n == 1 or n == 2:
        memo[n] = 1
    else :
        memo[n] = fibo(n-1) + fibo(n-2)

    return memo[n]

print(fibo(N))
'''