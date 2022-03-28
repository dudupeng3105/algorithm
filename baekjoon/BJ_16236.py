import sys
from collections import deque
input = sys.stdin.readline


# 상, 좌, 우, 하
def direction(a):
    if a == 1:
        return -1, 0
    elif a == 2:
        return 0, -1
    elif a == 3:
        return 0, 1
    else:
        return 1, 0


def bfs():
    q = deque()
    # (행, 열, 전 방향) 정도면 ㅇㅋ
    # 거리는 상관 없음
    q.append((s_r, s_c))
    mirror_map[s_r][s_c] = 0
    while q:
        p_r, p_c = q.popleft()
        for i in range(1, 5):
            dr, dc = direction(i)
            n_r, n_c = p_r + dr, p_c + dc
            while 0 <= n_r < r and 0 <= n_c < c and arr[n_r][n_c] != '*':
                if not mirror_map[n_r][n_c]:
                    mirror_map[n_r][n_c] = mirror_map[p_r][p_c] + 1
                    if arr[n_r][n_c] == 'C':
                        l_r, l_c = n_r, n_c
                    q.append((n_r, n_c))
                n_r, n_c = n_r + dr, n_c + dc

    return l_r, l_c


c, r = map(int, input().split())
arr = ['' for __ in range(r)]

for i in range(r):
    arr[i] = input()

flag_0 = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'C':
            s_r, s_c = i, j
            flag_0 = 1
            break
    if flag_0:
        break

mirror_map = [[0 for _ in range(c)] for __ in range(r)]
result_r, result_c = bfs()
print(mirror_map[result_r][result_c] - 1)
