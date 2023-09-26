import sys



def bfs(banners, stack, M, N):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    while stack:
        x, y = stack.pop()
        for d in range(8):
            if -1 < x + dx[d] < M and -1 < y + dy[d] < N:
                if banners[x + dx[d]][y + dy[d]] == 1:
                    banners[x + dx[d]][y + dy[d]] = 0
                    stack.append((x + dx[d], y + dy[d]))
    return banners



M, N = map(int, sys.stdin.readline().strip().split())

banners = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

answer = 0
stack = []

for x in range(M):
    for y in range(N):
        if banners[x][y] == 1:
            stack.append((x, y))
            banners[x][y] = 0
            answer += 1
            banners = bfs(banners, stack, M, N)

print(answer)
