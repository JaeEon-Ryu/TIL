A = input()

char = A[0]
cnt = 1
result = ''

for idx in range(1,len(A)):
    if char == A[idx]:
        cnt += 1
    else:
        result += char + str(cnt)
        cnt = 1
        char = A[idx]
result += char + str(cnt)

print(len(result))
print(result)