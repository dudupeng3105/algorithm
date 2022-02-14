import sys

sys.stdin = open("input.txt")

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(5)]
    result = 0
    for row in range(n):
        for col in range(n):
            temp = 0
            center_num = arr[row][col]
            for i in range(4):
                n_row = row + dx[i]
                n_col = col + dy[i]
                if n_row < 0 or n_row > n - 1 or \
                        n_col < 0 or n_col > n - 1:
                    continue
                temp += abs(arr[n_row][n_col] - center_num)
            result += temp

    print(f'#{tc} {result}')