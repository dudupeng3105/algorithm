import sys

sys.stdin = open("input.txt")

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for __ in range(100)]
    max_num = 0
    # 행
    for i in range(100):
        temp = sum(arr[i])
        if temp > max_num:
            max_num = temp

        #열
        temp = 0
        for j in range(100):
            temp += arr[j][i]
        if temp > max_num:
            max_num = temp

    # 대각
    temp = 0
    temp_2 = 0
    for i in range(100):
        temp += arr[i][i]
        temp_2 += arr[99-i][i]

    if temp > max_num:
        max_num = temp

    if temp_2 > max_num:
        max_num = temp_2

    print(f'#{tc} {max_num}')