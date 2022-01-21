# 연결리스트 PRACTICE
# 13. 연결리스트가 팰린드롬 구조인지 판별하라
# input 1->2 / false
# input 1->2->2->1 / true
# 13 - 1 리스트 변환
# 앞 뒤 모두 추출할 수 있는 자료구조 필요
# Definition for singly-linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    # 모든 노드 값 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next



def isPalindrome(head):
    q = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.data)
        node = node.next
    # q에 linked_list value 다 추가함 --> list 로 변환
    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():  #q.pop(0) 맨 앞에 가져오는데 O(n)임
            # 하나 꺼내오면 나머지 다 시프팅 해야되서
            return False

    return True


given_linked_list = LinkedList(1)
given_linked_list.append(2)
given_linked_list.append(2)
given_linked_list.append(1)
#given_linked_list.print_all()
print(isPalindrome(given_linked_list.head))

# 13 - 2 데크를 이용한 최적화
# 파이썬 데크는 이중 연결 리스트 구조로 양쪽 방향 모두 추출하는데 시간 O(1)
import collections
def is_palindrome(head):
    # 데크 자료형 선언
    q = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.data)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():  # 덱은 이중연결리스트이므로 Q(1)
            return False

    return True


given_linked_list = LinkedList(1)
given_linked_list.append(2)
given_linked_list.append(3)
given_linked_list.append(2)
given_linked_list.append(1)
#given_linked_list.print_all()
print(is_palindrome(given_linked_list.head))


def is_palindrome_2(head):
    rev = None
    slow = fast = head
    print(head.next)
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    # 팰린드롬 여부 확인
    while rev and rev.data == slow.data:
        slow, rev = slow.next, rev.next
    return not rev

print(is_palindrome_2(given_linked_list.head))

# 14 두 정렬 리스트의 병합