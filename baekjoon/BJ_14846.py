import sys

input = sys.stdin.readline
'''
3
1 2 3
3 2 1
5 6 3
3
1 1 2 3
2 2 2 2
1 1 3 3
'''
n = int(input())
arr = [[0 for _ in range(n+1)]] + [[0] + list(map(int, input().split())) for _ in range(n)]
set_map = [[set() for _ in range(n+1)] for __ in range(n+1)]
#dp = [[0 for _ in range(n+1)] for __ in range(n+1)]
# print(arr)

# print(dp)

# dp 계산
for r in range(1, n+1):
    for c in range(1, n+1):
        set_map[r][c] = (set_map[r-1][c] | set_map[r][c-1])
        set_map[r][c].add(arr[r][c])
        #print(set_map[r][c])
        #dp[r][c] = len(set_map[r][c])


# 쿼리 받기
k = int(input())
for _ in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    temp = set_map[r2][c2] - set_map[r2][c1-1] - set_map[r1-1][c2]
    ans = len(temp)
    if ans:
        print(ans)
    else:
        print(1)