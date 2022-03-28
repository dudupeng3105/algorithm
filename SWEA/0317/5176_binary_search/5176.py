import sys
sys.stdin = open("test.txt")


def binary_search_tree(node):
    global value
    if node <= n:  # like 중위순회
        binary_search_tree(2*node)
        tree[node] = value
        value += 1
        binary_search_tree(2*node+1)


test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    tree = [0 for _ in range(n+1)]
    value = 1
    binary_search_tree(1)
    print(f'#{tc} {tree[1]} {tree[n//2]}')