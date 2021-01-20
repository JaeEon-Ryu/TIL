A = input()
n = len(A)

for _ in range(n):
    if A[0] == A[-1]:
        A = A[-1] + A[:-1]
    else:
        break

char = A[0]
cnt = 1
result = ''

for i in range(1,len(A)):
    if char == A[i]:
        cnt += 1
    else:
        result += char + str(cnt)
        cnt = 1
        char = A[i]

result += char + str(cnt)

print(len(result))

