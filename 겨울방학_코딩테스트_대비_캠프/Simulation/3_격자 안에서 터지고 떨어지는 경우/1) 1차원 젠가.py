n = int(input())
blocks = []
for i in range(n):
    blocks.append(int(input()))

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

blocks = blocks[:s1 - 1] + blocks[e1:]
blocks = blocks[:s2 - 1] + blocks[e2:]

print(len(blocks))
for b in blocks:
    print(b)

''' 리스트 슬라이싱을 하지 않을 경우
# 변수 선언 및 입력
n = int(input())
numbers = [
    int(input())
    for _ in range(n)
]
end_of_array = n


# 입력 배열에서 지우고자 하는 부분 수열을 삭제함
# 비어있는 부분을 그 다음 부분의 값으로 차례차례 할당시킴
def cut_array(start_idx, end_idx):
    global end_of_array
    
    cut_len = end_idx - start_idx + 1;
    for i in range(end_idx + 1, end_of_array):
        numbers[i - cut_len] = numbers[i]
    
    end_of_array -= cut_len


# 두 번에 걸쳐 지우는 과정을 반복
for _ in range(2):
    s, e = tuple(map(int, input().split()))
    # [s, e] 구간을삭제
    cut_array(s - 1, e - 1)

# 출력:
print(end_of_array)
for i in range(end_of_array):
    print(numbers[i])
'''