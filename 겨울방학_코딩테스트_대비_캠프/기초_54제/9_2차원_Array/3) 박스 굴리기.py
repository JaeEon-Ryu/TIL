n = int(input())

arr = []
# 처음 그림
for i in range(n):
    arr.append(list(map(int,input().split())))

# 굴린 결과
for i in range(n):
    for j in range(n-1,-1,-1):
        print(arr[j][i],end=' ')
    print()