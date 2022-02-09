import sys

# 233677
sys.stdin = open('input.txt')
test_case = int(input())

for tc in range(test_case):
    cnt_arr = [0 for _ in range(10)]
    arr = [int(x) for x in input()]
    for num in arr:
        cnt_arr[num] += 1

    cnt = 0
    i = 0
    while i < 10:
        if cnt_arr[i] >= 3:
            cnt_arr[i] -= 3
            cnt += 1
            continue
        if cnt_arr[i] and cnt_arr[i + 1] and cnt_arr[i + 2]:
            cnt_arr[i] -= 1
            cnt_arr[i + 1] -= 1
            cnt_arr[i + 2] -= 1
            cnt += 1
            continue
        i += 1
    if cnt == 2:
        print(f'#{tc + 1} {1}')
    else:
        print(f'#{tc + 1} {0}')
