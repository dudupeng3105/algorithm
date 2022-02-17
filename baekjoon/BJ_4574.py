import sys
from collections import deque

sudoku_map = [[0 for _ in range(9)] for __ in range(9)]
row_num = [[False for _ in range(10)] for __ in range(9)]
col_num = [[False for _ in range(10)] for __ in range(9)]
box_num = [[[False for _ in range(10)] for _ in range(3)] for __ in range(3)]  # 9 * 3 * 3
# 도미노 체커도 필요
domino_num = [[False for _ in range(10)] for __ in range(10)]
# 같은 수는 첨부터 True 처리
for i in range(10):
    domino_num[i][i] = True

d_num = int(sys.stdin.readline())
alpha_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
# zero_pos = []
for i in range(d_num):
    # sudoku_map[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    u, lu, v, lv = map(str, sys.stdin.readline().rstrip().split())
    u = int(u)
    v = int(v)
    r_1, c_1 = alpha_dict[lu[0]], int(lu[1]) -1
    r_2, c_2 = alpha_dict[lv[0]], int(lv[1]) -1
    # 맵에 넣기
    sudoku_map[r_1][c_1] = u
    print(r_2, c_2)
    sudoku_map[r_2][c_2] = v
    # True 처리
    row_num[r_1][u] = True
    row_num[r_2][v] = True
    col_num[c_1][u] = True
    col_num[c_2][v] = True
    box_num[r_1 // 3][c_1 // 3][u] = True
    box_num[r_2 // 3][c_2 // 3][v] = True
    domino_num[u][v] = True
    domino_num[v][u] = True

# 숫자 1~9 받기
temp_lst = list(map(str, sys.stdin.readline().rstrip().split()))
for i in range(9):
    r_1, c_1 = alpha_dict[temp_lst[i][0]], int(temp_lst[i][1]) - 1
    sudoku_map[r_1][c_1] = i + 1
    row_num[r_1][i+1] = True
    col_num[c_1][i+1] = True
    box_num[r_1 // 3][c_1 // 3][i+1] = True

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# 빈칸을 하나씩 탐색하는것이 맞는듯
# 81
# idx // 9 = row
# idx % 9 = col

def dfs(idx):  # 짝수 depth마다 도미노 체커 해야하지 않나...
    prev = sudoku_map[row][col]
    for i in range(9):
        print(sudoku_map[i])
    print()
    for d in range(4):
        n_row, n_col, n_depth = row + dr[d], col + dc[d], depth + 1
        if n_row > 8 or n_row < 0 or n_col > 8 or n_col < 0:
            continue
        if sudoku_map[n_row][n_col]:  # 이미 채워져 있으면
            continue

        row = idx // 9
        col = idx % 9
        # 도미노 단위로 넣음 (가로, 가로역순, 세로, 세로 역순)
        for num1 in range(1, 10):
            for num2 in range(1, 10):
                # 더 가지 않을 조건
                if domino_num[num1][num2]:
                    continue

                if row_num[row][num1]:
                    continue
                if col_num[col][num1]:
                    continue
                if box_num[row // 3][col // 3][num1]:
                    continue
                if row_num[row][num2]:
                    continue
                if col_num[col][num2]:
                    continue
                if box_num[row // 3][col // 3][num2]:
                    continue
                #


            # 가로 num1, num2
            # i -> 빈칸에 넣을 숫자
            row_num[n_row][i] = True
            col_num[n_col][i] = True
            box_num[n_row // 3][n_col // 3][i] = True
            sudoku_map[n_row][n_col] = i
            if n_depth % 2 == 0:  # 끝까지 완성함
                if domino_num[prev][i]:  # 이미 있는 조각
                    continue
                else:
                    domino_num[prev][i] = True
                    domino_num[i][prev] = True
            print(n_row, n_col, n_depth)
            dfs(n_row, n_col, n_depth)
            # 들어갔는데 넣을 숫자가 없었으면 밑에 코드 실행 -> 백트래킹
            row_num[n_row][i] = False
            col_num[n_col][i] = False
            box_num[n_row // 3][n_col // 3][i] = False
            sudoku_map[n_row][n_col] = 0
            if n_depth % 2 == 0:  # 끝까지 완성함
                domino_num[prev][i] = False
                domino_num[i][prev] = False

for i in range(1, 10):
    if row_num[0][i]:
        continue
    if col_num[0][i]:
        continue
    if box_num[0 // 3][0 // 3][i]:
        continue
    row_num[0][i] = True
    col_num[0][i] = True
    box_num[0 // 3][0 // 3][i] = True
    sudoku_map[0][0] = i
    dfs(0,0,1)
    row_num[0][i] = False
    col_num[0][i] = False
    box_num[0 // 3][0 // 3][i] = False
    sudoku_map[0][0] = 0






for i in range(9):
    print(sudoku_map[i])

