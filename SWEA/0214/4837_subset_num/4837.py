import sys

# dfs 풀이
def dfs(element, start, depth):
    global cnt
    
    if sum(element) > k:
        return

    if depth == n:
        if sum(element) == k:
            cnt += 1
            return
        else:
            return

    for i in range(start, 13):
        element.append(i)
        dfs(element, i+1, depth + 1)
        element.pop()


sys.stdin = open("input.txt")

testcase = int(input())
for tc in range(1, testcase + 1):
    n, k = map(int, input().split())
    cnt = 0
    dfs([], 1, 0)
    print(f'#{tc} {cnt}')


