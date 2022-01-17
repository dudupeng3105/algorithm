def dfs(elements): # elements = [1,2,3]
    # 리프 노드일 때 결과 추가 --> 트리 맨 밑에 노드 leaf node
    if len(elements) == 0:
        results.append(prev_elements[:])

    # 순열 생성 재귀 호출
    for e in elements: # e = 1
        next_elements = elements[:] # n_e = 1,2,3
        next_elements.remove(e) # n_e = 2, 3

        prev_elements.append(e) # p_e = 1
        dfs(next_elements) # 1 2 3 출력
        prev_elements.pop() #

    return results


results = []
prev_elements = []
nums = [1, 2, 3]
print(dfs(nums))




