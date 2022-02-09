import sys

sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    building_lst = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):  # 양옆에 00 ~~~ 00 임
        left_max = max(building_lst[i-2], building_lst[i-1])
        right_max = max(building_lst[i+2], building_lst[i+1])
        max_height = max(left_max, right_max)

        if building_lst[i] > max_height:
            cnt += building_lst[i] - max_height

    print(f'#{tc+1} {cnt}')