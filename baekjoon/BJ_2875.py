from itertools import permutations

permutations()

n, m, k = map(int, input().split())

while k > 0:
    if n <= 2*(m-1):
        m -= 1
    else:
        n -= 1

    k -= 1

print(min(n//2, m))