# 도영이가 만든 맛있는 음식
# 재료가 n 개
# 신맛 S, 쓴 맛 B
# 만든 음식의 신맛은 S들의 곱
# 쓴 맛은 합
# 신 맛과 쓴 맛의 차이를 가장 작게 만들기
import sys

input = sys.stdin.readline

n = int(input())
# 재료 주어짐
bitter = []
sour = []
for i in range(n):
    a, b = map(int, input().split())
    sour.append(a)
    bitter.append(b)

ans = 10 ** 10
for i in range(1, 1 << n):
    #print(bin(i))
    temp_sour = 1  # 곱
    temp_bitter = 0  # 합
    for j in range(n):
        if i & (1 << j):
            #print("이 자리가 1이네요?")
            temp_sour = temp_sour * sour[j]
            temp_bitter = temp_bitter + bitter[j]
        else:
            #print("이 자리는 0이네요?")
            continue
    #print(temp_sour, temp_bitter)
    temp_diff = abs(temp_sour - temp_bitter)
    if temp_diff < ans:
        ans = temp_diff

print(ans)
