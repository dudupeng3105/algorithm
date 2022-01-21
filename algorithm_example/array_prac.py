# 7장 배열
# 7 두수의 합
# input : nums = [2,7,11,15], target = 9
# output : [0, 1]
# nums[0] + nums[1] = 9
# 7-1 브루트 포스 풀이(비효율)
# O(n^2)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 26
print(two_sum(nums, target))


# 7-2 in을 이용한 탐색
# 모든 조합을 비교하지 않고 정답, 즉 타겟에서 첫 번째 값을 뺀 값 target - n 이 존재
# 하는지 탐색
# in 연산이 비교 연산보다 빠름 / 시간복잡도는 차이안나지만 상수항에서 차이가 조금 있음
def two_sum_2(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [i, nums[i + 1:].index(complement) + (i + 1)]


print(two_sum_2(nums, target))


# 7-3 첫 번째 수를 뺀 결과 키 조회
# 시간 복잡도 개선
# 평균적으로 조회 O(1), 전체는 O(n)
def two_sum_3(nums, target):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리에 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺸 결과를 키로 조회
    for i, num in enumerate(nums):  # 딕셔너리라 있을 때 바로 조회 가능
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


print(two_sum_3(nums, target))


# 7-4 조회 구선 개선
# 좀더 간결하게
# 평균적으로 조회 O(1), 전체는 O(n)
def two_sum_4(nums, target):
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


# 7-5 투포인터 사용
# 왼쪽 포인터와 오른쪽 포인터의 합이
# 타켓보다 크면 오른쪽 포인터를 왼쪽으로
# 작다면 왼쪽포인터를 오른쪽으로 옮기며 조절
# 정렬이 되있어야
# O(n)
# 정렬하면 인덱스를 알 수 없어 곤란
def two_sum_5(nums, target):
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:  # 타겟이랑 같으면
            return [left, right]


# 8 빗물 트래핑
# 높이를 입력받아 얼마나 많은 물이 쌓일 수 있는지 계산
# input : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# output : 6
# 8 - 1 투포인터를 최대로 이동
# O(n)
def trap(height):
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), \
                              max(height[right], right_max)
        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume


height_list = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height_list))


# 8 - 2  스택 쌓기
# O(n)
# 현재 높이가 이전 높이보다 높을 때, 즉 꺾이는 부분 변곡점 기준으로 격차만큼
# volume을 채움
def trap_1(height):
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume


print(trap_1(height_list))

# 9 세 수의 합
# 입력
# nums = [-1, 0, 1, 2, -1, -4]
# output== [[-1, 0, 1],[-1, -1, 2]]
# 브루트 포스로 계산
# O(n^2) 까지 줄여보자

def three_sum(nums):
    results = []
    nums.sort()

    # 브루트 포스 n^3 반복
    for i in range(len(nums) -2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1, len(nums)):
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])

    return results


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))


# 투 포인터로 합 계산
def three_sum_2(nums):
    results = []
    nums.sort()

    for i in range(len(nums) -2):
        # 중복된 값 건너 뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # 간격을 좁혀가며 합 'sum' 계산
        left, right = i + 1, len(nums) -1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # 'sum = 0'인 경우이므로 정답 및 스킵 처리
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results

print(three_sum_2(nums))

# 10 배열 파티션 1
# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라
# input : [1, 4, 3, 2]
# output : 4
# n은 2가 되고 최대합은 4 / min(1,2) + min(3,4) = 4

# 10-1 오름차순 풀이
def array_pair_sum(nums):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


nums = [1, 4, 3, 2]
print(array_pair_sum(nums))

# 10-2 짝수 번째 값 계산
# 다 더할 필요없고 짝수 번쨰 값만 더하면 될 것 같다
def array_pair_sum_2(nums):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n

    return sum


print(array_pair_sum_2(nums))


# 10-3 파이써닉한 방식
# sum(sorted(num)[::2])

# 11 자신을 제외한 배열의 곱
# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의
# 곱셈 결과가 되도록 출력
# input : [1, 2, 3, 4]
# output : [24, 12, 8, 6]
# 나눗셈을 하지 않고 O(n) 풀이
# 11 - 1 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
def product_except_self(nums):
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
        # [1, 1, 2, 6]
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 갑을 차례대로 곱셈
    for i in range(len(nums) - 1, -1, -1):  # last에서 0까지 역순으로
        out[i] = out[i] * p
        p = p * nums[i]
    return out  #[1*4*3*2, 1*4*3, 2*4, 6]


nums = [1, 2, 3, 4]
print(product_except_self(nums))


# 12 주식을 사고팔기 가장 좋은 시점
# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라
# input : [7, 1, 5, 3, 6, 4]
# output : 5
# 12 - 1 브루트 포스로 계산
# O(n^2)
# 타임아웃임
def max_profit(prices):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price

#
# prices_list = [7, 1, 5, 3, 6, 4]
# print(max_profit(prices_list))

# 12 - 2 저점과 현재 값과의 차이 계산
# 카데인 알고리즘 활용
import sys


def max_porfit_2(prices):
    profit = 0
    min_price = sys.maxsize  # 이래 두면 뭐가 들어와도 바로 체인지됨

    # 최소값과 최대값 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


prices_list = [7, 1, 5, 3, 6, 4]
print(max_porfit_2(prices_list))