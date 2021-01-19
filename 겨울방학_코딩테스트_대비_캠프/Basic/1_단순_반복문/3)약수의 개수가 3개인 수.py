start, end = map(int, input().split())
result = 0

for num in range(start, end + 1): # strat ~ end 사이의 숫자들
    cnt = 0
    for check in range(1, num + 1): # 약수 구하기
        if num % check == 0:
            cnt += 1

    if cnt == 3: # 개수 세기
        result += 1

print(result)