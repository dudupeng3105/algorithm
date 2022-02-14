import sys

sys.stdin = open("input.txt")

test_case = int(input())

for tc in range(1, test_case + 1):
    arr = list(map(int, input().split()))
    flag = 0
    for i in range(1, 1 << 10):
        if flag:
            break
        temp = 0

        for j in range(10):
            if i & (1 << j):
                temp += arr[j]
        if temp == 0:
            flag = 1

    print(f'#{tc} {flag}')
