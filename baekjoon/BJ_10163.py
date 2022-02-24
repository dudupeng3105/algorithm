import sys
arr = [[0 for _ in range(1001)] for __ in range(1001)]

paper_num = int(sys.stdin.readline())
cnt = [0 for _ in range(paper_num+1)]
for num in range(1, paper_num + 1):
    x1, y1, w, h = map(int, sys.stdin.readline().split())
    for i in range(y1, y1+h):
        for j in range(x1, x1+w):
            if arr[i][j]:  # 이미 숫자가 있으면
                cnt[arr[i][j]] -= 1
                arr[i][j] = num
                cnt[num] += 1
            else:
                arr[i][j] = num
                cnt[num] += 1

# 영역 넓이 출력
for num in range(1, paper_num + 1):
    print(cnt[num])

