import sys
from collections import deque

input = sys.stdin.readline


# dfs로 검은색안에 있는 흰색은 -1로 바꿔버림


def bfs(row, col):
    global cnt
    q = deque()
    q.append((row, col))
    visited[row][col] = cnt
    flag = 1
    while q:
        o_r, o_c = q.popleft()
        if o_r % 2:  # 짝수행
            drc = even
        else:
            drc = odd

        for dr, dc in drc:
            n_r, n_c = o_r + dr, o_c + dc
            if n_r < 0 or n_r > r - 1 or n_c < 0 or n_c > c - 1:  # 맵밖으로 나갈수 있다 -> 갇혀있지 않다
                flag = 0
                continue
            if not arr[n_r][n_c] and not visited[n_r][n_c]:  # 하얀맵이고 방문안함
                visited[n_r][n_c] = cnt
                q.append((n_r, n_c))

    return flag


# -1 처리
def painting(cnt):
    for a in range(r):
        for b in range(c):
            if visited[a][b] == cnt:
                arr[a][b] = -1  # 1로 처리함


# main
c, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
visited = [[0 for _ in range(c)] for __ in range(r)]
odd = [(0, -1), (0, 1), (-1, 1), (-1, 0), (1, 1), (1, 0)]
even = [(0, -1), (0, 1), (-1, -1), (-1, 0), (1, -1), (1, 0)]

cnt = 0
for i in range(r):
    for j in range(c):
        if not visited[i][j] and not arr[i][j]:
            cnt += 1
            flag = bfs(i, j)
            if flag:  # 검은색에 둘러싸인 하얀색이 있었으면
                painting(cnt)  # -1로 색칠


# 실 계산 =  검은 돌개수 * 6 - sigma(각 검은돌의 인접한 검은돌의 수)
black_num = 0
adjacent = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == 1:  # 검은돌
            black_num += 1
            # 인접 돌 계산
            if i % 2:  # 짝수행
                drc = even
            else:  # 홀수행
                drc = odd

            for dr, dc in drc:
                adj_r, adj_c = i + dr, j + dc
                if adj_r < 0 or adj_r > r - 1 or adj_c < 0 or adj_c > c - 1:
                    continue
                else:
                    if arr[adj_r][adj_c]:
                        adjacent += 1

print(black_num*6-adjacent)