import sys

input = sys.stdin.readline


def rotate_45(lst, half_n):
    rotated_lst = [lst[i][::] for i in range(n)]
    # half_n = n//2
    for i in range(n):
        # (0,0) -> (n-1,n-1) 대각
        rotated_lst[i][half_n] = lst[i][i]
        # (0, n//2) -> (n-1, n//2)
        rotated_lst[i][n - i - 1] = lst[i][half_n]
        # (n//2, 0) -> (n//2, n-1)
        rotated_lst[i][i] = lst[half_n][i]
        # (i, n-i-1) 대각선
        rotated_lst[half_n][n - i - 1] = lst[i][n - i - 1]

    return rotated_lst


tc = int(input())
for _ in range(tc):
    n, deg = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    rotate_num = (deg // 45) % 8
    for i in range(rotate_num):
        arr = rotate_45(arr, n // 2)

    for i in range(n):
        print(*arr[i])
