'''
구현방법1 - O(2^n)
구현방법2 - O(nCm) # 쓸데없이 쓰는 부분이 하나도 없음 # 제일 효율적
'''

# 구현방법 1
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

    combination.append(curr_num)
    find_combination(curr_num+1,cnt+1)
    combination.pop()
    
    find_combination(curr_num+1,cnt)
    
find_combination(1,0)

''' 구현방법 2
# 변수 선언 및 입력

n, m = tuple(map(int, input().split()))
visited = [
    False for _ in range(n + 1)
]


# 방문한 원소들을 출력해줍니다.
def print_combination():
    for i in range(1, n + 1):
        if visited[i]:
            print(i, end = " ")
    
    print()


# 지금까지 뽑은 갯수와 마지막으로 뽑힌 숫자를 추적하여
# 그 다음에 뽑힐 수 있는 원소의 후보를 정합니다.
def find_combination(cnt, last_num):
    # m개를 모두 뽑은 경우 답을 출력해줍니다.
    if cnt == m:
        print_combination()
        return
    
    # 뽑을 수 있는 원소의 후보들을 탐색합니다.
    for i in range(last_num + 1, n + 1): 
        visited[i] = True;
        find_combination(cnt + 1, i);
        visited[i] = False;


# 가능한 범위를 순회하며 해당 숫자가 
# 조합의 첫번째 숫자일 때를 탐색합니다.
for i in range(1, n + 1):
    visited[i] = True
    find_combination(1, i)
    visited[i] = False
'''


'''구현방법1로 구현방법 2와 같은 효율 만들어내기
N, M = map(int, input().split())

combination = []

def print_combination():
    for c in combination:
        print(c, end=' ')
    print()

def find_combination(curr_num, cnt):
    
    ########################## 이 부분이 중요
    if cnt == M:
        print_combination()
        return

    if curr_num == N+1:
        return
    #########################

    combination.append(curr_num)
    find_combination(curr_num + 1, cnt + 1)
    combination.pop()

    find_combination(curr_num + 1, cnt)

find_combination(1, 0)
'''