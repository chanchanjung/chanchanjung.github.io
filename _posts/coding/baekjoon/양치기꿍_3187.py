import sys

R, C = map(int, sys.stdin.readline().strip().split())

farm = [list(sys.stdin.readline().strip()) for _ in range(R)]

visited = [[0 for _ in range(C)] for _ in range(R)]
sheep = 0
wolf = 0

def bfs(farm, visited, queue, R, C):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    s_count = 0
    w_count = 0
    while queue:
        x, y = queue.pop()
        if farm[x][y] == 'v':
            w_count += 1
        elif farm[x][y] == 'k':
            s_count += 1
        for d in range(4):
            if -1 < x + dx[d] < R and -1 < y + dy[d] < C:
                if visited[x + dx[d]][y + dy[d]] == 0:
                    visited[x + dx[d]][y + dy[d]] = 1
                    if farm[x + dx[d]][y + dy[d]] != '#':
                        queue.append((x + dx[d], y + dy[d]))
    if s_count > w_count:
        return visited, s_count, 0
    return visited, 0, w_count


for i in range(R):
    for j in range(C):
        if visited[i][j] == 0:
            visited[i][j] = 1
            if farm[i][j] != '#':
                visited, now_sheep, now_wolf = bfs(farm, visited, [(i, j)], R, C)
                sheep += now_sheep
                wolf += now_wolf
print(sheep, wolf)