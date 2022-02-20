# def binary_search(arr, target):
#     start = 0
#     end = len(arr) - 1
#     if target > arr[end]:
#         return end + 1
#
#     while start < end:
#         mid = (start + end) // 2
#
#         if arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid
#
#     return end
#
# # test = [1,3,5,7,9,11,13]
# # for x in range(15):
# #     print(x, end=' ')
# #     print(binary_search_2(test, x))
# n = int(input())
# min_list = []
# max_list = []
# test_list = []
# for _ in range(n):
#     a, b = map(int, input().split())
#     min_list.append(a-b)
#     max_list.append(a+b)
#     test_list.append((a-b, a+b))
#
# min_list.sort()
# max_list.sort()
#
# for min_num, max_num in test_list:
#     # 시작점 인덱스
#     min_index = binary_search(max_list, min_num)
#
#     max_index = binary_search(min_list, max_num + 1)
#
#     print(min_index + 1, max_index)



def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid

    return end


n = int(input())
num_list = []
test_list = []
for i in range(n):
    a, b = map(int, input().split())
    num_list.append(a-b)
    num_list.append(a+b)
    test_list.append((a-b, a+b))

num_list.sort()

end_index = len(num_list)
for min_num, max_num in test_list:
    # 시작점 인덱스
    min_index = binary_search(num_list, min_num)
    # 거꾸로 확인
    max_index = binary_search(num_list, max_num+1)
    print(binary_search(num_list, 95+1)//2 + 1)
    min_index = min_index // 2 + 1
    max_index = max_index // 2 + 1
    print(min_index, max_index)