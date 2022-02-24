c, r = map(int, input().split())
row = [x for x in range(r + 1)]
col = [x for x in range(c + 1)]

cut_num = int(input())
for _ in range(cut_num):
    direction, num = map(int, input().split())
    if direction:  # 세로
        col[num] = -1  # -1로 바꿈, 구분 위해
    else:  # 가로
        row[num] = -1

# 가로 최대길이
max_horizontal = 0
temp = 0
for i in range(1, c + 1):
    if col[i] != -1:
        temp += 1
    else:  # col[i] == -1
        temp += 1
        if temp > max_horizontal:
            max_horizontal = temp
        temp = 0  # 초기화

# 마지막 조각 체크
if temp > max_horizontal:
    max_horizontal = temp

# 세로 최대길이
max_vertical = 0
temp = 0
for i in range(1, r + 1):
    if row[i] != -1:
        temp += 1
    else:  # row[i] == -1
        temp += 1
        if temp > max_vertical:
            max_vertical = temp
        temp = 0  # 초기화

if temp > max_vertical:
    max_vertical = temp

print(max_vertical * max_horizontal)
