import sys

input = sys.stdin.readline

n, q = map(int, input().split())
arr = [False for _ in range(n + 1)]
for _ in range(q):
    hope_num = int(input())
    now_num = hope_num
    flag = 1
    occupied_land_num = -1
    while now_num > 1:
        if arr[now_num]:  # true 이미 점유
            occupied_land_num = now_num
            flag = 0
        now_num = now_num // 2

    if flag:  # 점유가능
        arr[hope_num] = True
        print(0)
    else:  # 점유 불가능
        print(occupied_land_num)
