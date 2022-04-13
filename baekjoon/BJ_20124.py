n = int(input())
a = []
for _ in range(n):
    name, num = map(str, input().split(' '))
    a.append([name, int(num)])

a.sort(key=lambda x: (-x[1], x[0]))
print(a[0][0])
