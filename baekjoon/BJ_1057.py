import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

cnt = 0
while a != b:
    a = a - a//2
    b = b - b//2
    #print(a, b)
    cnt += 1

print(cnt)
