import sys
INT_MIN = -sys.maxsize

n = int(input())
s = list(map(int,input().split()))

dp = [INT_MIN for _ in range(n+1)]
a = s[:]
a.insert(0,0)

dp[0] = 0

for i in range(1,n+1):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))