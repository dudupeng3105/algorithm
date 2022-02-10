class BinaryHeap(object):
    def __init__(self):
        self.items = [None]
    
    def __len__(self):
        return len(self.items) - 1
    
    # 삽입 시 실행, 반복 구조 구현
    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0:
            if self.items[i] < self.itmes[parent]:
                self.items[parent], self.items[i] = \
                    self.items[i], self.items[parent]

            i = parent
            parent = i // 2
    
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    # 추출 시 실행, 재귀 구조 구현
    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right
        
        # 위에 둘 중에 하나라도 걸리면 idx가 달라지므로 재귀가 더 들어감
        # 들어가기전에 스왑 그래서 제자리까지 찾아감
        if smallest != idx:
            self.items[idx], self.items[smallest] = \
                self.items[smallest], self.items[idx]
            self._percolate_down(smallest)

    def extract(self):
        extracted = self.items[1] # 뺄꺼니까 저장해둠
        self.items[1] = self.items[len(self)] # root와 마지막 node change
        self.items.pop() # 이게 마지막 노드를 뺌 (저장해뒀음)
        self._percolate_down(1)
        return extracted

# 문제 55
# 정렬되지 않은 배열에서 k 번째 큰 요소를 추출하라
# [3,2,3,1,2,4,,5,5,6], k = 4
# output = 4
# 1. heapq 모듈 사용
import heapq
from typing import List
class Solution_55:
    def findKthLargest(self, nums: List[int], k:int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n) # 파이썬이 최소힙만 지원하기 때문
        
        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)


lst = [3,2,3,1,2,4,5,5,6]
k = 4
sol = Solution_55()
print(sol.findKthLargest(lst, k))
# 2. heapq의 heapify 사용
class Solution_55_2:
    def findKthLargest(self, nums: List[int], k:int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
# 3. heapq의 nlargest 사용
class Solution_55_3:
    def findKthLargest(self, nums: List[int], k:int) -> int:
        return heapq.nlargest(k, nums)[-1]
# 4. 정렬을 이용한 풀이
class Solution_55_4:
    def findKthLargest(self, nums: List[int], k:int) -> int:
        return sorted(nums, reverse=True)[k - 1]