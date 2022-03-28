test_case = int(input())
displacement = [(0, 1), (1, 1), (1, 0), (1, -1), \
                (0, -1), (-1, 1), (-1, 0), (-1, -1)]


def check_target(row, col, direction, check_color):
    temp = []
    n_r = row + displacement[direction][0]
    n_c = col + displacement[direction][1]
    while True:
        if 0 <= n_r < n and 0 <= n_c < n:
            if arr[n_r][n_c] == 0:
                return []
            if arr[n_r][n_c]:  # 0 아니면
                if arr[n_r][n_c] == check_color:
                    return temp
                else:  # 다른 색
                    temp.append((n_r, n_c))
                    n_r += displacement[direction][0]
                    n_c += displacement[direction][1]
                    continue

        else:  # 범위 밖이면
            return []


def othello_operation(r, c, color):
    arr[r][c] = color
    for i in range(8):
        target_temp = check_target(r, c, i, color)
        for c_r, c_c in target_temp:
            arr[c_r][c_c] = color


for tc in range(1, test_case + 1):
    n, m = map(int, input().split())
    arr = [[0 for _ in range(n)] for __ in range(n)]
    # 정중앙 두기
    arr[n // 2][n // 2] = 2
    arr[n // 2 - 1][n // 2] = 1
    arr[n // 2][n // 2 - 1] = 1
    arr[n // 2 - 1][n // 2 - 1] = 2

    for _ in range(m):
        r, c, color = map(int, input().split())
        othello_operation(r-1, c-1, color)

    white_num = 0
    black_num = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                black_num += 1
            elif arr[i][j] == 2:
                white_num += 1
    print(f'#{tc} {black_num} {white_num}')




