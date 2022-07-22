import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0 for _ in range(M)] for __ in range(N)]

# queen(1)
temp = list(map(int, input().split()))
for i in range(temp[0]):
    arr[temp[2 * i + 1]-1][temp[2 * i + 2]-1] = 1

# knight(2)
temp = list(map(int, input().split()))
for i in range(temp[0]):
    arr[temp[2 * i + 1]-1][temp[2 * i + 2]-1] = 2

# pawn(3)
temp = list(map(int, input().split()))
for i in range(temp[0]):
    arr[temp[2 * i + 1]-1][temp[2 * i + 2]-1] = 3

# 구현 해야함
safe_zone = [[False for _ in range(M)] for __ in range(N)]
for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            continue

        elif arr[i][j] == 1:  # queen
            safe_zone[i][j] = True
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                n_r, n_c = i, j
                n_r, n_c = n_r + dr, n_c + dc
                while 0 <= n_r < N and 0 <= n_c < M:
                    if arr[n_r][n_c]:
                        break
                    else:
                        safe_zone[n_r][n_c] = True

                    n_r, n_c = n_r + dr, n_c + dc

        elif arr[i][j] == 2:  # knight
            safe_zone[i][j] = True
            for dr, dc in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
                n_r, n_c = i + dr, j + dc
                if 0 <= n_r < N and 0 <= n_c < M:
                    safe_zone[n_r][n_c] = True

        else:  # 3
            safe_zone[i][j] = True

# 개수 구하기
ans = 0
for i in range(N):
    for j in range(M):
        if not safe_zone[i][j]:
            ans += 1


print(ans)