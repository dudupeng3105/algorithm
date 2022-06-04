#https://jason9319.tistory.com/113

import bisect
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = []
dp.append(arr[0])

for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
        print(dp)
    else:
        dp[bisect.bisect_left(dp, arr[i])] = arr[i]
        print(dp)

print(len(dp))