import sys
from collections import deque

N = int(sys.stdin.readline())

r1, c1, r2, c2 = map(int, sys.stdin.readline().strip().split())

queue = deque()

queue.append((r1, c1))

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]
visited = [[-1 for _ in range(N)] for _ in range(N)]
visited[r1][c1] = 0

answer = -1
while queue:
    r, c = queue.pop()
    for d in range(6):
        
        if -1 < r + dr[d] < N and -1 < c + dc[d] < N:
            if r + dr[d] == r2 and c + dc[d] == c2:
                if answer == -1 or answer > visited[r][c] + 1:
                    answer = visited[r][c] + 1
                
            if visited[r + dr[d]][c + dc[d]] == -1 or visited[r + dr[d]][c + dc[d]] > 1 + visited[r][c]:
                visited[r + dr[d]][c + dc[d]] = 1 + visited[r][c]
                queue.append((r + dr[d], c + dc[d]))
print(answer)


