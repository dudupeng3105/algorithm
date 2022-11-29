import sys
# 기차가..
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0 for _ in range(N)]
for _ in range(M):
    op = list(map(int, input().split()))
    if op[0] == 1:  # 1 i x : 1번 기차에 x 번째 좌석에 사람을 태운다 (or연산)
        # 1 << 2 = 0b100
        i, x = op[1] - 1, op[2] - 1
        # 101000 | 000100 = 101100 (비트 켜기)
        arr[i] = arr[i] | (1 << x)
    elif op[0] == 2:  # 2 i x : 1번 기차에 x 번째 좌석에 사람을 내린다 (& ~)
        i, x = op[1] - 1, op[2] - 1
        arr[i] = arr[i] & ~(1 << x)

    elif op[0] == 3:  # 3 i : SHL
        i = op[1] - 1
        # ~(1 << 20) = 0(21번째 자리) 11111111111111(20~1자리)
        arr[i] = (arr[i] << 1) & ~(1 << 20)

    else:  # op[0] ==4  # 4 i : SHR
        i = op[1] - 1
        arr[i] = (arr[i] >> 1)

    # print(arr)

# print(arr)
print(len(set(arr)))
