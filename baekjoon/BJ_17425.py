import sys
# 약수의 합
input = sys.stdin.readline

tc = int(input())
# 1 ~ 10^6
f = [0 for _ in range(1000001)]
for i in range(1, 10**3 + 1):
    for j in range(i*i, 10**6 + 1, i):  # 약수의 절반 이하를 보장
        # if i = 10 -> 100부터는 100의 약수에서 중간이거나 그 전에 위치 무조건
        # ex) i = 6 이면
        # 36 => 1, 2, 3, 4, #6#, 9, 12, 18, 36 (딱 중간)
        # 36 미만, 30 => 1, 2, 3, 5, #6#, 10, 15, 30 (중간에서 뒤)
        # 36 초과, 48 => 1, 2, 3, 4, #6#, 8, 12, 16, 24, 48 (중간 이전)
        # 약수의 가운데에서 앞부분만 계산하면 뒤는 자동으로 나오니까
        # i * i 부터 끝까지 한다.
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
