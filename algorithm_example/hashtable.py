import collections

# Definition for singly-linked list
class ListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None


class my_hash_map:
    # 초기화
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # 삽입
    def put(self, key, value):
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입하고 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


# hashmap = my_hash_map()
# hashmap.put(1, 1)  # 키, 밸류
# hashmap.put(2, 2)
# hashmap.put(2, 1)
# hashmap.put(2, 4)
# hashmap.put(2, 5)
# hashmap.remove(2)
# print(hashmap.get(2))  # 1을 리턴
# print(hashmap.get(2))
# print(hashmap.get(1))  # 키
# print(hashmap.get(3))  # 키가 존재하지 않음
# hashmap.put(2, 1)
# hashmap.remove(2) # 키
# print(hashmap.get(2))  # 키가 삭제되어 존재 x

# 29. 보석과 돌
# J = 'aA', S = 'aAAbbbb'
# output 3
# 29-1 해시테이블 이용

def num_jew_in_stone(j, s):
    freqs = {}
    count = 0

    # 돌(S)의 빈도 수 계산
    for char in s:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    # 보석(J)의 빈도 수 합산
    for char in j:
        if char in freqs:
            count += freqs[char]  # a는 1개 A는 2개

    return count



# 29-2 defaultdict를 이용한 비교 생략
def num_jew_in_stone(j,s):
    freqs = collections.defaultdict(int)
    count = 0

    # 비교 없이 돌(S) 빈도 수 계산
    for char in s:
        freqs[char] += 1

    # 비교 없이 보석 빈도 합산
    for char in j:
        count += freqs[char]

    return count

# 29-3 counter 계산 생략

def num_jew_in_stone(j, s):
    freqs = collections.Counter(s) # 돌 빈도수 계산
    count = 0

    for char in j:
        count += freqs[char]

    return count


# 29-4 파이써닉한 방식
def num_jew(j, s):
    return sum(stone in j for stone in s)

# 30 중복 문자 없는 가장 긴 부분 문자열

def length_of_longest_substring(s):
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        # 이미 등장했덩 문자라면 'start' 위치 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1
        else: # 최대 부문 문자열 길이 개ㅑㅇ신
            max_length = max(max_length, index - start + 1)

        # 현재 문자의 위치 삽입
        used[char] = index

# 'abcabcbb'
# 3 ('abc')
# 슬라이딩 윈도우와 투 포인터로 사이즈 조절


# 31 상위 k 빈도 요소
# nums = [1,1,1,2,2,3], k =2
# [1, 2]
# 31-1 Counter를 이용한 음수 순 추출
import heapq
def top_k_frequent(nums, k):
    freqs = collections.Counter(nums)
    freqs_heap = []
    # 힙에 음수로 삽입
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = list()
    # k번 만큼 추출, min heapq이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk


def topKFrequent(nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]




# 31-2 파이썬 다운 방식