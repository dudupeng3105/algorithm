import sys

sys.stdin = open("input.txt")

testcase = int(input())
for tc in range(1, testcase + 1):
    arr = [[0 for _ in range(10)] for __ in range(10)]
    n = int(input())
    violet_cnt = 0
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        if color == 1:  # 칠할 색깔 빨강
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if arr[r][c] == 3:
                        continue

                    if arr[r][c] == 1:
                        continue

                    else:  # 칠해져있는 색이 파랑이거나 0
                        arr[r][c] += 1
                        if arr[r][c] == 3:
                            violet_cnt += 1

        else:  # if color == 2 # 칠할 색깔 파랑
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if arr[r][c] == 3:
                        continue

                    if arr[r][c] == 2:
                        continue

                    else:  # 칠해져있는 색이 빨강임
                        arr[r][c] += 2
                        if arr[r][c] == 3:
                            violet_cnt += 1

    print(f'#{tc} {violet_cnt}')