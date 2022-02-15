import sys


def bs(left, right, want_page):
    global cnt
    c = (left+right)//2
    if want_page > c:
        cnt += 1
        bs(c, right, want_page)
    elif want_page < c:
        cnt += 1
        bs(left, c, want_page)
    else:  # 같으면
        return cnt

    return cnt


sys.stdin = open("input.txt")

testcase = int(input())
for tc in range(1, testcase + 1):
    num_page, a_page, b_page = map(int, input().split())
    cnt = 1
    a_cnt = bs(1, num_page, a_page)
    cnt = 1
    b_cnt = bs(1, num_page, b_page)
    if a_cnt < b_cnt:
        print(f'#{tc} A')
    elif a_cnt > b_cnt:
        print(f'#{tc} B')
    else:  # 무승부
        print(f'#{tc} 0')