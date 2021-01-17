a, b = map(int, input().split())

result = 0
for num in range(a, b + 1):
    result += num

print(result)