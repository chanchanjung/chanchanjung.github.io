from heapq import heappush, heappop

def solution(k, dungeons):
    answer = 0
    queue = []
    for idx, dungeon in enumerate(dungeons):
        visited = [0 for _ in range(len(dungeons))]
        if k >= dungeon[0]:
            visited[idx] = 1
            heappush(queue, (-1, k-dungeon[1], visited))
    

    while queue:
        count, hp, visited = heappop(queue)
        inDungeon = False
        for idx, dungeon in enumerate(dungeons):
            if visited[idx] == 0 and hp >= dungeon[0]:
                inDungeon = True
                next_visited = visited[:]
                next_visited[idx] = 1
                heappush(queue, (count-1, hp-dungeon[1], next_visited))
        if not inDungeon:
            answer = max(answer, abs(count))
    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))