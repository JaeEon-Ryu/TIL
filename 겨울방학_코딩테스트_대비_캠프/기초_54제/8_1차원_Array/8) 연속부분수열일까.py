n1, n2 = map(int,input().split())

n1_nums = ''.join(input().split())
n2_nums = ''.join(input().split())

if n2_nums in n1_nums:
    print('Yes')
else:
    print('No')