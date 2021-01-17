'''
3의 배수이거나 숫자에 3, 6, 9 중 하나라도 들어가있는 경우에는 0을 출력
'''

n = int(input())

for num in range(1,n+1):
    if num%3 == 0 or '3' in str(num) or '6' in str(num) or '9' in str(num):
        print(0,end=' ')
    else:
        print(num,end=' ')