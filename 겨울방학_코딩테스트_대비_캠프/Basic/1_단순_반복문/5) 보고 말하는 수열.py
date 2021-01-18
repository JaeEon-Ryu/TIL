N = int(input())

element = '1'
cnt = 1
origin = '1'

for i in range(2, N + 1):

    temp = ''
    for idx in range(len(element)-1):
        next = idx + 1
        if next == len(element): # out of length

        elif element[next] != origin : # 다를 경우

        else : # 같을 경우


    element = temp
    print(element)

#print(element)
