import sys
sys.stdin = open("test.txt")


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


for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    row = 99
    col = []
    # 1. 출발점들 찾기(거꾸로 올라가게 했음)
    for j in range(100):
        if arr[99][j] == 1:
            col.append(j)

    result = 10000000
    result_col = 0
    for this_col in col:
        r, c = 99, this_col
        dist = 0
        # 사다리 로직
        flag = 1
        d = 1  # 처음엔 북진
        while flag:
            # print(d, row, col)
            d, dr, dc = check_direction(d, r, c)
            r = r + dr
            c = c + dc
            dist += 1
            if r == 0:  # 첫 행 도착
                break

        if result > dist:
            result = dist
            result_col = c

    print(f'#{tc} {result_col}')
