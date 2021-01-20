'''
완전탐색으로 푸는 방법 - (모든 경우의 수)
O(N)으로 푸는 방법 - 기호에 따른 숫자 변화
'''

'''
완전탐색 풀이
'''

import sys
INT_MIN = -sys.maxsize
global max_val
max_val = INT_MIN\
#print(max_val)
def calculation(a,op,b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    else:
        return a*b

def find_max():
    global max_val

    result = 4 # 처음 숫자는 4로 시작해야 제일 큼
    for op,num in zip(op_list,nums):
        result = calculation(result,op,num)
    #print(result)
    if result > max_val:
        max_val = result

def find_permutaion(cnt):
    if cnt == N:
        find_max()
        return

    nums.append(1)
    find_permutaion(cnt+1)
    nums.pop()

    nums.append(4)
    find_permutaion(cnt+1)
    nums.pop()



# 값 입력받기
s = input()
N = (len(s)+1)//2
s = s[1:]
op_list = []

# operator 따로 보관
for i in range(len(s)):
    if i%2==0:
        op_list.append(s[i])

# 숫자들 따로 보관
nums = []

# permutation 시작
find_permutaion(0)

print(max_val)


'''

def calculation(a,op,b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    else:
        return a*b

s = input()
s = s[1:]

result = 4
for i in range(len(s)):
    if i%2 == 0:
        if s[i] == '+' or s[i] == '*':
            result = calculation(result,s[i],4)
        else:
            result = calculation(result, s[i], 1)

print(result)
'''