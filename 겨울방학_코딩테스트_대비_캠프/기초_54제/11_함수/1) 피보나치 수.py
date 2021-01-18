N = int(input())
a,b = 1,1

for i in range(1,N):
    a,b = b,a+b

print(a)