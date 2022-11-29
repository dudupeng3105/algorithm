# 23022 숙제
import sys
import heapq

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n, s = map(int, input().split())
    t = list(map(int, input().split()))
    v = list(map(int, input().split()))
    tv = []
    for i in range(n):
        tv.append([t[i], v[i]])
    tv.sort()  # 시간에 대해 정렬
    # 현재 가능한 숙제를 힙큐에 넣고
    # v(기울기)가 큰 거부터 꺼냄(기울기 큰 애를 나두면
    # 다음 시간(t+1)에 손해가 커짐)
    heap = []
    idx = 0
    score = 0
    time = s

    while idx < n:

        # 현재 가능한 숙제를 힙큐에 넣기
        while idx < n and tv[idx][0] <= time:
            heapq.heappush(heap, [-tv[idx][1], idx])
            idx += 1

        #print("시간", time, heap)

        if heap:  # 힙 내용물있으면
            # v(기울기 큰 것)을 먼저 함
            temp_v, temp_idx = heapq.heappop(heap)
            score = score + (time - tv[temp_idx][0]) * (-temp_v)
            time += 1

        else:
            time = tv[idx][0]  # 시간을 다음숙제까지 점프

    #print(time, heap)
    while heap:
        # v(기울기 큰 것)을 먼저 함
        temp_v, temp_idx = heapq.heappop(heap)
        score = score + (time - tv[temp_idx][0]) * (-temp_v)
        time += 1
    print(score)
