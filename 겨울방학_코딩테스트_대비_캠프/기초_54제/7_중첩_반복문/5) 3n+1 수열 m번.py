def count_until_1(n):
    cnt = 0

    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        cnt += 1

    return cnt


n = int(input())
m = []
for i in range(n):
    m.append(int(input()))

for num in m:
    print(count_until_1(num))