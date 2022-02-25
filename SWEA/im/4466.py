import sys
sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case+1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    max_score_sum = sum(scores[:k])
    print(f"#{tc} {max_score_sum}")