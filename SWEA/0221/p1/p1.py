from collections import deque


class Mystack:
    def __init__(self):
        self.q = deque()

    def __len__(self):
        return len(self.q)

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


s1 = Mystack()
s1.push(1)
print(s1.top())
s1.push(2)
print(s1.top())
s1.push(3)
print(s1.top())
print('size', len(s1))
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.empty())

