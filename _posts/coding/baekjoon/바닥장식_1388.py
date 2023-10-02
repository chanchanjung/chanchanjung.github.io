import sys

N, M = map(int, sys.stdin.readline().strip().split())
floors = [list(sys.stdin.readline().strip()) for _ in range(N)]
answer = 0

def bfs_hori(floors, queue, M):
    dy = [-1, 1]
    while queue:
        x, y = queue.pop()
        for d in range(2):
            if -1 < y + dy[d] < M:
                if floors[x][y + dy[d]] == '-':
                    floors[x][y + dy[d]] = '.'
                    queue.append((x, y + dy[d]))



def bfs_ver(floors, queue, N):
    dx = [-1, 1]
    while queue:
        x, y = queue.pop()
        for d in range(2):
            if -1 < x + dx[d] < N:
                if floors[x + dx[d]][y] == '|':
                    floors[x + dx[d]][y] = '.'
                    queue.append((x + dx[d], y))
    

for i in range(N):
    for j in range(M):
        if floors[i][j] == '-':
            floors[i][j] = '.'
            bfs_hori(floors, [(i, j)], M)
            answer += 1
        elif floors[i][j] == '|':
            floors[i][j] = '.'
            bfs_ver(floors, [(i, j)], N)
            answer += 1

print(answer)