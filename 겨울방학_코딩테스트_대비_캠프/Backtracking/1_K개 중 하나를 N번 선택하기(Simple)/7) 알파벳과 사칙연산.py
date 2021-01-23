'''
리스트[::2]    # 처음부터 끝까지 2칸씩            = 홀수번째
리스트[1::2]   # 첫 번째 인덱스부터 끝까지 2칸씩   = 짝수번째
'''

import sys
INT_MAX = -1 * sys.maxsize

s = input()

unique_set = set(s[::2]) # 중복제거된 알파벳들
unique_len = len(unique_set)

nums = []

def string_calculator(s_modified):
    result = int(s_modified[0])
    s_modified = s_modified[1:]

    for i in range(len(s_modified)):
        if i%2 == 1:
            # s_modified[i-1] = 연산자
            # s_modified[i] = 오른쪽 숫자
            result = calculation(result,s_modified[i-1],int(s_modified[i]))

    return result

def calculation(left,op,right):
    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    else:
        return left * right

def cal_in_permutation():
    global max_val

    s_copied = s[:]
    # permutation에서 얻은 숫자를 문자에 대입
    for n,u in zip(nums, unique_set):
        s_copied = s_copied.replace(u,str(n))

    max_val = max(max_val,string_calculator(s_copied))


def find_permutations(cnt):
    if cnt == unique_len:
        cal_in_permutation()
        return

    for i in range(1,5):
        nums.append(i)
        find_permutations(cnt+1)
        nums.pop()

global max_val
max_val = INT_MAX
find_permutations(0)

print(max_val)