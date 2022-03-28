import sys

sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    n, m, l = map(int, input().split())

    tree = [0 for _ in range(n + 2)]
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a] = b
        
    # 트리 값 채우기
    for i in range(n, 0, -1):  # n -> 1
        if not tree[i]:  # tree[i] == 0
            tree[i] = tree[2 * i] + tree[2 * i + 1]

    print(f'#{tc} {tree[l]}')
