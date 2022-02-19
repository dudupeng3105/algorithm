import sys

sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    given_lst = input()
    bar_start = []
    cut_pieces = 0
    i = 0
    while i < len(given_lst):
        if given_lst[i] == ')':  # 바 종료
            bar_start.pop()  # 하나 꺼냄

        if given_lst[i] == '(':
            if given_lst[i + 1] == ')':  # 레이저
                cut_pieces += len(bar_start)  # 아직 안끝난 바개수만큼 더해줌
                i += 1
            else:  # 바 시작임
                cut_pieces += 1  # 조각이 하나 생기는 거임
                bar_start.append('(')

        i += 1

    print(f'#{tc} {cut_pieces}')
