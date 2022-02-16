import sys


# KMP 알고리즘
# 필요한 함수 -> 실패함수
# 실패함수 -> prefix와 와 suffix가 일치하는 최대길이
# 실패함수를 통해서 일정 부분의 비교 건너뜀
def failure_function(pattern):
    f = [0]  # 실패함수 초기화
    i = 1
    j = 0
    m = len(pattern)
    while i < m:
        if pattern[i] == pattern[j]:
            f.append(j + 1)  # failure function 값 저장
            i += 1
            j += 1
        elif j > 0:
            j = f[j - 1]  # use failure function to shift pattern
        else:
            f.append(0)  # no match
            i += 1

    return f


def kmp(test, pattern):
    f = failure_function(pattern)
    i = 0
    j = 0
    n = len(test)
    m = len(pattern)
    while i < n:
        if test[i] == pattern[j]:  # pattern match
            if j == m - 1:
                return i - j  # match! -> test에서 패턴의 시작위치 리턴
            else:
                i = i + 1
                j = j + 1
        else:  # 불일치
            if j > 0:  # j가 이동했으면, pattern이 몇 번은 matched
                j = f[j - 1]
            else:  # 첨부터 안맞음
                i = i + 1

    return -1  # No match


sys.stdin = open("test_input.txt", 'rt', encoding='UTF8')

for _ in range(1, 11):
    tc = int(input())
    pattern = list(input())
    pattern_length = len(pattern)
    test = list(input())
    cnt = 0
    index = 0
    while index != -1:
        index = kmp(test, pattern)
        test = test[index + pattern_length:]
        cnt += 1

    print(f'#{tc} {cnt - 1}')  # 마지막꺼는 아니므로 한 개 빼줌
