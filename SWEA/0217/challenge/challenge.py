import random


def binary_search(target, list):
    start = 0
    end = len(list)
    cnt = 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            return mid, cnt
        elif list[mid] > target:
            end = mid - 1
        else:  # target > list[mid]
            start = mid + 1
        cnt += 1

    return None, cnt


M = 4
teammates = ['권나은', '김동욱', '서상균', '이호준']
problems = [4861, 1216]
problem_dict = {'4861': '회문_1', '1216': '회문_2'}
N = [random.randint(-2000, 7000) for _ in range(M*M)]
num_list = []

for problem in problems:
    random_index = random.randint(0, M*M-1)
    num_list.append(random_index)
    N[random_index] = problem

N.sort()
print(N)

for problem in problems:
    index, search_cnt = binary_search(problem, N)
    #print(index, search_cnt)
    temp = index + search_cnt
    print(f'{teammates[temp%4]}님이 {problem_dict[str(problem)]}발표를 하겠습니다.')


