import sys

N = int(sys.stdin.readline())
arr = [[] for _ in range(N + 1)]
arr[0] = [1]
for _ in range(N-1):
    v1, v2 = map(int, sys.stdin.readline().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

bfs_seq = list(map(int, sys.stdin.readline().split()))


que = [0]
idx = 0
for num in bfs_seq:
    while num not in arr[que[idx]]:
        idx += 1
        if idx > len(que) - 1:
            print(0)
            exit(0)
    
    que.append(num)

print(1)