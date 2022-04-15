# import sys
# input = sys.stdin.readline
#
#
# def check(arr):
#     i = 0
#     len_arr = len(arr)
#     while i < len_arr-1:
#         target = arr[i]
#         len_target = len(arr[i])
#         if arr[i+1][:len_target] == target:
#             return print('NO')
#         i += 1
#     return print('YES')
#
#
# test_case = int(input())
# for _ in range(test_case):
#     n = int(input())
#     arr = []
#
#     for __ in range(n):
#         arr.append(input().rstrip())
#     arr.sort()
#     check(arr)

import sys
import math


class Node:
    def __init__(self, data):
        self.data = data
        self.child = [None for _ in range(10)]
        self.check = False  # 해당 노드를 마지막으로 끝나는 문자열 체크


class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, phone):
        tmp = self.root
        for i in phone:
            if tmp.child[i]:  # 비어있지 않으면
                tmp = tmp.child[i]  # 한 레벨 더내려감
            else:  # 비어 있으면 새로운 노드 만듬
                new = Node(i)
                tmp.child[i] = new
                tmp = new
        tmp.check = True

    def consistency(self, phone):
        tmp = self.root
        for i in range(len(phone)):
            if tmp.check:  # 다른 문자열을포함하고 있다면
                # 내려가고있던 길에 더 빨리 끝난 문자열이 있으면 포함한 것
                return False
            tmp = tmp.child[phone[i]]  # 같은문자를 따라 내려감감
        return True


for _ in range(int(input())):
    n = int(input())
    phone_list = []
    trie = Trie()

    for _ in range(n):
        phone = list(map(int, input().split()))
        trie.insert(phone)
        phone_list.append(phone)
    result = True

    for p in phone_list:
        result *= trie.consistency(p)

    if result:
        print("YES")
    else:
        print("NO")


def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True