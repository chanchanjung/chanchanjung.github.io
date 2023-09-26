import sys

M, N = map(int, sys.stdin.readline().strip().split())

cheese = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

cheese_count = 0
melt_time = 0
for m in range(M):
    cheese_count += cheese[m].count(1)


def dfs(cheese, stack, M, N):
    visited = [[0 for _ in range(N)] for _ in range(M)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    melt_count = 0
    while stack:
        x,y = stack.pop()
        visited[x][y] = 1
        
        for d in range(4):
            if -1 < x + dx[d] < M and -1 < y + dy[d] < N:
                if cheese[x + dx[d]][y + dy[d]] == 0 and visited[x + dx[d]][y + dy[d]] == 0:
                    stack.append((x + dx[d], y + dy[d]))
                elif cheese[x + dx[d]][y + dy[d]] == 1:
                    cheese[x + dx[d]][y + dy[d]] = 2
                    melt_count += 1
        
    return melt_count

                
while True:
    melt_count = dfs(cheese, [(0, 0)], M, N)
    for ci in range(M):
        for cj in range(N):
            if cheese[ci][cj] == 2:
                cheese[ci][cj] = 0
    melt_time += 1
    if cheese_count - melt_count == 0:
        print(melt_time)
        print(cheese_count)
        break
    else:
        cheese_count -= melt_count
            


