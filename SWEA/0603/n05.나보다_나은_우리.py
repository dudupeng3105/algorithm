from itertools import combinations

for tc in range(50):
    n = int(input())
    ans = input().rstrip()
    student_ans = [[] for _ in range(n)]
    for i in range(n):
        student_submit = input().rstrip()
        for j in range(len(ans)):
            if student_submit[j] == ans[j]:
                student_ans[i].append(j)

    test_set = set([i for i in range(len(ans))])

    flag = 0
    for r in range(1, n+1):
        for combi in combinations(student_ans, r):
            sum_set = set()
            for c in combi:
                sum_set.update(c)
            if sum_set == test_set:
                flag = 1
                break
        if flag:
            break

    if flag:
        print(r)
    else:
        print(-1)

    if tc == 49:
        pass
    else:
        dump = input()