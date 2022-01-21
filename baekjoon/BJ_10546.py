# 배부른 마라토너
# 한명이 완주 못했음
# 1 <= N <= 10^5
import sys
N = int(sys.stdin.readline())
participants_dict = {}
for _ in range(2*N-1):
    a = sys.stdin.readline().rstrip()
    if a in participants_dict:
        del participants_dict[a]
    else:
        participants_dict[a] = 1

print(*participants_dict)
