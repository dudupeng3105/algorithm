# 1954 달팽이 숫자
import sys

sys.stdin = open("input.txt")

test_case = int(input())
for tc in range(test_case):
    N = int(input())
    arr = [[0 for _ in range(N)] for __ in range(N)]
    num = 1  # 1~n*n 채워넣기
    i = 0
    j = 0
    path_checker = 1  # x 축 양의 방향 전진
    while num < N ** 2 + 1:
        arr[i][j] = num
        if path_checker == 1:  # x 축 양의 방향 전진
            if j == N - 1 or arr[i][j + 1]:
                path_checker = 4  # y 축 음의 방향으로 전환
                i += 1
            else:
                j += 1

        elif path_checker == 4:  # y 축 음의 방향으로 전환
            if i == N - 1 or arr[i + 1][j]:
                path_checker = 3  # x 축 음의 방향 전진
                j -= 1
            else:
                i += 1

        elif path_checker == 3:  # x 축 음의 방향 전진
            if j == 0 or arr[i][j - 1]:
                path_checker = 2  # y 축 양의 방향 전진
                i -= 1
            else:
                j -= 1

        elif path_checker == 2:  # y 축 양의 방향 전진
            if i == 0 or arr[i - 1][j]:
                path_checker = 1  # x 축 양의 방향 전진
                j += 1
            else:
                i -= 1

        num += 1

    print(f'#{tc + 1}')
    for row in arr:
        print(*row)