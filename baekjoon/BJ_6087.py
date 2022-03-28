import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    global total_time, flag
    result_r, result_c, result_dist = -1, -1, 10000
    while q:
        r, c, dist = q.popleft()
        for i in range(4):
            n_r, n_c = r + dr[i], c + dc[i]
            if 0 <= n_r < n and 0 <= n_c < n and truth_map[n_r][n_c] == False \
                    and arr[n_r][n_c] <= shark_size:
                if arr[n_r][n_c] != 0 and arr[n_r][n_c] < shark_size and dist <= result_dist:  # 먹을수있는 물곡
                    if result_dist == 10000:  # 처음 만난 먹을 수 있는물고기
                        truth_map[n_r][n_c] = True
                        total_time = total_time + dist + 1
                        result_r, result_c = n_r, n_c
                        result_dist = dist
                    else:  # 이전 것이 있음
                        truth_map[n_r][n_c] = True
                        if n_r < result_r:
                            result_r, result_c = n_r, n_c
                        elif n_r == result_r:
                            if n_c < result_c:
                                result_r, result_c = n_r, n_c
                        else:  # 결과유지
                            continue

                else:
                    if dist < result_dist:
                        truth_map[n_r][n_c] = True
                        q.append((n_r, n_c, dist+1))

    # 다 돌았는데 먹은게 없다
    if result_dist == 10000:
        flag = 1
    return result_r, result_c


n = int(input())
arr = [[0 for _ in range(n)] for __ in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

flag_0 = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            s_r, s_c = i, j
            flag_0 = 1
            break
    if flag_0:
        break


flag = 0
shark_size = 2
shark_cnt = 0
total_time = 0
# 상, 좌, 우, 하
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

while True:
    truth_map = [[False for _ in range(n)] for __ in range(n)]
    q = deque()
    q.append((s_r, s_c, 0))
    truth_map[s_r][s_c] = True
    arr[s_r][s_c] = 0  # 시작위치 0 처리
    s_r, s_c = bfs()
    if flag:
        break
    else:
        shark_cnt += 1
    if shark_cnt == shark_size:
        shark_cnt = 0
        shark_size += 1

print(total_time)