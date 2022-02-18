import sys

sys.setrecursionlimit(10 ** 6)


def truth_operation(row1, col1, row2, col2, num1, num2, T_F):
    row_num[row1][num1] = T_F
    col_num[col1][num1] = T_F
    box_num[row1 // 3][col1 // 3][num1] = T_F
    row_num[row2][num2] = T_F
    col_num[col2][num2] = T_F
    box_num[row2 // 3][col2 // 3][num2] = T_F
    if T_F:
        sudoku_map[row1][col1] = num1
        sudoku_map[row2][col2] = num2
    else:  # False
        sudoku_map[row1][col1] = 0
        sudoku_map[row2][col2] = 0


def exist_check(row1, col1, row2, col2, num1, num2):
    if row_num[row1][num1]:
        return True
    if col_num[col1][num1]:
        return True
    if box_num[row1 // 3][col1 // 3][num1]:
        return True
    if row_num[row2][num2]:
        return True
    if col_num[col2][num2]:
        return True
    if box_num[row2 // 3][col2 // 3][num2]:
        return True

    return False


def dfs(idx):
    global flag
    if flag:
        return
    if idx == 81:
        print('Puzzle ' + str(k))
        for i in range(9):
            print(*sudoku_map[i], sep='')
        flag = True
        return

    row = idx % 9
    col = idx // 9

    if sudoku_map[row][col]:
        dfs(idx + 1)
        return
    else:
        # 도미노 단위로 넣음 (가로, 가로역순, 세로, 세로 역순)
        for d in range(2):  # 상하, 좌우 설정
            r_1, c_1 = row, col
            r_2, c_2 = row + dr[d], col + dc[d]
            # print(r_2, c_2)
            if r_2 > 8 or c_2 > 8:
                continue
            if sudoku_map[r_2][c_2]:
                continue

            for num1 in range(1, 9):
                for num2 in range(num1+1, 10, 1):
                    # 더 가지 않을 조건
                    if domino_num[num1][num2]:
                        continue
                    domino_num[num1][num2] = True
                    domino_num[num2][num1] = True
                    for i in range(2):  # 순방향, 역방향 숫자
                        if i == 0:
                            # case 1 원래 순서
                            if exist_check(r_1, c_1, r_2, c_2, num1, num2):
                                continue
                            truth_operation(r_1, c_1, r_2, c_2, num1, num2, True)
                            dfs(idx + 1)
                            truth_operation(r_1, c_1, r_2, c_2, num1, num2, False)
                        else:  # 역순
                            if exist_check(r_1, c_1, r_2, c_2, num2, num1):
                                continue
                            truth_operation(r_1, c_1, r_2, c_2, num2, num1, True)
                            dfs(idx + 1)
                            truth_operation(r_1, c_1, r_2, c_2, num2, num1, False)
                    domino_num[num1][num2] = False
                    domino_num[num2][num1] = False
        return


k = 0
while True:
    d_num = int(sys.stdin.readline())
    k += 1
    if d_num == 0:
        break
    else:
        sudoku_map = [[0 for _ in range(9)] for __ in range(9)]
        row_num = [[False for _ in range(10)] for __ in range(9)]
        col_num = [[False for _ in range(10)] for __ in range(9)]
        box_num = [[[False for _ in range(10)] for _ in range(3)] for __ in range(3)]  # 9 * 3 * 3
        # 도미노 체커도 필요
        domino_num = [[False for _ in range(10)] for __ in range(10)]
        # 같은 수는 첨부터 True 처리
        for i in range(10):
            domino_num[i][i] = True
        alpha_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
        for i in range(d_num):
            u, lu, v, lv = map(str, sys.stdin.readline().rstrip().split())
            u = int(u)
            v = int(v)
            r_1, c_1 = alpha_dict[lu[0]], int(lu[1]) - 1
            r_2, c_2 = alpha_dict[lv[0]], int(lv[1]) - 1
            # 맵에 넣기
            # True 처리
            truth_operation(r_1, c_1, r_2, c_2, u, v, True)
            domino_num[u][v] = True
            domino_num[v][u] = True

        # 숫자 1~9 받기
        temp_lst = list(map(str, sys.stdin.readline().rstrip().split()))
        for i in range(9):
            r_1, c_1 = alpha_dict[temp_lst[i][0]], int(temp_lst[i][1]) - 1
            sudoku_map[r_1][c_1] = i + 1
            row_num[r_1][i + 1] = True
            col_num[c_1][i + 1] = True
            box_num[r_1 // 3][c_1 // 3][i + 1] = True

        dr = [1, 0]
        dc = [0, 1]

        flag = False
        dfs(0)