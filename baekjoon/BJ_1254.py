import sys

input = sys.stdin.readline

s = input().rstrip()

# 투포인터 비스무리하게 품
end = len(s) - 1
end_char = s[end]
start = 0
ans = 2 * end + 1
for i in range(len(s) - 1):
    # 시작이 끝과 같아야한다
    end = len(s) - 1
    if s[i] == end_char:
        start = i
        temp_len = end - start + 1
        flag = 1
        while start < end:
            start += 1
            end -= 1
            if s[start] == s[end]:
                continue
            else:
                flag = 0  # 실패
                break

        if flag:
            ans = 2 * len(s) - temp_len
            break
print(ans)
