import sys
from collections import deque


def bfs(): 
    global display_clip_map
    q = deque()
    q.append([1, 0])
    display_clip_map[1][0] = 0 # [1][0] 화면 이모티콘수, 클립보드 수 / value -> 걸리는 시간

    while q:
        display, clip = q.popleft()

        if display == S:
            print(display_clip_map[display][clip])            
            return

        for action in range(3):
            if action == 0:
                if display_clip_map[display][display] == -1:  # 클립보드에 저장
                    display_clip_map[display][display] = display_clip_map[display][clip] + 1
                    q.append([display, display])
                    continue
                else:
                    continue

            elif action == 1: # 클립보드 개수만큼 화면에 붙이기                
                if display + clip < S + 10 and display_clip_map[display + clip][clip] == -1:
                    display_clip_map[display + clip][clip] = display_clip_map[display][clip] +1
                    q.append([display + clip, clip])
                    continue
                else:
                    continue

            else: # 화면에서 이모티콘 한 개 삭제                
                if display -1 > 0 and display_clip_map[display -1][clip] == -1:
                    display_clip_map[display -1][clip] = display_clip_map[display][clip] +1
                    q.append([display -1, clip])
                    continue                    
                else:
                    continue


S = int(sys.stdin.readline())
display_clip_map = [[-1 for _ in range(S+10)] for __ in range(S+10)]
bfs()
