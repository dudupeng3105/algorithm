# 1010 번 다리놓기
# 강 서쪽 N 포인트 <= 강 동쪽 M 포인트
# nCr = n! / r!(n-r)!
from math import comb

N = int(input())
for _ in range(N):
    N, M = map(int, input().split(' '))
    print(comb(M, N))


