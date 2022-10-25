import sys
input = sys.stdin.readline

H, W = map(int, input().split())
heights = list(map(int, input().split()))

ans = 0
total = 0
for h in range(1, H + 1):
    flag = 0
    temp_cnt = 0
    for i in range(W):
        # 처음 벽 만남(flag = 0 => 1)
        if not flag:
            if heights[i] >= h:
                flag = 1
        else:
            if heights[i] >= h:
                total += temp_cnt
                temp_cnt = 0
            else:
                temp_cnt += 1
    # print(i, total)

print(total)


