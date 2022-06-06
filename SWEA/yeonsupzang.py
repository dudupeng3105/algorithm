people_lst = [0 for _ in range(N)]

for a, b in trust:
    people_lst[b] += 1

for i in range(N):
    if people_lst[i] == N-1:
        print(i+1)
        break
