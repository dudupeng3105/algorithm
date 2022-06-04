import sys
input = sys.stdin.readline


n = int(input())
arr = [input() for _ in range(n)]
coin_map = [[0 for _ in range(n)] for __ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            coin_map[i][j] = 1


ans = n*n
# 행에 대한 모든 경우의 2^20 = 10^6 정도
for bit_seq in range(1 << n):
    # 맵 복사
    temp_map = [coin_map[x][:] for x in range(n)]
    for i in range(n):
        if bit_seq & (1 << i):
            for j in range(n):
                temp_map[i][j] = 1 - temp_map[i][j]

    # 행 경우의 수에 대한 열 경우의 수(h,t 개수 중 작은 거 고르면됨
    # 열끼리 서로 독립적임)
    cnt = 0
    for j in range(n):
        col_cnt = 0
        for i in range(n):
            if temp_map[i][j]:
                col_cnt += 1

        cnt += min(col_cnt, n-col_cnt)

    if cnt < ans:
        ans = cnt

print(ans)