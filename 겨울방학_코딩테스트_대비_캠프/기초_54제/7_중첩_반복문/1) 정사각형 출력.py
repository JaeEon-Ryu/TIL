n = int(input())

for num in range(1,n**2+1):
    print(num,end=' ')
    if num%n == 0:
        print()