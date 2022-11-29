import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
cumulative_arr = [0]

for i in range(1, N+1):
    cumulative_arr.append(cumulative_arr[i-1] + arr[i-1])

cnt = 0
for i in range(1, N+1):
    for j in range(i, N+1):
        temp = cumulative_arr[j] - cumulative_arr[i-1]
        if temp == M:
            cnt += 1

print(cnt)