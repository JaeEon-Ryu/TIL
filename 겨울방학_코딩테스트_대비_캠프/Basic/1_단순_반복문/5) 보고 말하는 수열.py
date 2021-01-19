
N = int(input())
element = '1'

for i in range(2,N+1): # N번째 원소를 찾기 위해
    temp = ''
    cnt = 1

    for idx in range(len(element)): # 원소의 문자를 하나하나 탐색
        # out of range거나 앞, 뒤의 문자가 다를 경우 temp에 저장 및 cnt 초기화
        if (idx + 1 == len(element)) or element[idx] != element[idx + 1]:
            temp += str(element[idx]) + str(cnt)
            cnt = 1
        else:
            cnt += 1

    # 축적해놓은 temp를 element에 모두 저장 후 다시 element를 반복문으로
    element = temp

print(element)