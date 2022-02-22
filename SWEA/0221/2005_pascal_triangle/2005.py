test_case = int(input())

for tc in range(test_case):
    N = int(input())
    arr = [[0 for _ in range(N)] for __ in range(N)]
    arr[0][0] = 1
    i = 1

    while i != N:
        arr[i][0] = 1
        for k in range(1, i + 1):
            arr[i][k] = arr[i-1][k-1] + arr[i-1][k]
        i += 1

    print(f'#{tc + 1}')
    for j in range(len(arr)):
        print(" ".join(map(str, arr[j][:j+1])))