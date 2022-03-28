def dfs(total, start, depth):
    global result

    if depth > n:
        return

    if total > result:
        return

    if total >= h:
        if total < result:
            result = total
        return

    for i in range(start, n):
        plus_num = arr[i]
        dfs(total + plus_num, i + 1, depth + 1)


test_case = int(input())
for tc in range(1, test_case + 1):
    n, h = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 99999999
    dfs(0, 0, 0)
    print(f'#{tc} {result - h}')