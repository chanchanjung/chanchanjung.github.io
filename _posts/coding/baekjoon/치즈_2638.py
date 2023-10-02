import sys

N, M = map(int, sys.stdin.readline().strip().split())

cheese_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

melt_time = 0
cheese_count = 0
for cheese in cheese_list:
    cheese_count += cheese.count(1)


def bfs(cheese_list, visited, queue, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.pop()
        if x == 0 and y == 0:
            visited[0][0] = 1
        for d in range(4):
            if -1 < x + dx[d] < N and -1 < y + dy[d] < M:
                if cheese_list[x + dx[d]][y + dy[d]] == 0 and visited[x + dx[d]][y + dy[d]] == 0:
                    visited[x + dx[d]][y + dy[d]] = 1
                    queue.append((x + dx[d], y + dy[d]))
                elif cheese_list[x + dx[d]][y + dy[d]] == 1:
                    visited[x + dx[d]][y + dy[d]] += 1
    return visited



    

while cheese_count > 0:
    visited = bfs(
        cheese_list, 
        [[0 for _ in range(M)] for _ in range(N)], 
        [(0, 0)],
        N, M
    )

    for i in range(N):
        for j in range(M):
            if visited[i][j] > 1:
                cheese_list[i][j] = 0
                cheese_count -= 1
    
    melt_time += 1

print(melt_time)

