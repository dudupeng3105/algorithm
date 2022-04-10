import sys
import heapq
input = sys.stdin.readline

n = int(input())
lecture_lst = []
for _ in range(n):
    lecture_lst.append(list(map(int, input().split())))

lecture_lst.sort(key=lambda x: -x[1])
if lecture_lst:
    total_day = lecture_lst[0][1]  # 총 날짜
else:
    total_day = 0

lecture_hq = []  # 힙으로 쓰일 리스트
lecture_idx = 0
total_money = 0
for day in range(total_day, 0, -1):
    while lecture_idx < n and lecture_lst[lecture_idx][1] == day:
        heapq.heappush(lecture_hq, -lecture_lst[lecture_idx][0])
        lecture_idx += 1
    # 힙에 넣었으면 하나만 꺼냄
    if lecture_hq:
        total_money += heapq.heappop(lecture_hq)

print(-total_money)
