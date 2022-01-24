#42 이진 트리의 최대 깊이
#반복 구조로 BFS 풀이
#BFS 반복구조, BFS는 큐로 구현
import collections
class treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_depth(root : treenode):
    if root is None:
        return 0
    queue = collections.deque([root])    
    depth = 0

    while queue:
        depth += 1
        # 큐 연산 추출 노드의 자식 노드 삽입
        for _ in range(len(queue)):
            cur_root = queue.popleft()           
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
            
    # BFS 반복 횟수 == 깊이
    return depth

n1 = treenode(3)
n2 = treenode(9)
n3 = treenode(20)
n4 = treenode(15)
n5 = treenode(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

print(max_depth(n1))

# 43 이진 트리의 직경
# 두 노드 간 가장 긴 경로의 길이를 출력하라
#
class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: treenode) -> int:
        def dfs(node: treenode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽 각각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest

n1 = treenode(1)
n2 = treenode(2)
n3 = treenode(3)
n4 = treenode(4)
n5 = treenode(5)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
sol = Solution()

print(sol.diameterOfBinaryTree(n1))

class Solution_2:
    result = 0

    def longest_univalue_path(self, root):
        def dfs(node: treenode):
            if node is None:
                return 0
            
            # dfs, 존재하지 않는 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽, 오른쪽 자식 노드간 거리의 합 최대값이 결과
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)
        
        dfs(root)
        return self.result

n1 = treenode(5)
n2 = treenode(4)
n3 = treenode(5)
n4 = treenode(1)
n5 = treenode(1)
n6 = treenode(5)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
sol = Solution_2()
print(sol.longest_univalue_path(n1))


# 45 이진 트리 반전
# 좌우반전
# 45-1 파이썬 다운 방식
class Solution_45_1:
    def invert_tree(self, root : treenode):
        if root:
            root.left, root.right = \
                self.invert_tree(root.right), self.invert_tree(root.left)
            return root
        else: # 끝까지 왔을 때
            return None

n1 = treenode(4)
n2 = treenode(2)
n3 = treenode(7)
n4 = treenode(1)
n5 = treenode(3)
n6 = treenode(6)
n7 = treenode(9)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
sol = Solution_45_1()
print(sol.invert_tree(n1))

# 좌우반전
# 45-2 반복 구조로 BFS
class Solution_45_2:
    def invert_tree(self, root : treenode):
        queue = collections.deque([root])

        while queue:
            node = queue.popleft() # 루트 꺼냄(첫 번쨰 반복에서)
            # 부모 노드 부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

# 좌우반전
# 45-3 반복 구조로 DFS
class Solution_45_3:
    def invert_tree(self, root : treenode):
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            # 부모 노드 부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)
        
        return root

# 45-4 반복 구조로 DFS 후위 순회
class Solution_45_4:
    def invert_tree(self, root : treenode):
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            # 부모 노드 부터 하향식 스왑
            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left           
    
        return root