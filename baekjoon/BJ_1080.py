n, m = map(int, input().split())
arr1 = [list(map(int, input())) for _ in range(n)]
arr2 = [list(map(int, input())) for _ in range(n)]


# 한번에 뒤집을 수 있는 칸이 3*3 크기
def flip(row, col):
    for dx in range(3):
        for dy in range(3):
            arr1[row+dx][col+dy] = 1 - arr1[row+dx][col+dy]

    return arr1


cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if arr1[i][j] != arr2[i][j]:
            arr1 = flip(i, j)
            cnt += 1


if arr1 == arr2:
    print(cnt)
else:
    print(-1)
