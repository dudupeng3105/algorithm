import sys

sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case+1):
    arr = [0 for _ in range(5001)]
    n = int(input())
    for _ in range(n):
        start, end = map(int, input().split())
        for i in range(start, end + 1):
            arr[i] += 1

    p = int(input())
    temp = []
    for _ in range(p):
        c = int(input())
        temp.append(arr[c])

    print(f'#{tc}', end=' ')
    print(*temp)



