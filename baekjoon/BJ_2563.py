arr = [[0 for _ in range(100)] for __ in range(100)]

paper_num = int(input())
for _ in range(paper_num):
    c, r = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            arr[i][j] = 1

# 영역 넓이 구하기
result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            result += 1

print(result)
