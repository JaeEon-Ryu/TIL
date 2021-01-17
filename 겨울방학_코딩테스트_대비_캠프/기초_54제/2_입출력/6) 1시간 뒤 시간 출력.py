'''
ex) 23시 8분일 경우, 문제에서는 23:08이 아닌 23:8
따라서 콜론 (' : ')을 기준으로 시간을 재정의함
'''


time = input()

for idx,t in enumerate(time):
    if t == ':':
        time = str(int(time[:idx])+1) + time[idx:]
        break

print(time)