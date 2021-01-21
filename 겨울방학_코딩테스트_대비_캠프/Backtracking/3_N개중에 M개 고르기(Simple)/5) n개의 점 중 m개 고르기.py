n, m = map(int,input().split())
points = []
possible_index = []
possible_index2 = []
global result
global max_val
global max_list
max_list =[]
max_val = 0
result = []
for i in range(n):
    points.append(list(map(int,input().split())))


def first_combination(curr_idx, cnt):
    global max_list
    global max_val
    global result
    if curr_idx == n:
        if cnt == m:
            ''':type
            print_combination()
            '''
            print(possible_index)
            second_combination(0,0)
            if result:
                if max_val < max(result):
                    max_val = max(result)
                    max_list.append(max_val)
            result = []

        return

    possible_index.append(curr_idx)
    first_combination(curr_idx + 1, cnt + 1)
    possible_index.pop()

    first_combination(curr_idx + 1, cnt)

def second_combination(curr_idx, cnt):

    if curr_idx == len(possible_index):
        if cnt == 2:
            ''':type
            print_combination()
            '''
            print(possible_index2)
            idx_1 = possible_index[0]
            idx_2 = possible_index[1]
            dist = (points[idx_1][0] - points[idx_2][0]) ** 2 +\
                   (points[idx_1][1] - points[idx_2][1]) ** 2
            result.append(dist)

        return

    possible_index2.append(possible_index[curr_idx])
    second_combination(curr_idx + 1, cnt + 1)
    possible_index2.pop()

    second_combination(curr_idx + 1, cnt)


first_combination(0, 0)
print(min(max_list))





'''
4 3

1 1
4 4
3 5
2 2

'''


'''
3 3
1 1
4 4
5 3

20

4 3
1 1
4 4
5 3
0 0

20
'''