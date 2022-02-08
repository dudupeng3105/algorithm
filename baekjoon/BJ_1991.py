import sys

N = int(sys.stdin.readline())
tree= {}

for n in range(N):
    node, left, right = sys.stdin.readline().strip().split()
    tree[node] = [left, right]

def preorder(node):  # 전위순회 ABDCEFG N(node)L(left)R(right)
    if node == '.':
        return
    print(node, end="")
    preorder(tree[node][0])
    preorder(tree[node][1])    

def inorder(node):  # 중위순회 DBAECFG L(left)N(node)R(right)
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end="")
    inorder(tree[node][1])      

def postorder(node):  # 후위순회 DBEGFCA L(left)R(right)N(node)
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1]) 
    print(node, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')