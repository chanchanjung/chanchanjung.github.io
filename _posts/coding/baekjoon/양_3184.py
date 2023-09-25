import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

yards = [list(sys.stdin.readline().strip()) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]
queue = deque()

sheeps, wolves = 0, 0

def bfs(queue, animals, visited):
    global yards, n, m
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        now = queue.pop()
        for d in range(4):
            if -1 < now[0] + dx[d] < n and -1 < now[1] + dy[d] < m:
                if visited[now[0] + dx[d]][now[1] + dy[d]] == 0:
                    visited[now[0] + dx[d]][now[1] + dy[d]] = 1
                    if yards[now[0] + dx[d]][now[1] + dy[d]] == 'v':
                        animals[1] += 1
                        queue.append([now[0] + dx[d], now[1] + dy[d]])
                    elif yards[now[0] + dx[d]][now[1] + dy[d]] == 'o':
                        animals[0] += 1 
                        queue.append([now[0] + dx[d], now[1] + dy[d]])
                    elif yards[now[0] + dx[d]][now[1] + dy[d]] == '.':
                        queue.append([now[0] + dx[d], now[1] + dy[d]])
    return animals, visited



for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            if yards[i][j] == 'v':
                queue.append([i, j])
                visited[i][j] = 1
                animals, visited = bfs(queue, [0, 1], visited)
                if animals[0] > animals[1]:
                    sheeps += animals[0]
                else:
                    wolves += animals[1]
            elif yards[i][j] == 'o':
                queue.append([i, j])
                visited[i][j] = 1
                animals, visited = bfs(queue, [1, 0], visited)
                if animals[0] > animals[1]:
                    sheeps += animals[0]
                else:
                    wolves += animals[1]
            elif yards[i][j] == '#':
                visited[i][j] = 1
            



print(sheeps, wolves)