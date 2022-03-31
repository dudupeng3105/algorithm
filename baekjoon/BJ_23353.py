import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
horizon_dp = [[0 for _ in range(n)] for _ in range(n)]
vertical_dp = [[0 for _ in range(n)] for _ in range(n)]
diagonal_dp = [[0 for _ in range(n)] for _ in range(n)]
r_diagonal_dp = [[0 for _ in range(n)] for _ in range(n)]

def check(r, c, dis):
    n_i, n_j = r - dis[0], c - dis[1]
    cnt = 0
    while arr[n_i][n_j] == 1:
        n_i, n_j = n_i - dis[0], n_j - dis[1]
        cnt += 1

    return cnt


# 가로 체크, 세로 체크, 대각 체그
# 1. 가로체크
for i in range(n):
    white_flag = 0
    for j in range(n):
        cnt = 0
        if j == 0:
            if arr[i][j] == 1:  # 흑돌이면
                horizon_dp[i][j] = 1
            elif arr[i][j] == 2:  # 백돌이면
                horizon_dp[i][j] = 1
                white_flag = 1
            else:  # 빈칸이면
                continue
        else:
            if arr[i][j] == 1:  # 흑돌이면
                if arr[i][j-1] == 0:
                    horizon_dp[i][j] = 1
                else:  # horizon_dp[i][j-1] != 0
                    horizon_dp[i][j] = horizon_dp[i][j-1] + 1

            elif arr[i][j] == 2:  # 백돌이면
                if arr[i][j - 1] == 0:
                    horizon_dp[i][j] = 1
                    white_flag = 1
                else:  # horizon_dp[i][j-1] != 0
                    if white_flag:  # white_flag = 1
                        if arr[i][j-1] == 1:
                            # 앞에 1 몇개 인지 체크해야함
                            num_1 = check(i, j, [0, 1])
                            horizon_dp[i][j] = num_1 + 1
                        else:
                            horizon_dp[i][j] = 1
                    else: # white_flag = 0
                        horizon_dp[i][j] = horizon_dp[i][j - 1] + 1
                        white_flag = 1

            else:  # 빈칸이면
                horizon_dp[i][j] = 0
                white_flag = 0

        cnt += 1

for i in range(n):
    print(horizon_dp[i])
print()

# 세로 체크
for j in range(n):
    white_flag = 0
    for i in range(n):
        if i == 0:
            if arr[i][j] == 1:  # 흑돌이면
                vertical_dp[i][j] = 1
            elif arr[i][j] == 2:  # 백돌이면
                vertical_dp[i][j] = 1
                white_flag = 1
            else:  # 빈칸이면
                continue
        else:
            if arr[i][j] == 1:  # 흑돌이면
                if arr[i-1][j] == 0:
                    vertical_dp[i][j] = 1
                else:  # vertical_dp[i-1][j] != 0
                    vertical_dp[i][j] = vertical_dp[i-1][j] + 1

            elif arr[i][j] == 2:  # 백돌이면
                if arr[i-1][j] == 0:
                    vertical_dp[i][j] = 1
                    white_flag = 1
                else:  # vertical_dp[i-1][j] != 0
                    if white_flag:  # white_flag = 1
                        if arr[i-1][j] == 1:
                            # 앞에 1 몇개 인지 체크해야함
                            num_1 = check(i, j, [1, 0])
                            vertical_dp[i][j] = num_1 + 1
                        else:
                            vertical_dp[i][j] = 1
                    else: # white_flag = 0
                        vertical_dp[i][j] = vertical_dp[i-1][j] + 1
                        white_flag = 1

            else:  # 빈칸이면
                vertical_dp[i][j] = 0
                white_flag = 0

for i in range(n):
    print(vertical_dp[i])
print()

# 대각 체크(좌상 부분)
d = [-1, 1]
for i in range(n):
    white_flag = 0
    j = 0
    while i >= 0:  # 범위 벗어 날 때 까지
        if j == 0:
            if arr[i][j] == 1:  # 흑돌이면
                diagonal_dp[i][j] = 1
            elif arr[i][j] == 2:  # 백돌이면
                diagonal_dp[i][j] = 1
                white_flag = 1
            else:  # 빈칸이면
                i, j = i + d[0], j + d[1]
                continue
        else:
            if arr[i][j] == 1:  # 흑돌이면
                if arr[i + 1][j - 1] == 0:
                    diagonal_dp[i][j] = 1
                else:  # diagonal_dp[i + 1][j - 1] != 0
                    diagonal_dp[i][j] = diagonal_dp[i + 1][j - 1] + 1

            elif arr[i][j] == 2:  # 백돌이면
                if arr[i + 1][j - 1] == 0:
                    diagonal_dp[i][j] = 1
                    white_flag = 1
                else:  # diagonal_dp[i + 1][j - 1] != 0
                    if white_flag:  # white_flag = 1
                        if arr[i + 1][j - 1] == 1:
                            # 앞에 1 몇개 인지 체크해야함
                            num_1 = check(i, j, d)
                            diagonal_dp[i][j] = num_1 + 1
                        else:
                            diagonal_dp[i][j] = 1
                    else: # white_flag = 0
                        diagonal_dp[i][j] = diagonal_dp[i + 1][j - 1] + 1
                        white_flag = 1

            else:  # 빈칸이면
                diagonal_dp[i][j] = 0
                white_flag = 0

        i, j = i + d[0], j + d[1]

for i in range(n):
    print(diagonal_dp[i])
print()

# 대각 부분(우하)
d = [-1, 1]
for j in range(1, n):
    white_flag = 0
    i = n - 1
    while j < n:  # 범위 벗어 날 때 까지
        if i == n - 1:
            if arr[i][j] == 1:  # 흑돌이면
                diagonal_dp[i][j] = 1
            elif arr[i][j] == 2:  # 백돌이면
                diagonal_dp[i][j] = 1
                white_flag = 1
            else:  # 빈칸이면
                i, j = i + d[0], j + d[1]
                continue
        else:
            if arr[i][j] == 1:  # 흑돌이면
                if arr[i + 1][j - 1] == 0:
                    diagonal_dp[i][j] = 1
                else:  # diagonal_dp[i + 1][j - 1] != 0
                    diagonal_dp[i][j] = diagonal_dp[i + 1][j - 1] + 1

            elif arr[i][j] == 2:  # 백돌이면
                if arr[i + 1][j - 1] == 0:
                    diagonal_dp[i][j] = 1
                    white_flag = 1
                else:  # diagonal_dp[i + 1][j - 1] != 0
                    if white_flag:  # white_flag = 1
                        if arr[i + 1][j - 1] == 1:
                            # 앞에 1 몇개 인지 체크해야함
                            num_1 = check(i, j, d)
                            diagonal_dp[i][j] = num_1 + 1
                        else:
                            diagonal_dp[i][j] = 1
                    else: # white_flag = 0
                        diagonal_dp[i][j] = diagonal_dp[i + 1][j - 1] + 1
                        white_flag = 1

            else:  # 빈칸이면
                diagonal_dp[i][j] = 0
                white_flag = 0

        i, j = i + d[0], j + d[1]

for i in range(n):
    print(diagonal_dp[i])
print()

# 역대각 체크(우상 부분)
d = [1, 1] # 오른쪽 아래방향 대각선 진행
for j in range(n):
    white_flag = 0
    i = 0
    while j < n:  # 범위 벗어 날 때 까지
        if i == 0:
            if arr[i][j] == 1:  # 흑돌이면
                r_diagonal_dp[i][j] = 1
            elif arr[i][j] == 2:  # 백돌이면
                r_diagonal_dp[i][j] = 1
                white_flag = 1
            else:  # 빈칸이면
                i, j = i + d[0], j + d[1]
                continue
        else:
            if arr[i][j] == 1:  # 흑돌이면
                if arr[i - 1][j - 1] == 0:
                    r_diagonal_dp[i][j] = 1
                else:  # r_diagonal_dp[i - 1][j - 1] != 0
                    r_diagonal_dp[i][j] = r_diagonal_dp[i - 1][j - 1] + 1

            elif arr[i][j] == 2:  # 백돌이면
                if arr[i - 1][j - 1] == 0:
                    r_diagonal_dp[i][j] = 1
                    white_flag = 1
                else:  # r_diagonal_dp[i - 1][j - 1] != 0
                    if white_flag:  # white_flag = 1
                        if arr[i - 1][j - 1] == 1:
                            # 앞에 1 몇개 인지 체크해야함
                            num_1 = check(i, j, d)
                            r_diagonal_dp[i][j] = num_1 + 1
                        else:
                            r_diagonal_dp[i][j] = 1
                    else: # white_flag = 0
                        r_diagonal_dp[i][j] = r_diagonal_dp[i - 1][j - 1] + 1
                        white_flag = 1

            else:  # 빈칸이면
                r_diagonal_dp[i][j] = 0
                white_flag = 0

        i, j = i + d[0], j + d[1]


for i in range(n):
    print(r_diagonal_dp[i])
print()

# 역대각 체크(좌하 부분)
d = [1, 1]  # 오른쪽 아래방향 대각선 진행
for i in range(1, n):
    white_flag = 0
    j = 0
    while i < n:  # 범위 벗어 날 때 까지
        if j == 0:
            if arr[i][j] == 1:  # 흑돌이면
                r_diagonal_dp[i][j] = 1
            elif arr[i][j] == 2:  # 백돌이면
                r_diagonal_dp[i][j] = 1
                white_flag = 1
            else:  # 빈칸이면
                i, j = i + d[0], j + d[1]
                continue
        else:
            if arr[i][j] == 1:  # 흑돌이면
                if arr[i - 1][j - 1] == 0:
                    r_diagonal_dp[i][j] = 1
                else:  # r_diagonal_dp[i - 1][j - 1] != 0
                    r_diagonal_dp[i][j] = r_diagonal_dp[i - 1][j - 1] + 1

            elif arr[i][j] == 2:  # 백돌이면
                if arr[i - 1][j - 1] == 0:
                    r_diagonal_dp[i][j] = 1
                    white_flag = 1
                else:  # r_diagonal_dp[i - 1][j - 1] != 0
                    if white_flag:  # white_flag = 1
                        if arr[i - 1][j - 1] == 1:
                            # 앞에 1 몇개 인지 체크해야함
                            num_1 = check(i, j, d)
                            r_diagonal_dp[i][j] = num_1 + 1
                        else:
                            r_diagonal_dp[i][j] = 1
                    else: # white_flag = 0
                        r_diagonal_dp[i][j] = r_diagonal_dp[i - 1][j - 1] + 1
                        white_flag = 1

            else:  # 빈칸이면
                r_diagonal_dp[i][j] = 0
                white_flag = 0

        i, j = i + d[0], j + d[1]
#
for i in range(n):
    print(r_diagonal_dp[i])
print()


# max 값 구하기
ans = 0
for i in range(n):
    ans = max(ans, max(horizon_dp[i]))
    ans = max(ans, max(vertical_dp[i]))
    ans = max(ans, max(diagonal_dp[i]))
    ans = max(ans, max(r_diagonal_dp[i]))
print(ans)