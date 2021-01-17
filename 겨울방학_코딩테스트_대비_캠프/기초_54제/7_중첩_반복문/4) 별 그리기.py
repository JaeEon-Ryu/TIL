n = int(input())

for i in range(1,2*n):
    print(' ' * abs(n-i), end='')
    print('*' * ((2*n-1) - abs(n-i)*2))