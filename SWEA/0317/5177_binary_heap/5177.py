import sys
sys.stdin = open("test.txt")


def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last  # 새로 추가된 정점을 자식으로
    p = c // 2  # 완전이진트리에서의 부모 정점
    while p >= 1 and tree[p] > tree[c]:  # 부모가 있고, 자식의 키 값이 더 크면 교환
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2


test_case = int(input())
for tc in range(1, test_case + 1):
    node_num = int(input())
    tree = [0] * (node_num+1)
    last = 0   # 마지막 정점 번호
    num_lst = list(map(int, input().split()))
    for num in num_lst:
        enq(num)

    # 조상 노드들의 합
    last_node = node_num
    result = 0
    last_node = last_node // 2
    while last_node >= 1:
        result += tree[last_node]
        last_node = last_node // 2
    print(f'#{tc} {result}')
