a,b = map(int, input().split())

digit = 0
result = (str(a//b) + ".")
rest = a%b

while digit < 20:
    rest *= 10
    result += str(rest//b)
    rest %= b
    digit += 1

print(result)