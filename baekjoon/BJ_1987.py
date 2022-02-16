# import sys
#
#
# def dfs(row, col, depth):
#     global max_path
#
#     if depth > max_path:
#         max_path = depth
#
#     for i in range(4):
#         n_row, n_col = row + dr[i], col + dc[i]
#         if n_row > r-1 or n_row < 0 or n_col > c-1 or n_col < 0:
#             continue
#         ascii_char = ord(board[n_row][n_col]) - 65
#         if alpha_lst[ascii_char]:  # True
#             continue
#
#         board_truth[n_row][n_col] = True
#         alpha_lst[ascii_char] = True
#         dfs(n_row, n_col, depth+1)
#         board_truth[n_row][n_col] = False
#         alpha_lst[ascii_char] = False
#
#
# r, c = map(int, sys.stdin.readline().split())
# board = [[] for __ in range(r)]
# for i in range(r):
#     board[i] = list(sys.stdin.readline().rstrip())
#
#
# alpha_lst = [False for _ in range(26)]
# board_truth = [[False for _ in range(c)] for __ in range(r)] # 방문 체크용
#
# dr = [1, 0, -1, 0]
# dc = [0, 1,  0, -1]
# max_path = 0
#
# alpha_lst[ord(board[0][0])-65] = True  # ord('A') =65
# dfs(0, 0, 1)
# print(max_path)
#
#
# # 딕트라고 빠른건아님, 리스트도 값 가져오는건 O(1)임

import sys

# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])

    while q:
        x, y, ans = q.pop()
        print(ans)

        # 좌우상하 갈 수 있는지 살펴본다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
BFS(0, 0)
print(answer)