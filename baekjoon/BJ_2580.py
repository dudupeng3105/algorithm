import sys

sudoku_map = [[0 for _ in range(9)] for __ in range(9)]
row_num = [[False for _ in range(10)] for __ in range(9)]
col_num = [[False for _ in range(10)] for __ in range(9)]
box_num = [[[False for _ in range(10)] for _ in range(3)] for __ in range(3)] # 9 * 3 * 3
zero_pos = []
for i in range(9):
    sudoku_map[i] = list(map(int, sys.stdin.readline().rstrip().split()))

# 채워져 있는 숫자 수 세기
for i in range(9):
    for j in range(9):
        sudoku_num = sudoku_map[i][j]
        if sudoku_num == 0: # 0 개수 만큼 뺌
            zero_pos.append((i, j))
        row_num[i][sudoku_num] = True
        col_num[j][sudoku_num] = True
        box_num[i//3][j//3][sudoku_num] = True

last_num = len(zero_pos)

def dfs(num_zero):
    if num_zero == last_num: # 끝까지 완성함
        for i in range(9):
            print(*sudoku_map[i])

        exit(0)

    n_row, n_col = zero_pos[num_zero] # 0 포지션
    for i in range(10):
        # i -> 0에 넣을 숫자
        if row_num[n_row][i]:
            continue
        if col_num[n_col][i]:
            continue
        if box_num[n_row // 3][n_col // 3][i]:
            continue

        row_num[n_row][i] = True
        col_num[n_col][i] = True
        box_num[n_row // 3][n_col // 3][i] = True
        sudoku_map[n_row][n_col] = i
        dfs(num_zero+1)
        # 들어갔는데 넣을 숫자가 없었으면 밑에 코드 실행 -> 백트래킹
        row_num[n_row][i] = False
        col_num[n_col][i] = False
        box_num[n_row // 3][n_col // 3][i] = False
        sudoku_map[n_row][n_col] = 0

dfs(0)