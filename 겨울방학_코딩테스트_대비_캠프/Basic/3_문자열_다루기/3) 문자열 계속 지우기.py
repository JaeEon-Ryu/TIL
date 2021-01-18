A = input()
B = input()

while B in A:
    idx = A.index(B)
    A = A[:idx] + A[idx + len(B):]

print(A)