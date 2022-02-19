import sys
sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    n, q = map(int, input().split())
    arr = [0 for x in range(n+1)]

    for num in range(1, q+1):
        left, right = map(int, input().split())
        for i in range(left, right+1):
            arr[i] = num

    print(f'#{tc}', end=' ')
    print(*arr[1:])