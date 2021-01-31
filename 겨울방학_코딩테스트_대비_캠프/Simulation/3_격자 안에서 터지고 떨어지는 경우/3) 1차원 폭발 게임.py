import sys
n,m = map(int,input().split())
bombs = []
for _ in range(n):
    bombs.append(int(input()))

if m == 1:
    print(0)
    sys.exit()

while bombs:
    curr_index = 0
    curr_num = bombs[0]
    cnt_same = 1
    is_exploded = False
    deleted_length = 0

    for i in range(1,len(bombs)):
        if curr_num == bombs[i-deleted_length]:
            cnt_same += 1
        else: # 숫자가 다를 경우 개수 확인
            if cnt_same >= m :
                del bombs[curr_index:i-deleted_length]
                deleted_length += (i - deleted_length) - curr_index
                is_exploded = True

            curr_index = i-deleted_length
            curr_num = bombs[i-deleted_length]
            cnt_same = 1

    if cnt_same >= m:  # 위 반복문을 수행하고 나온 예외사항 -> ( 끝까지 숫자가 같은 경우 )
        del bombs[curr_index : i - deleted_length + 1]

    if not is_exploded:
        break


if bombs:
    print(len(bombs))
    for b in bombs:
        print(b)
else:
    print(0)

'''
4 2
1
2
2
1


5 2
1
2
2
1
1
'''