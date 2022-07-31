import sys

input = sys.stdin.readline
# 볼 모으기
N = int(input())
given_str = input().rstrip()

# 파랑, 빨강, 좌, 우
ans = 10000000
# 파랑 우로
flag = 0
temp = 0
for i in range(len(given_str) - 1, -1, -1):
    if given_str[i] == 'B':
        if flag:
            temp += 1

    else:  # given_str[i] == 'R'
        flag = 1
        continue

ans = min(temp, ans)

# 빨강 우로
flag = 0
temp = 0
for i in range(len(given_str) - 1, -1, -1):
    if given_str[i] == 'R':
        if flag:
            temp += 1

    else:  # given_str[i] == 'R'
        flag = 1
        continue

ans = min(temp, ans)

# 파랑 좌로
flag = 0
temp = 0
for i in range(len(given_str)):
    if given_str[i] == 'B':
        if flag:
            temp += 1

    else:  # given_str[i] == 'R'
        flag = 1
        continue

ans = min(temp, ans)

# 빨강 좌로
flag = 0
temp = 0
for i in range(len(given_str)):
    if given_str[i] == 'R':
        if flag:
            temp += 1

    else:  # given_str[i] == 'B'
        flag = 1
        continue

ans = min(temp, ans)

print(ans)
