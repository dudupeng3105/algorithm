import sys

sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    n, k = map(int, input().split())
    students_set = set(range(1, n + 1))
    good_students = set(map(int, input().split()))
    result = list(students_set - good_students)
    print(f"#{tc}", *result)
