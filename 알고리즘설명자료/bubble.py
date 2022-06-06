def bubble_sort(arr):
    length = len(arr) - 1
    for i in range(length, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def counting_sort(arr):
    length = len(set(arr))
    length_b = len(arr)
    count_arr = [0 for _ in range(length)]
    result = [0 for _ in range(length_b)]
    # 카운팅
    for num in arr:
        count_arr[num] += 1
    # 누적
    for i in range(1, length):
        count_arr[i] += count_arr[i-1]

    for i in range(length_b-1, -1, -1):
        count_arr[arr[i]] -= 1
        result[count_arr[arr[i]]] = arr[i]

    return result


test = [55, 7, 78, 12, 42]
print(bubble_sort(test))

count_test = [0, 4, 1, 3, 1, 2, 4, 1]
print(counting_sort(count_test))
