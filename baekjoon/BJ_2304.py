building_map = [0 for _ in range(1001)]
roof_map = [0 for _ in range(1001)]

building_num = int(input())
# 입력받기
for _ in range(building_num):
    number, height = map(int, input().split())
    building_map[number] = height

# 왼쪽에서 끝까지, max_height 찾기
max_height = 0
max_index = 0

for i in range(1001):
    if building_map[i] > max_height:
        max_height = building_map[i]
        max_index = i

    roof_map[i] = max_height

peak_num = max_index
# 오른쪽에서 peak_num 전까지
max_height = 0
max_index = 0
for j in range(1000, peak_num, -1):
    if building_map[j] > max_height:
        max_height = building_map[j]
        max_index = j

    roof_map[j] = max_height


print(sum(roof_map))
