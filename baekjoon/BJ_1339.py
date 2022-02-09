from collections import defaultdict
N = int(input())
word_lst = []
for _ in range(N):
    given_list = list(input())
    word_lst.append(given_list)

d = defaultdict(int)
for word in word_lst:
    length = len(word)
    for i in range(length):
        if d[word[i]]:
            d[word[i]] += 10**(len(word)-1-i)
        else:
            d[word[i]] = 10**(len(word)-1-i)

s_dict_lst = sorted(d.items(), key=lambda item: item[1], reverse=True)
# 변환 dict 만들기
N = 9 # 9부터 넣음
conversion_dict = defaultdict(str)
for item in s_dict_lst:
    conversion_dict[item[0]] = str(N)
    N -= 1

# word 숫자 합 계산
result = 0
for word in word_lst:
    temp_str = ''
    for w in word:
        temp_str += conversion_dict[w]
    result += int(temp_str)
print(result)






