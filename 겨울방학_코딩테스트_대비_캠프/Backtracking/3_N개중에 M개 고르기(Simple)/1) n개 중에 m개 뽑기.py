'''
구현방법1 - O(2^n)
구현방법2 - O(nCm) # 쓸데없이 쓰는 부분이 하나도 없음 # 제일 효율적

'''

N, M = map(int,input().split())

combination = []

def print_combination():
    for c in combination:
        print(c,end=' ')
    print()
    
def find_combination(curr_num,cnt):
    if curr_num == N+1:
        if cnt == M:
            print_combination()
        return

    if cnt > M:
        return

    combination.append(curr_num)
    find_combination(curr_num+1,cnt+1)
    combination.pop()
    
    find_combination(curr_num+1,cnt)
    
find_combination(1,0)