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

# 46 두 이진 트리 병합
class Solution_46:
    def merge_trees(self, t1: treenode, t2: treenode):
        if t1 and t2:
            node = treenode(t1.val + t2.val)
            node.left = self.merge_trees(t1.left, t2.left)
            node.right = self.merge_trees(t1.right, t2.right)

            return node
        else:
            return t1 or t2

n1 = treenode(1)
n2 = treenode(3)
n3 = treenode(2)
n4 = treenode(5)
n1.left = n2
n1.right = n3
n2.left = n4
r1 = treenode(2)
r2 = treenode(1)
r3 = treenode(3)
r4 = treenode(4)
r5 = treenode(7)
r1.left = r2
r1.right = r3
r2.right = r4
r3.right = r5
sol = Solution_46()
print(sol.merge_trees(n1,r1))

# 47. 이진 트리 직렬화 & 역직렬화
# 완전이진트리는 배열에 낭비없이 배치 가능
# 깊이는 1, 2, 4 ,8 
# 부모/자식 노드의 위치는 부모 i/2,. 왼쪽 자식 2*i,
# 오른쪽 자식 2*i + 1
class codec:
    # 직렬화 계층구조 --> byte stream
    def serialize(self, root):
        queue = collections.deque([root]) # root 노드 들어감
        result = ['#'] # 1번 노드부터이므로 처음은 None(#)
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else: # 자식 없을 때
                result.append(str(node.val))
        return ' '.join(result)

    # 역직렬화  byte stream --> 계층구조
    def deserialize(self, data):
        # 예외처리
        if data == '# #': # 아무것도 없을때
            return None
        
        nodes = data.split()
        root = treenode(int(nodes[1])) # nodes[0] = #
        queue = collections.deque([root])
        index = 2
        # 빠른 러너처럼 자식 노드 결과 먼저 확인 휴 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#': # 왼쪽 자식 처리
                node.left = treenode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#': # 오른쪽 자식 처리
                node.right = treenode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root

# 48. 균형 이진 트리
# 높이 균형은 모든 노드의 서브트리 간의 높이 차이가 1 이하
class solution_48:
    def is_balanced(self, root : treenode):
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            # 높이 차이가 나는 경우 -1(끝까지 -1 리턴), 이외에는 높이에 따라 1증가
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            else:
                return max(left, right) + 1
        
        return check(root) != -1


n1 = treenode(1)
n2 = treenode(2)
n3 = treenode(2)
n4 = treenode(3)
n5 = treenode(3)
n6 = treenode(4)
n7 = treenode(4)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n4.left = n6
n4.right = n7
sol = solution_48()
print(sol.is_balanced(n1))

# 49. 최소 높이 트리
# 노드 개수와 무방향 그래프를 입력받아 트리가 최소 높이가 되는 루트의 목록
# 리턴하라
class solution_49:
    def find_min_height_trees(self, n, edges):
        if n <= 1:
            return [0]
        
        # 양반향 그래프 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을 때 까지 반복 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

class solution_50:
    def sorted_arr_to_bst(self, nums):
        if not nums:
            return None
    
        # 중앙값 인덱스
        mid = len(nums) // 2

        # 분할 정복으로 이진 검색 결과 트리 구성
        node = treenode(nums[id])
        node.left = self.sorted_arr_to_bst(nums[:id])
        node.right = self.sorted_arr_to_bst(nums[id+1:])

        return node


