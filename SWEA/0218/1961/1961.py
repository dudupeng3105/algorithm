import sys
sys.stdin = open("test.txt")

def rotate_90(arr):
    arr_2 = [[0 for _ in range(N)] for __ in range(N)]
    for row in range(N):
        for col in range(N):
            arr_2[col][N - 1 - row] = arr[row][col]

    return arr_2


test_case = int(input())
for tc in range(test_case):
    N = int(input())
    arr = [[0 for _ in range(N)] for __ in range(N)]
    result_list = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    for r in range(3): # 90, 180, 270
        arr = rotate_90(arr)
        for i in range(N):
            if r == 0:
                result_list[i] = arr[i]
                print(result_list)
            else:
                result_list[i] += arr[i]
                print(result_list)

    print(f'#{tc+1}')
    for i in range(N):
        for j in range(len(result_list[i])-1):
            if (j+1) % N == 0:
                print(result_list[i][j], end='')
                print(' ',end='')
            else:
                print(result_list[i][j], end='')
        print(result_list[i][len(result_list[i])-1]) # 마지막 요소