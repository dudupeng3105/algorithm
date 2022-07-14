import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
initial_len = 0
for i in range(n):
    temp = input().rstrip()
    initial_len += len(temp)
    arr.append(temp)

needed = m - initial_len
essential = needed // (n - 1)
lack = needed - essential * (n - 1)

rank = [0 for _ in range(n)]

order = 1
# 우선순위 1 소문자 중에 앞에 있는거에..
for i in range(1, n):
    if arr[i][0].islower():  # 소문자이면..
        rank[i] = order
        order += 1

# 우선순위 2 대문자 중에 뒤에 있는거에..
for i in range(n - 1, 0, -1):
    if not arr[i][0].islower():  # 대문자이면..
        rank[i] = order
        order += 1
#
# print(lack)
# print(rank)
result = arr[0]
for i in range(1, n):
    temp = essential
    if rank[i] <= lack:
        temp += 1

    result += ('_' * temp + arr[i])

print(result)
