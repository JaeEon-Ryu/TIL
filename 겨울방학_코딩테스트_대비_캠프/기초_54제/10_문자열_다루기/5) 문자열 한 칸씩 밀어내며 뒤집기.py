'''
1 -> 가장 앞에 있는 문자를 제외한 나머지 문자를 한 칸씩 앞으로
    가장 앞에 있던 문자를 가장 뒤로
2 -> 가장 뒤에 있는 문자를 제외한 나머지 문자를 한 칸씩 뒤로
    가장 뒤에 있던 문자를 가장 앞으로
3 -> 문자열을 좌우로 뒤집기
'''

s, q = input().split()
q = int(q)
s = list(s)

for i in range(q):
    op = input()

    if op == '1':
        s = s[1:] + [s[0]]

    elif op == '2':
        s = [s[-1]] + s[:-1]

    else:
        s = s[::-1]

    print(''.join(s))

