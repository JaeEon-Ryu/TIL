'''
모든 배열 0으로 할당
1. 모든 배열 순회 -> 0이라면 숫자 삽입 후 2번 무한반복
2. 1번에서 찾았던 배열 위치에서 한칸 아래 왼쪽 ( 왼쪽으로 대각선 방향 )
원소로 접근 가능하다면 접근하고 숫자 삽입
'''

n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
num = 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            arr[i][j] = num

            num += 1
            x = i + 1
            y = j - 1


            while x < n and y >= 0:
                arr[x][y] = num

                num += 1
                x += 1
                y -= 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()

