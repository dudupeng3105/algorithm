import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# % 7 처리 미리 한 번 하기
# for i in range(n):
#     a[i] = a[i] % 7
# for i in range(m):
#     b[i] = b[i] % 7

# m 번의 연산
for i in range(m):
    for j in range(n):
        if a[j] == 0:
            continue
        else:
            a[j] = (a[j] + b[i]) % 7

print(a)