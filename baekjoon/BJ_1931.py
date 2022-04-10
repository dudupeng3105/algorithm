n = int(input())
time_lst = []
for _ in range(n):
    s, e = map(int, input().split())
    time_lst.append([s,e])

time_lst.sort(key=lambda x: (x[1], x[0]))
cnt = 1
now_end_time = time_lst[0][1]
for i in range(1, n):
    if time_lst[i][0] >= now_end_time:
        now_end_time = time_lst[i][1]
        cnt += 1

print(cnt)