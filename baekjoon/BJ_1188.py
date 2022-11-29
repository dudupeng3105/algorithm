import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
chunk = m//math.gcd(n, m)

print(m-m//chunk)