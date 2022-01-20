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


nums = [2,7,11,15]
target = 26
print(two_sum(nums, target))
# 7-2 in을 이용한 탐색
# 모든 조합을 비교하지 않고 정답, 즉 타겟에서 첫 번째 값을 뺀 값 target - n 이 존재
# 하는지 탐색
# in 연산이 비교 연산보다 빠름 / 시간복잡도는 차이안나지만 상수항에서 차이가 조금 있음
def two_sum_2(nums, target):
    for i, n in enumerate(nums):
        complement = target -n

        if complement in nums[i + 1:]:
            return [i, nums[i+1:].index(complement) + (i+1)]


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
    for i, num in enumerate(nums): # 딕셔너리라 있을 때 바로 조회 가능
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target-num]]


print(two_sum_3(nums, target))

# 7-4 조회 구선 개선
# 좀더 간결하게
# 평균적으로 조회 O(1), 전체는 O(n)
def two_sum_4(nums, target):
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]
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
