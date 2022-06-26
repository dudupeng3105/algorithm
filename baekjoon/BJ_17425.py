import sys

input = sys.stdin.readline

tc = int(input())
# 1 ~ 10^6
f = [0 for _ in range(1000001)]
for i in range(1, 10**3 + 1):
    for j in range(i*i, 10**6 + 1, i):  # 약수의 절반 이하를 보장
        # if i = 10 -> 100부터는 100의 약수에서 중간이거나 그 전에 위치 무조건
        # 나머지 부분은 b를 통해서 계산됨 굿
        b = j//i
        if i == b:  # 4 => 2 * 2 같은 경우
            f[j] += i
        else:
            f[j] = f[j] + i + b

# g 계산
g = [0 for _ in range(1000001)]
for i in range(1, 10**6 + 1):
    g[i] = g[i-1] + f[i]

for _ in range(tc):
    n = int(input())
    print(g[n])
