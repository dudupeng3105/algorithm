import sys
input = sys.stdin.readline

R, C, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
ans = sys.maxsize
ans_h = -1
for h in range(257): # h 최종 높이
    added_block = 0
    removed_block = 0
    for r in range(R):
        for c in range(C):
            this_height = arr[r][c]
            if this_height > h:
                removed_block += (this_height - h)
            else:
                added_block += (h - this_height)
    # print(h, removed_block, added_block, ans)
    if removed_block + B >= added_block:  # 제거한 블록 + 원래 갖고 있던거가 -> 쌓을 수 있는 블록 >= 쌓았던 블록
        if removed_block * 2 + added_block <= ans:
            ans = removed_block * 2 + added_block
            ans_h = h

print(ans, ans_h)
