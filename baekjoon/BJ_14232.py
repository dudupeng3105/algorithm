import sys

input = sys.stdin.readline


# 1.k의 소수 구하기
# 2. 2~마지막 소수 까지 for문 계속 돔
# 3. 2의 반복
# 4. 마지막 소수로도 안나눠지면 자기자신 추가해줌
# 5. 끝
def cal_prime(num):
    end = int(num ** 0.5) + 1
    prime = [True] * end
    # 소수 판별
    for i in range(2, end):
        if prime[i]:
            for j in range(2 * i, end, i):
                prime[j] = False

    return [i for i in range(2, end) if prime[i]]


k = int(input())
prime_lst = cal_prime(k)
result = []

while True:
    flag = 1
    for i in prime_lst:

        if i > k:
            break

        if k % i == 0:
            result.append(i)
            k = k//i
            flag = 0

    if flag:
        if not k == 1:
            result.append(k)
        break

print(len(result))
print(*sorted(result))
