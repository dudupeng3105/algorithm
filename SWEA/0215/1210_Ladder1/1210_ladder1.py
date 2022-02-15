import sys


def check_direction(d, row, col):
    # 1: 북쪽 방향
    # 2: 왼쪽 방향
    # 3: 오른쪽 방향
    if d == 1:
        # 왼쪽 체크
        dr, dc = -1, 0  # 계속 직진일 때

        if col != 0 and arr[row][col - 1]:  # 좌회전
            d = 2
            dr, dc = 0, -1
        if col != 99 and arr[row][col + 1]:  # 우회전
            d = 3
            dr, dc = 0, 1

    elif d == 2:  # 왼쪽방향
        dr, dc = 0, -1  # 방향 유지 시
        # 오른쪽 체크
        if arr[row - 1][col]:
            d = 1
            dr, dc = -1, 0

    elif d == 3:  # 오른쪽방향
        dr, dc = 0, 1  # 방향 유지 시
        # 왼쪽 체크
        if arr[row - 1][col]:
            d = 1
            dr, dc = -1, 0  # 방향 유지 시

    return d, dr, dc


sys.stdin = open("input.txt")

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    row = 99
    col = 0
    # 1. 2(출발점 찾기)(100번째 행에 있음)
    for j in range(100):
        if arr[99][j] == 2:
            col = j
            break

    # 사다리 로직
    flag = 1
    d = 1  # 처음엔 북진
    while flag:
        # print(d, row, col)
        d, dr, dc = check_direction(d, row, col)
        row = row + dr
        col = col + dc
        if row == 0: # 첫 행 도착
            print(f'#{tc} {col}')
            break
