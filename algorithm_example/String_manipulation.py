# 1. 유효한 팰린드롬
import collections


# 뒤집어도 같은 말이 되는 단어
# 1-1 리스트로 변환 : 304 ms


def ispalindrom(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:  # 1개 남았을 때는 안함
        # print(strs)
        if strs.pop(0) != strs.pop():  # pop 하면서 양쪽 끝에 하나씩 총 2개 빠짐
            return False

    return True


# 1-2 데크 자료형을 이용한 최적화
# 리스트 pop(0)는 O(n)
# 데크의 popleft() O(1) 이기 때문

def ispalindrom_deque(s: str) -> bool:  # 64ms
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


# 1-3 슬라이싱 사용 # 36ms
import re


def ispalindrom_slicing(s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]  # 거꾸로한거랑 맞는지 비교


# s = input()
# print(ispalindrom(s))
# print(ispalindrom_deque(s))
# print(ispalindrom_slicing(s))

# 2. 문자열 뒤집기
# 2-1 투 포인터를 이용한 스왑
# 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식
def reverseString(s):  # 216ms
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


s = ['h', 'e', 'l', 'l', 'o']
print(reverseString(s))


# 2-2 파이썬다운 방식
# s.reverse()  # 208ms

# 3. 로그파일 재정렬
# 로그의 가장 앞 부분은 식별자
# 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 숫자 로그는 입력 순서대로 한다.
# 3-1 람다와 연산자를 이용
def reorder_log_files(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(reorder_log_files(logs))

# 4. 가장 흔한 단어
paragraph = "Bob hit a ball, the hit BALL flew after it was hit."
banned = ["hit"]


# 4 - 1. 리스트 컴프리헨션, Counter 객체 사용
def most_common_word(para, ban):
    words = [word for word in re.sub(r'[^a-zA-Z0-9]', ' ', para).lower().split()
             if word not in ban]

    counts = collections.Counter(words)

    return counts


result = most_common_word(paragraph, banned)
print(result.most_common(1))  # 이러면 키랑 밸류 보임
print(result.most_common(1)[0][0])

# 5. 그룹 애너그램
# 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
given_input = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']


# 5-1 정렬하여 딕셔너리에 추가


def group_anagrams(s):
    anagrams = collections.defaultdict(list)

    for word in s:
        print(word)
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)  # anagrams['key'].append(value)
    print(anagrams)
    return list(anagrams.values())


result = group_anagrams(given_input)
print(result)


# 6 가장 긴 팰린드롬 부분 문자열

# 6 - 1 중앙을 중심으로 확장하는 풀이
# longest common substing (LCS)
# 투포인터 사용

def longest_palindrome(s):
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left, right):
        print(left, right)
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        print(s[left + 1:right])
        return s[left + 1:right]  # left + 1 ~ right - 1

    # 해당사항 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len)
    return result


print(longest_palindrome('babadnannan'))
