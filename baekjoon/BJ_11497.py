import sys

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    left = []
    right = []
    for i in range(len(arr) // 2):
        left.append(arr[2 * i])
        right.append(arr[2 * i + 1])

    if len(arr) % 2: # n이 홀수
        ans = left + [arr[-1]] + right[::-1]
    else:
        ans = left + right[::-1]

    # 최대 차이 찾기
    diff = 0
    for i in range(1, n):
        temp = abs(ans[i] - ans[i-1])
        if temp > diff:
            diff = temp

    print(diff)


