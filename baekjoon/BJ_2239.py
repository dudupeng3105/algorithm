import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

sudoku = [[] for _ in range(9)]
for i in range(9):
    sudoku[i] = list(map(int, input().rstrip()))

# 가로, 세로, 33 트루스맵
horizon_truth = [[False for __ in range(10)] for _ in range(9)]
vertical_truth = [[False for __ in range(10)] for _ in range(9)]
square_truth = [[[False for ___ in range(10)] for __ in range(3)] for _ in range(3)]
zero_pos = []
# 채우기
for i in range(9):
    for j in range(9):
        num = sudoku[i][j]
        if not num:
            zero_pos.append((i, j))
        horizon_truth[i][num] = True
        vertical_truth[j][num] = True
        square_truth[i // 3][j // 3][num] = True


def dfs(num_zero):
    if num_zero == last_num:  # 끝까지 완성함
        for i in range(9):
            print(*sudoku[i], sep='')

        exit(0)

    n_row, n_col = zero_pos[num_zero]  # 0 포지션
    for i in range(10):
        # i -> 0에 넣을 숫자
        if horizon_truth[n_row][i]:
            continue
        if vertical_truth[n_col][i]:
            continue
        if square_truth[n_row // 3][n_col // 3][i]:
            continue

        horizon_truth[n_row][i] = True
        vertical_truth[n_col][i] = True
        square_truth[n_row // 3][n_col // 3][i] = True
        sudoku[n_row][n_col] = i
        dfs(num_zero + 1)
        horizon_truth[n_row][i] = False
        vertical_truth[n_col][i] = False
        square_truth[n_row // 3][n_col // 3][i] = False
        sudoku[n_row][n_col] = 0


last_num = len(zero_pos)
dfs(0)
