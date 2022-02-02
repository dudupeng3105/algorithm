from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)


def dfs(start, depth):
    global yes_or_no
    visited[start] = True 
    if depth % 2: # 홀수 depth(1,3,5...)
        color_check[start] = 1 # black
    else: # 짝수 depth(2,4,6...)
        color_check[start] = 0 # white
    
    for i in connected_dict[start]:
        
        if visited[i] == False:
            dfs(i, depth + 1)
        else:
            if color_check[start] == color_check[i]:                
                yes_or_no = 1


    
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    N, M = map(int, sys.stdin.readline().split())  # vertax, edge
    connected_dict = defaultdict(list)
    for __ in range(M):
        a, b = map(int, sys.stdin.readline().split())    
        connected_dict[a].append(b)
        connected_dict[b].append(a)    

    visited = [False for x in range(N + 1)]
    color_check = [-1 for x in range(N + 1)] # 초기화는 -1로
    color_check[0] = 0 # white
    yes_or_no = 0    
    # 연결요소가 1이상인 경우도 생각해서 출발 다해봄
    for i in range(1, N + 1):
        if visited[i] == False:
            dfs(i, 0)            
        else:
            continue

    if yes_or_no:
        print('NO')
    else:
        print('YES')