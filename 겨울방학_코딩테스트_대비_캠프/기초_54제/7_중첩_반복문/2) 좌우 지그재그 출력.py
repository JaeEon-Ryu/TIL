'''
짝수 행마다 역방향으로 출력한다는 것을 감안
'''

n = int(input())

for i in range(0,n):
    if i%2==0:
        for j in range(1,n+1):
            print((n*i)+j,end=' ')
    else:
        for j in range(n,0,-1):
            print((n*i)+j,end=' ')
    print()