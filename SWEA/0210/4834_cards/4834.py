import sys
# 카드
sys.stdin = open('input.txt')

testcase = int(input())
for tc in range(testcase):
    length = int(input())
    arr = [int(x) for x in input()]
    # arr = list(input())
    print(arr)
    count_lst = [0 for x in range(10)]
    for i in arr:
        count_lst[int(i)] += 1

    cnt = 0
    num = 0
    for j in range(10):
        if count_lst[j] >= cnt:
            cnt = count_lst[j]
            num = j
    print(f'#{tc + 1} {num} {cnt}')
