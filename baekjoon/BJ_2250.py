# 2250, 트리의 높이와 너비
# 격자에 그림
# 같은 레벨에 있는 노드는 같은 행에 위치
# 가장 왼쪽, 오른쪽격자열은 비지 않았다.
# 중위순회와 뎁스 사용했음
# LNR
# 루트노드는 depth 1
import sys

def inorder(node, depth):  # 중위순회 L(left)N(node)R(right)
    # 여기에 depth만 버무리면 됨
    if node == -1:
        return
    inorder(tree[node][0], depth + 1)    
    depth_num.append(depth)    
    inorder(tree[node][1], depth + 1) 


N = int(sys.stdin.readline())
tree = [[] for i in range(N + 1)] #
rootcheck=[0] * (N+2) # n+1 인덱스에는 '-1'이 들어가서 방해못하게
for n in range(N):    
    node, left, right = map(int, sys.stdin.readline().strip().split())
    rootcheck[int(node)] += 1
    rootcheck[int(left)] += 1
    rootcheck[int(right)] += 1    
    tree[node] = [left, right]

root_node = rootcheck.index(1)

depth_num = []
inorder(root_node, 1) # 중위 순회 돌려서 위치(index)랑 뎁스 찾음
tree_map = [[0,0] for _ in range(max(depth_num) + 1)]
for i, depth in enumerate(depth_num):
    if tree_map[depth][0] == 0: # 아직 왼쪽 지점 안들어 왔으면
        tree_map[depth][0] = i + 1 # 몇 번째 칼럼인지 넣음
    else:
        tree_map[depth][1] = i + 1 # 들어올때마다 오른쪽 끝점 바꾸면 됨   


max_width = 0
result_depth = 0

for depth in range(len(tree_map)-1, 0, -1): # 가장 넓은 최소레벨이므로 거꾸로 감
    if 0 in tree_map[depth]:
        this_width = 1
    else:
        this_width = tree_map[depth][1] - tree_map[depth][0] + 1
    if this_width >= max_width:
        max_width = this_width
        result_depth = depth

print(result_depth, max_width)