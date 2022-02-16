import sys

sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1,test_case+1):
    p = list(input())
    p = p[::-1]
    print(f'#{tc}', end=' ')
    print(*p, sep='')