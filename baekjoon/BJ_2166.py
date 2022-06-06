import sys
input = sys.stdin.readline

n = int(input())
coordinates = [[0,0] for _ in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    coordinates[i] = [x, y]

x0, y0 = coordinates[0]
ans = 0
for i in range(1, n-1):
    x1, y1 = coordinates[i]
    x2, y2 = coordinates[i+1]
    triangle_area = (x1*y0 + x2*y1 + x0*y2) - (x0*y1 + x1*y2 + x2*y0)

    ans += triangle_area

print(round(abs(ans)/2, 2))