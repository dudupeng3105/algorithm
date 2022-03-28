from collections import deque
test_case = int(input())

def direction(a):
    if a == 1:  # 1, 1
        return [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    elif a == 2:  # 1, 1
        return [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    elif a == 3:  # 1, 1
        return [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    elif a == 4:  # 1, 1
        return [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    else:
        return [(1, 1), (-1, -1), (1, -1), (-1, 1)]



def bfs(s_r, s_c):
    result = -1
    q = deque()
    q.append((s_r, s_c, [arr[s_r][s_c]]))
    while q:
        r, c, path = q.popleft()
        #print("pop", r,c ,path)
        for dr, dc in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            #print(dr, dc)
            n_r, n_c = r + dr, c + dc
            #print(r,c, path, n_r, n_c)
            # 시작점 돌아왔을때
            if n_r == s_r and n_c == s_c:
                #print("걸림", path)
                if len(path) < 4:
                    continue
                else:
                    if len(path) > result:
                        print(path)
                        result = len(path)
                        continue

            if 0 <= n_r < n and 0 <= n_c < n:
                next_dessert = arr[n_r][n_c]
                if next_dessert not in path:
                    #print(n_r, n_c, path)
                    q.append((n_r, n_c, path + [next_dessert]))
                else:
                    continue

    return result


for tc in range(1, test_case + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_result = 0
    for i in range(n):
        for j in range(n):
            temp = bfs(i, j)
            if temp > max_result:
                max_result = temp

    #bfs(2, 0)
    print(f'#{tc} {max_result}')