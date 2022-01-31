N, M = map(int, input().split())
arr = [[0 for _ in range(M)] for __ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input()))

result = 0

for i in range(2 **(N*M)):
    total = 0
    # 가로 계산
    for row in range(N):
        sigma_row = 0
        for col in range(M):
            position = row * M + col
            if i & (1 << position) != 0:
                sigma_row = 10 * sigma_row + arr[row][col]
            else:
                total += sigma_row
                sigma_row = 0
        total += sigma_row
    # 세로 계산
    for col in range(M):
        sigma_col = 0
        for row in range(N):
            position = row * M + col
            if i & (1 << position) == 0:
                sigma_col = 10 * sigma_col + arr[row][col]
            else:
                total += sigma_col
                sigma_col = 0
        total += sigma_col

    result = max(result, total)
print(result)