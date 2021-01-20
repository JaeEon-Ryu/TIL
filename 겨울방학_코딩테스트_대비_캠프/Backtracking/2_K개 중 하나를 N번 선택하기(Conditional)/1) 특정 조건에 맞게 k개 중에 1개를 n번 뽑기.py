K,N = map(int,input().split())

permutation = []

def print_permutation():
    for i in range(len(permutation)):
        print(permutation[i],end =' ')
    print()

# 지금까지 cnt개의 숫자를 뽑았을 때
# 어떤 숫자를 뽑을지를 선택하는 함수
def find_permutations(cnt):
    if cnt == N:
        print_permutation()
        return

    for i in range(1,K+1):
        if cnt > 1 and \
                i == permutation[cnt-1] and\
                i == permutation[cnt-2]:
            continue
        else:
            permutation.append(i)
            find_permutations(cnt+1)
            permutation.pop()

find_permutations(0)