density = int(input())
seq = []
direction_cnt = [0, 0, 0, 0, 0]
for _ in range(6):
    direction, length = map(int, input().split())
    direction_cnt[direction] += 1
    seq.append((direction, length))

# w, h 찾기
w_h_list = []
for i in range(1, 5):
    if direction_cnt[i] == 1:
        w_h_list.append(i)

# 파인 곳 찾기 w,h 다음에 cnt 2인거 나오면 그 다음 2개가 파인 곳
for i in range(6):
    if seq[i][0] in w_h_list:
        if seq[(i + 1) % 6][0] not in w_h_list:
            w, h = seq[i][1], seq[i - 1][1]
            edge_w, edge_h = seq[(i + 2) % 6][1], seq[(i + 3) % 6][1]

# 참외 수 계산
area = w * h - edge_w * edge_h
print(area * density)
