import sys

input = sys.stdin.readline


# 일단 45도 회전부터
def rotate_45(arr, row, col):
    new_arr = [[' ' for _ in range(row * col)] for __ in range(row * col)]
    for i in range(row):
        for j in range(col):
            new_arr[j + i][row - i - 1 + j] = arr[i][j]

    return new_arr


# 90도 회전
def rotate_90(arr, row, col):
    new_arr = [[' ' for _ in range(row)] for __ in range(col)]
    for i in range(row):
        for j in range(col):
            new_arr[j][row-i-1] = arr[i][j]

    return new_arr


r, c = map(int, input().split())
given_arr = [list(input().rstrip()) for _ in range(r)]
deg = int(input())
num_op_90 = deg // 90
num_op_45 = (deg - num_op_90 * 90) // 45

for _ in range(num_op_90):
    given_arr = rotate_90(given_arr, r, c)
    r, c = c, r  # axis change

for _ in range(num_op_45):
    given_arr = rotate_45(given_arr, r, c)

for i in range(r*c):
    try:
        this_str = "".join(given_arr[i]).rstrip()
        if not this_str:
            break
        else:
            print(this_str)
    except:
        break

