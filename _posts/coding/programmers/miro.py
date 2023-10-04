from heapq import heappop, heappush



def solution(maps):
    answer = 0
    miro = [list(map) for map in maps]
    N = len(miro)
    M = len(miro[0])
    min_miro = [[float('inf') for _ in range(M)] for _ in range(N)]
    start = (0, 0)
    laver = (0, 0)
    end = (0, 0)
    for i in range(N):
        for j in range(M):
            if miro[i][j] == 'S':
                start = (i, j)
            elif miro[i][j] == 'L':
                laver = (i, j)
            elif miro[i][j] == 'E':
                end = (i, j)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = []
    heappush(queue, (0, start))
    min_miro[start[0]][start[1]] = 0
    while queue:
        current_distance, current_node = heappop(queue)
        x, y = current_node
        if min_miro[x][y] < current_distance:
            continue

        for d in range(4):
            if -1 < x + dx[d] < N and -1 < y + dy[d] < M:
                if miro[x + dx[d]][y + dy[d]] != 'X':
                    if min_miro[x + dx[d]][y + dy[d]] > current_distance + 1:
                        min_miro[x + dx[d]][y + dy[d]] = current_distance + 1
                        heappush(queue, (current_distance + 1, (x + dx[d], y + dy[d])))
    
    if min_miro[laver[0]][laver[1]] == float('inf'):
        return -1
    
    answer = min_miro[laver[0]][laver[1]]

    queue = []
    heappush(queue, (0, laver))
    min_miro = [[float('inf') for _ in range(M)] for _ in range(N)]
    min_miro[laver[0]][laver[1]] = 0
    while queue:
        current_distance, current_node = heappop(queue)
        x, y = current_node
        if min_miro[x][y] < current_distance:
            continue

        for d in range(4):
            if -1 < x + dx[d] < N and -1 < y + dy[d] < M:
                if miro[x + dx[d]][y + dy[d]] != 'X':
                    if min_miro[x + dx[d]][y + dy[d]] > current_distance + 1:
                        min_miro[x + dx[d]][y + dy[d]] = current_distance + 1
                        heappush(queue, (current_distance + 1, (x + dx[d], y + dy[d])))
    
    if min_miro[end[0]][end[1]] == float('inf'):
        return -1
    
    answer += min_miro[end[0]][end[1]]

    return answer



print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))