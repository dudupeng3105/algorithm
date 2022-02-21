# stack 이라는 자료 구조
# 내가 정의 하는 ADT
class Stack:

    # stack이 최초 생성 될때 필요한 정보들
    # stack의 크기를 기본 값으로 받아와야 한다.
    def __init__(self, size):
        # stack의 크기
        self.size = size
        # stack을 저장할 자료 구조
        # 최초 stack 생성시 각 위치에는 값이 없다.
        self.arr = [None] * size # [0, 0, 0, 0] X
        # stack의 최상단
        self.top = -1

    # stack이 비어있는지 확인
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.top == self.size - 1:
            return True
        else:
            return False

    # stack의 추가 연산 == push
    # top 위치에 값을 입력
    def push(self, n):
        # 어디에?
        self.top += 1
        self.arr[self.top] = n

    def pop(self):
        if not self.is_empty():
            result = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return result
        else:
            raise IndexError('범위를 벗어남')

s1 = Stack(5)
print(s1.arr)
print(s1.size)
print(s1.top)
print('='*30)

s1.push('A')
print(s1.top)
s1.push('B')
print(s1.top)
s1.push('C')
print(s1.top)
s1.push('D')
print(s1.top)
s1.push('E')
print(s1.top)
print(s1.arr)
print(s1.is_full())
print(s1.is_empty())
print('='*30)
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.arr)