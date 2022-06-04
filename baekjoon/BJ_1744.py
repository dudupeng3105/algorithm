import sys

input = sys.stdin.readline

n = int(input())
minus = []
plus = []
one = []
for _ in range(n):
    a = int(input())
    if a == 1:
        one.append(a)
    elif a > 0:
        plus.append(a)
    else:
        minus.append(a)

# 연산
plus.sort()
minus.sort(reverse=True)
ans = 0
idx = len(plus)//2
while idx > 0:
    a = plus.pop()
    b = plus.pop()
    ans += (a*b)
    idx -= 1

if plus:
    ans += plus.pop()

if one:
    ans += len(one)

len_minus = len(minus)//2
idx = 0
while idx < len_minus:
    a = minus.pop()
    b = minus.pop()
    ans += (a*b)
    idx += 1

if minus:
    ans += minus.pop()

print(ans)