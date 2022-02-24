arr = [[0 for _ in range(101)] for __ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

# 영역 넓이 구하기
result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            result += 1

print(result)