a, b = map(int,input().split())

result = 0
for num in range(a,b+1):
    if num%2==0:
        result += num

print(result)