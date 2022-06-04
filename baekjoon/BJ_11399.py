import sys
input = sys.stdin.readline

n = int(input())

minute_lst = list(map(int, input().split()))

minute_lst.sort()

acc = 0  # accumulate
ans = 0
for minute in minute_lst:
    ans += (acc + minute)
    acc += minute

print(ans)