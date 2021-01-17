for i in range(1,20):
    for j in range(1,20):
        if j%2 == 0:
            print('/ {0} * {1} = {2}'.format(i,j,i*j))
        else:
            print('{0} * {1} = {2}'.format(i,j,i*j),end=' ')
    print()