'''
제일 싸게 사고, 제일 비싸게 팔기

'''

n = int(input())
price_list = list(map(int,input().split()))

max_profit = 0
min_price = price_list[0]

for i in range(1,n):
    profit = price_list[i] - min_price

    if profit > max_profit:
        max_profit = profit
    if price_list[i] < min_price:
        min_price = price_list[i]

print(max_profit)

