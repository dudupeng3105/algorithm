import sys

sudoku_map = [[0 for _ in range(9)] for __ in range(9)]
row_num = [[False for _ in range(10)] for __ in range(9)]
col_num = [[False for _ in range(10)] for __ in range(9)]
box_num = [[[False for _ in range(10)] for _ in range(3)] for __ in range(3)]  # 9 * 3 * 3
# 도미노 체커도 필요
domino_num = [[False for _ in range(9)] for __ in range(9)]

d_num = int(sys.stdin.readline())
alpha_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
# zero_pos = []
for i in range(d_num):
    # sudoku_map[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    u, lu, v, lv = map(str, sys.stdin.readline().rstrip().split())
    u = int(u)
    v = int(v)
    r_1, c_1 = alpha_dict[lu[0]], int(lu[1])-1
    print(r_1, c_1)
    r_2, c_2 = alpha_dict[lv[0]], int(lv[1])-1
    print(r_2, c_2)
    # True 처리
    row_num[r_1][u] = True
    row_num[r_2][v] = True
    col_num[c_1][u] = True
    col_num[c_2][v] = True
    box_num[r_1 // 3][c_1 // 3][u] = True
    box_num[r_2 // 3][c_2 // 3][v] = True

# 숫자 1~9 받기
temp_lst = list(map(str, sys.stdin.readline().rstrip().split()))
for i in range(9):
    r_1, c_1 = alpha_dict[temp_lst[i][0]], int(temp_lst[i][1]) - 1
    row_num[r_1][i + 1] = True
    col_num[c_1][i + 1] = True
    box_num[r_1 // 3][c_1 // 3][i + 1] = True


for i in range(9):
    print(row_num[i])

print()
for j in range(9):
    print(col_num[j])
print()
for i in range(3):
    print(box_num[i])