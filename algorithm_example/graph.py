from typing import List
# 32 섬의 개수
# 1을 육지로, 0을 물로 가정 2D 그리드맵
# 섬의 개수 구해라 -> 1덩어리
class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
        # 더 이상 땅이 아닌 경우 종료
        # 2d 맵 벋어날 때
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != 1:
                return
            
            grid[i][j] = 0  # 탐색된 곳은 바다로 만들어버림
                            # 다음 번 섬 탐색 시 무시하려고
            #동서남북 탐색
            dfs(i + 1, j) # 동
            dfs(i - 1, j) # 서
            dfs(i, j + 1) # 남
            dfs(i, j - 1) # 북

        ## 실행 코드
        count = 0
        for i in range(len(grid)): # 행 개수 만큼 반복            
            for j in range(len(grid[0])): # 열 개수 만큼 반복                
                if grid[i][j] == 1:
                    dfs(i, j) # 처음 들어갈때 1 있는데부터 들감
                    # 모든 육지 탐색 후 카운트 1 증가
                    # 탐험하고 오면 섬 한개가 바다가 되서 다음 for문에는 
                    # 무조건 다른 섬이 걸림
                    count += 1
        return count

given_map = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
sol = Solution()
print(sol.num_islands(given_map))

# 33. 전화 번호 문자 조합
# 2~9까지 숫자가 주어졌을 때 전화번호로 조합 가능한 문자
class Solution_33:
    def letter_combinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            #끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return
            
            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        # 예외 처리
        if not digits:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                "6": "mno", "7":"pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result
    

sol = Solution_33()
print(sol.letter_combinations("23"))

# 34-1 순열
class Solution_34:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일 때 추가
            if len(elements) == 0:
                results.append(prev_elements[:])
            
            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results

# itertools  이용
import itertools
def permute(self, nums:List[int]) -> List[int]:
    return list(itertools.permutations(nums))

# 35 조합(combinations)
class Solutions_35:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k-1)
                elements.pop()

        dfs([], 1, k) # 1부터 시작
        return results

sol = Solutions_35()
print(sol.combine(5, 2))

def combin(self, n: int, k: int) -> List[List[int]]:
    return list(itertools.combinations(range(1, n+1), k)) # 1~N 에서 k 에 뽑는 조합

class Solution_36:
    def combinationSum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 자신 부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result

sol = Solution_36()
print(sol.combinationSum([2, 3, 6, 7], 7))

# 37 부분 집합
class Solution_37:
    def subsets(self, nums:List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            # 매번 결과 추가
            result.append(path)

            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])
            
        dfs(0, [])
        return result

sol = Solution_37()
print(sol.subsets([1,2,3]))
