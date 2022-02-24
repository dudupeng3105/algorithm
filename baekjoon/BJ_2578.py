arr = [[0 for _ in range(5)] for __ in range(5)]
call_number = []
row_checker = [0, 0, 0, 0, 0]
col_checker = [0, 0, 0, 0, 0]
diagonal_checker = [0, 0]
for i in range(5):
    arr[i] = list(map(int, input().split()))

for j in range(5):
    call_number += map(int, input().split())

# 번호 부름
bingo = 0
for k in range(25):
    this_num = call_number[k]
    for i in range(5):
        flag = 0
        for j in range(5):
            if arr[i][j] == this_num:
                row_checker[i] += 1
                col_checker[j] += 1
                if i + j == 4:
                    diagonal_checker[1] += 1
                if i == j:
                    diagonal_checker[0] += 1
                flag = 1
                break
        if flag:
            break

    if diagonal_checker[1] == 5:
        diagonal_checker[1] += 1  # 더이상 걸리지 않게
        bingo += 1
    if diagonal_checker[0] == 5:
        diagonal_checker[0] += 1  # 더이상 걸리지 않게
        bingo += 1
    if row_checker[i] == 5:
        bingo += 1
    if col_checker[j] == 5:
        bingo += 1
    if bingo >= 3:
        print(k+1)
        break

