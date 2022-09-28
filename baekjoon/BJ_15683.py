import sys
from itertools import product

input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
cctv_arr = []
wall_num = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] in [1, 2, 3, 4, 5]:
            cctv_arr.append((i, j))
        elif arr[i][j] == 6:
            wall_num += 1

cctv_num = len(cctv_arr)
ans = 0
for seq in product([1, 2, 3, 4], repeat=cctv_num):
    temp = set()  # 감시할 수 있는 곳을 넣을 거임
    for i in range(cctv_num):
        r, c = cctv_arr[i]
        cctv_type = arr[r][c]
        rotate_type = seq[i]
        if cctv_type == 1:
            if rotate_type == 1: # 상
                dr, dc = -1, 0
            elif rotate_type == 2: # 우
                dr, dc = 0, 1
            elif rotate_type == 3: # 하
                dr, dc = 1, 0
            else: # 좌
                dr, dc = 0, -1

            while 0 <= r < R and 0 <= c < C and arr[r][c] != 6:
                temp.add(r*C+c)
                r, c = r + dr, c + dc

        elif cctv_type == 2:
            if rotate_type == 1: # 좌우
                n_r, n_c = r, c
                dr, dc = 0, -1
                # 좌
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = 0, 1
                # 우
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc

            elif rotate_type == 2: # 상하
                n_r, n_c = r, c
                dr, dc = -1, 0
                # 상
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = 1, 0
                # 하
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
            else:
                continue

        elif cctv_type == 3:
            if rotate_type == 1: # 상우
                n_r, n_c = r, c
                dr, dc = -1, 0
                # 상
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = 0, 1
                # 우
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc

            elif rotate_type == 2: # 우하
                n_r, n_c = r, c
                dr, dc = 0, 1
                # 상
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = 1, 0
                # 하
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
            elif rotate_type == 3:  # 좌하
                n_r, n_c = r, c
                dr, dc = 0, -1
                # 좌
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = 1, 0
                # 하
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
            else: # 4 좌상
                n_r, n_c = r, c
                dr, dc = 0, -1
                # 좌
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = -1, 0
                # 상
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc

        elif cctv_type == 4:
            if rotate_type == 1: # 좌상우
                n_r, n_c = r, c
                dr, dc = 0, -1
                # 좌
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = -1, 0
                # 상
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = 0, 1
                # 우
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc

            elif rotate_type == 2: # 상우하
                n_r, n_c = r, c
                dr, dc = 0, 1
                # 상
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = 0, 1
                # 우
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = 1, 0
                # 하
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
            elif rotate_type == 3:  # 좌하우
                n_r, n_c = r, c
                dr, dc = 0, -1
                # 좌
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = 1, 0
                # 하
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = 1, 0
                # 하
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
            else: # 4 하좌상
                n_r, n_c = r, c
                dr, dc = 1, 0
                # 하
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = 0, -1
                # 좌
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = -1, 0
                # 상
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc

        else: # cctv_type == 5
            if rotate_type == 1:  # 상하좌우
                n_r, n_c = r, c
                dr, dc = 0, -1
                # 좌
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = -1, 0
                # 상
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = 1, 0
                # 하
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
                n_r, n_c = r, c
                dr, dc = 0, 1
                # 우
                while 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] != 6:
                    temp.add(n_r * C + n_c)
                    n_r, n_c = n_r + dr, n_c + dc
            else:
                continue

    ans = max(ans, len(temp))

#print(ans)
print(R*C-ans-wall_num)