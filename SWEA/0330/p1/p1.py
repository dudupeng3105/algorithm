def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        #print(smaller, equal, larger)
        return quicksort(smaller) + equal + quicksort(larger)


test_case = int(input())
for tc in range(test_case):
    unsorted_list = list(map(int, input().split()))
    print(quicksort(unsorted_list))