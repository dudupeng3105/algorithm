import random
from collections import defaultdict, deque

# 티미룸 파도타기~
# 대범이는 문제에서 주어지는 이름의 친구의 티미룸을 방문하고 싶다. 하지만 티미룸의 기능 부족으로 이름을 검색한다고
# 해당 유저의 티미룸에는 갈 수 가 없다고 한다. 따라서 대범이는 반드시 파도타기를 이용해서만 친구를 찾아야 한다.
# 대범이에게 유저들의 친구리스트가 주어질 때, 대범이가 친구리스트를 보고 최소 몇 번만에 파도타기를 통해 주어지는
# 이름을 가진 친구의 티미룸으로 갈 수 있는지 구하라.
# 입력으로 맨 처음에 N과 찾고자하는 유저가 주어진다.
# 두번째 줄에는 대범이의 친구리스트가 주어진다.
# 다음 N개의 줄에는 N명의 유저의 친구리스트가 주어진다.
# 서로 친구가 아닐 수 있다.
# 마지막 줄에는 유저의 이름이 주어진다.
# 만약 파도타기로 찾아갈 수 없으면 '티미룸 안써!'라고 출력해주세요


# 테케
# name_list = ['하민', '박지현', '재준', '누리', '윤호준', '제학', '김지현', '상균', '영진', '이호준', '정현', '대영'
#     , '민형', '동욱', '혜라', '지선', '성목', '준식', '효근', '현우']
#
# friends_dict = defaultdict(list)
# target_index = random.randint(4, 20)
# print("타겟 인데스", target_index)
#
# for i in range(target_index+1):
#     friends_dict[name_list[i]] = random.sample(name_list[:target_index+1], random.randint(2, target_index//2))
#     try:
#         friends_dict[name_list[i]].remove(name_list[i])
#     except:
#         pass
#     print(name_list[i], friends_dict[name_list[i]])


f = open('input.txt', 'a')
f.writelines([str(45), '\n'])
for tc in range(1, 46):
    friends_dict = defaultdict(list)
    user_num = random.randint(4, 1000)
    target_index = random.randint(4, user_num)
    print("타겟 인덱스", target_index)
    f.writelines([str(target_index), ' ', str(user_num), '\n'])
    for i in range(1, user_num + 1):
        friends_dict[i] = random.sample([x for x in range(1, user_num + 1)], random.randint(2, target_index // 2))
        try:
            friends_dict[i].remove(i)
        except:
            pass
        print(i, friends_dict[i])
        temp = ''
        for j in range(len(friends_dict[i])):
            temp += (str(friends_dict[i][j]) + ' ')
        temp = temp.rstrip()
        f.writelines([str(i), ' ', temp, '\n'])

    # print(target_index, name_list[target_index])
    # print(0, *friends_dict[0])
    # for i in range(1, user_num):
    #     print(i, *friends_dict[i])


    # 풀이 1(dfs)
    def bfs():
        q = deque()
        visited = [False for _ in range(user_num + 1)]
        q.append((1, 0))  # node, dist
        visited[1] = True
        while q:
            node, dist = q.popleft()
            for next_node in friends_dict[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append((next_node, dist + 1))
                    if next_node == target_index:
                        return dist + 1

        return False


    # main
    ff = open('output.txt', 'a')
    ff.writelines(['#', str(tc), ' '])
    print('타겟 인덱스(유저)', target_index)
    result = bfs()
    print()
    if not result:
        print("티미룸 안써!")
        ff.writelines(["티미룸 안써!", '\n'])
    else:
        print(result)
        ff.writelines([str(result), '\n'])
    ff.close()
f.close()
