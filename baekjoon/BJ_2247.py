import sys
input = sys.stdin.readline

n = int(input())
result = 0
for num in range(2, n//2+1):
    result = (result + num*(n//num-1) % 1000000) % 1000000

print(result)


