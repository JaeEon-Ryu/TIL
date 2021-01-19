start, end = map(int, input().split())
result = 0

for num in range(start, end + 1):
    divisor_sum = 0

    for current in range(1,num):
        if num % current == 0: # 약수 구하고 해당 약수들을 모두 합치기
            divisor_sum += current

    if divisor_sum == num:
        print(num)
        result += 1

print(result)