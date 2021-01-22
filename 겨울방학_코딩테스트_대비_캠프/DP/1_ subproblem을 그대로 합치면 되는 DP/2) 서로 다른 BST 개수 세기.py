'''
n == 1 : 1  #         1         => 1
n == 2 : 2  #       1   1       => 2
n == 3 : 5  #     2   1   2     => 5
n == 4 : 14 #   5   2   2   5   => 14

'''

n = int(input())
num_of_bst = [0 for i in range(n+1)]

num_of_bst[0] = 1
num_of_bst[1] = 1

for i in range(2,n+1):
    for j in range(i):
        num_of_bst[i] += num_of_bst[j] * num_of_bst[i-j-1]
        # print('num_of_bst[%d] * num_of_bst[%d] = %d * %d = %d'
        #       %(j,i-j-1,num_of_bst[j],num_of_bst[i-j-1]
        #         ,num_of_bst[j]*num_of_bst[i-j-1]))
        # print()
    #print()

print(num_of_bst[n])