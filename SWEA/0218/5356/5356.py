import sys
sys.stdin = open('test.txt')

test_case = int(input())

for tc in range(1, test_case + 1):
    arr = [[-1 for _ in range(15)] for __ in range(5)]

    for i in range(5):
        given_str = input()
        arr[i][:len(given_str)] = list(given_str)

    col = 0
    cnt = 0
    temp = ''
    while cnt < 5 and col < 15:  # -1 연속 5개 나오면 중지함(글자가 없음)
        cnt = 0
        for row in range(5):
            if arr[row][col] == -1:
                cnt += 1
                continue
            else:
                temp += arr[row][col]

        col += 1

    print(f'#{tc} {temp}')

