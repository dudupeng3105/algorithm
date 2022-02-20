import sys
from collections import deque


def bfs(r, c):  # 0 그룹 찾기
    cnt = 0
    q = deque()
    q.append((r, c))
    visited[r][c] = True  # 방문 및 길이 처리
    zeros[r][c] = group
    cnt += 1
    while q:
        row, col = q.popleft()

        for i in range(4):
            n_row, n_col = row + dr[i], col + dc[i]
            if n_row < 0 or n_row > n - 1 or n_col < 0 or n_col > m - 1:
                continue
            if arr[n_row][n_col]:  # 벽이면
                continue
            if visited[n_row][n_col]:  # 이미 경로 있으면
                continue

            visited[n_row][n_col] = True
            zeros[n_row][n_col] = group
            cnt += 1
            q.append((n_row, n_col))

    return cnt


n, m = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(m)] for __ in range(n)]
wall_lst = []

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().rstrip()))

visited = [[False for _ in range(m)] for __ in range(n)]
zeros = [[0 for _ in range(m)] for __ in range(n)]
group = 1
group_dict = {}
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
# 벽 리스트 및 제로 그룹 만들기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            wall_lst.append((i, j))  # 벽 리스트에 추가
        else:  # arr[i][j] 0 이면 제로 그룹 확인 by bfs
            if visited[i][j]:
                continue
            visited[i][j] = True
            group_cnt = bfs(i, j)
            group_dict[group] = group_cnt
            group += 1

# 이동할 수 있는 칸 구하기
for r, c in wall_lst:
    group_set = set()  # 중복 그룹있을수도 있음
    for i in range(4):
        n_r, n_c = r + dr[i], c + dc[i]
        if n_r < 0 or n_r > n - 1 or n_c < 0 or n_c > m - 1:  # 범위 밖이면 무시
            continue
        if not zeros[n_r][n_c]:  # 벽이면
            continue
        # 0 일 때
        group_set.add(zeros[n_r][n_c])

    for group_i in group_set:
        arr[r][c] += group_dict[group_i]
    arr[r][c] = arr[r][c] % 10

for i in range(n):
    print(*arr[i], sep='')


# 블러드 필 공부