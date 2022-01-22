# # 연결리스트를 이용한 스택 ADT 구현
# class Node:
#     def __init__(self, item, next):
#         self.item = item
#         self.next = next
#
#
# class Stack:
#     def __init__(self):
#         self.last = None
#
#     def push(self, item):
#         self.last = Node(item, self.last)
#
#     def pop(self):
#         item = self.last.item
#         self.last = self.last.next
#         return item
#
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
#
# for _ in range(5):
#     print(stack.pop())
#
# # 20 유효한 괄호
# # 괄호로 된 입력값이 올바른지 판별
# # input = ()[]{}
# # true
#
# def is_valid(s):
#     stack = []
#     table = {
#         ')': '(',
#         '}': '{',
#         ']': '[',
#     }
#
#     # 스택 이용 예외 처리 및 일치 여부 판별
#     for char in s:
#         if char not in table:
#             stack.append(char)
#         elif not stack or table[char] != stack.pop():
#             return False
#
#     return len(stack) == 0
#
#
# print(is_valid('()[]{}'))
#
# # 21. 중복된 문자를 제외하고 사전식 순서로 나열
# # input 'bcabc'
# # output 'abc'
# # 21-1 재귀를 이용한 분리
# given_str = 'cbacdcbc'
#
#
# def remove_duplicate_letters(s):
#     # 집합으로 정렬
#     print(sorted(set(s)))
#     for char in sorted(set(s)):
#         suffix = s[s.index(char):]
#         print(suffix)
#         # 전체 집합과 접미사 집합이 일치할때 분리 진행
#         print(f'set(s){set(s)} set(suffix){set(suffix)}')
#         if set(s) == set(suffix):
#             print('true')
#             return char + remove_duplicate_letters(suffix.replace(char, ""))
#     return ""


#print(remove_duplicate_letters(given_str))

import collections

given_str = 'cbacdcbc'
# 21-2 스택을 이용한 문자 제거
def remove_duplicate_letters(s):
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        #print(counter)
        if char in seen:
            continue
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        #print(f'seen: {seen}, stack: {stack}, char: {char}')
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            # char < char(=stack[-1]) 비교됨
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)


print(remove_duplicate_letters(given_str))

# 며칠 뒤에 더 따뜻한 날이 될까
T = [73, 74, 75, 71, 69, 72, 76, 73]
def dailyTemperatures(T):
    answer = [0] * len(T)
    stack = [] # 인덱스 담는 스택
    for i, cur in enumerate(T):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur > T[stack[-1]]:
            last = stack.pop()  # 스택 최상단 인덱스
            answer[last] = i - last # 날짜 차이
        stack.append(i)

    return answer

print(dailyTemperatures(T))

# 23 큐를 이용한 스택 구현
class Mystack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) -1):
            self.q.append(self.q.popleft()) # 앞에있던거 꺼내서 다시 뒤에 올림

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

stack = Mystack()
stack.push(1)
stack.push(1)
print(stack.top())
print(stack.pop())
print(stack.empty())


# 24 스택을 이용한 큐 구현
class MyQueue:
    def __init__(self):
        self.input = [] # 스택 1
        self.output = [] # 스택 2

    def push(self, x):
        self.input.append(x) # 인풋 스택에 append

    def pop(self): # 조회하고 pop
        self.peek()
        return self.output.pop()

    def peek(self):
        # output이 없으면 모두 재입력
        if not self.output: # 어차피 역순이기 떄문에 맨위에꺼 조회하면 peek 맞음
            while self.input:
                self.output.append(self.input.pop()) # 이러면 역순으로 쌓임
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


# 25 원형 큐 디자인인
# circular queue
class my_circular_queue:
    def __init__(self, k):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0  # front pointer
        self.p2 = 0  # rear pointer

    # enQueue(): 리어 포인터 이동
    def enQueue(self, value):
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    # deQueue() : 프론트 포인터 이동
    def deQueue(self): # 값 가져오진 않고 삭제만
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self):
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None