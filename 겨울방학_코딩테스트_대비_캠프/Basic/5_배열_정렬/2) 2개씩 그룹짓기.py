N = int(input())
elements = list(map(int,input().split()))
elements.sort()
max_value = 0

for idx in range(len(elements)//2):
    value = elements[idx] + elements[-idx-1]
    max_value = max(max_value,value)

print(max_value)