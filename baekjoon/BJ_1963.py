import sys
from collections import deque

input = sys.stdin.readline


def prime_list():
    for i in range(2, 100):
        # 소수인 상태에서 소수의 배수를 체크해줘야 함
        if prime_truth[i]:
            # 소수의 배수 체크
            for j in range(2 * i, 10000, i):
                prime_truth[j] = False


def bfs(start_num):
    q = deque()
    q.append((start_num, 0))  # a, cnt, path

    visited = [False for i in range(10000)]
    visited[start_num] = True

    while q:
        prime, cnt = q.popleft()
        prime_str = str(prime)
        for digit in range(4):
            # print(digit_num)
            for i in range(10):
                next_prime = int(prime_str[:digit] + str(i) + prime_str[digit + 1:])
                if visited[next_prime] == 0 and prime_truth[next_prime] and next_prime >=1000:
                    if next_prime == b:
                        return cnt + 1
                    visited[next_prime] = True
                    q.append((next_prime, cnt + 1))

    return "Impossible"


# print(prime_lst)
test_case = int(input())
prime_truth = [True for _ in range(10000)]
prime_list()
for _ in range(test_case):
    a, b = map(int, input().split())
    if a == b:
        print(0)
    else:
        print(bfs(a))
