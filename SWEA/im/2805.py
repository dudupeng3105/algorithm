import sys
sys.stdin = open("test.txt")

test_case = int(input())

for tc in range(1, test_case + 1):
    n = int(input())
    arr = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input()))

    mid = n // 2
    result = 0
    # 위 아래 두 줄씩 계산
    for i in range(mid):
        result += sum(arr[i][mid-i: mid+i+1])
        result += sum(arr[n-1-i][mid - i: mid + i + 1])
    # 중간줄
    result += sum(arr[mid][:])

    print(f'#{tc} {result}')