test_case = int(input())

for tc in range(1, test_case + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append([a, b])

    arr.sort(key=lambda x: (x[1], x[0]))
    print(arr)
    i = 1
    cnt = 1
    end_time = arr[0][1]
    while i < n:
        if arr[i][0] < end_time:
            i += 1
        else:
            cnt += 1
            end_time = arr[i][1]
            i += 1

    print(f'#{tc} {cnt}')
