import time


def dfs(element, subset, sum_subset):
    global cnt
    cnt += 1
    if sum_subset > 10:
        return
    if sum_subset == 10:
        print(subset)
        return

    for i in range(element + 1, 11):  # 2, 11
        subset.append(i)
        next_elements = i
        dfs(next_elements, subset, sum_subset+i)
        subset.pop()

    return


def dfs_2(element, subset):
    global cnt
    cnt += 1
    if sum(subset) > 10:
        return
    if sum(subset) == 10:
        print(subset)
        return

    for i in range(element + 1, 11):  # 2, 11
        subset.append(i)
        next_elements = i
        dfs_2(next_elements, subset)
        subset.pop()

    return


def dfs_3(element, subset):
    global cnt
    cnt += 1
    if sum(subset) > 10:
        return
    if sum(subset) == 10:
        print(subset)
        return

    for i in range(len(element)):  # 1~10, 2~10
        subset.append(element[i])
        next_elements = element[i+1:]
        dfs_3(next_elements, subset)
        subset.pop()

    return


def dfs_4(element, subset, sum_subset):
    global cnt
    cnt += 1
    if sum_subset > 10:
        return
    if sum_subset == 10:
        print(subset)
        return

    for i in range(len(element)):  # 1~10, 2~10
        subset.append(element[i])
        next_elements = element[i+1:]
        dfs_4(next_elements, subset, sum_subset + element[i])
        subset.pop()

    return


cnt = 0
start = time.time()
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dfs(0, [], 0)
print(cnt)
print(f"time:{time.time() - start: 0.10f}")

cnt = 0
start = time.time()
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dfs_2(0, [])
print(cnt)
print(f"time:{time.time() - start: 0.10f}")

cnt = 0
start = time.time()
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dfs_3(num_list, [])
print(cnt)
print(f"time:{time.time() - start: 0.10f}")

cnt = 0
start = time.time()
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dfs_4(num_list, [], 0)
print(cnt)
print(f"time:{time.time() - start: 0.10f}")

# sum을 매번하는거보다 sum을 저장하는 변수를 하나 쓰는게 더빠름
# 리스트를 shallow copy 하는거 보다 시작점 넘겨주는게 더 빠름