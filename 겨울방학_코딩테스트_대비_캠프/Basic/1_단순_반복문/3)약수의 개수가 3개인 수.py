start, end = map(int, input().split())
result = 0

for num in range(start, end + 1):
    cnt = 0
    for check in range(1, num + 1):
        if num % check == 0:
            cnt += 1

    if cnt == 3:
        result += 1

print(result)