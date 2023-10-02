import sys


N, M, K = map(int, sys.stdin.readline().strip().split())
trash_list = [[0 for _ in range(M)] for _ in range(N)]
answer = 0

for _ in range(K):
    x, y = map(int, sys.stdin.readline().strip().split())
    trash_list[x-1][y-1] = 1

visited = [[0 for _ in range(M)] for _ in range(N)]


def bfs(trash_list, queue, count, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.pop()
        for d in range(4):
            if -1 < x + dx[d] < N and -1 < y + dy[d] < M:
                if trash_list[x + dx[d]][y + dy[d]] == 1:
                    queue.append((x + dx[d], y + dy[d]))
                    trash_list[x + dx[d]][y + dy[d]] = 0
                    count += 1
    return count


for i in range(N):
    for j in range(M):
        if trash_list[i][j] == 1:
            trash_list[i][j] = 0
            trash_count = bfs(trash_list, [(i, j)], 1, N, M)
            if trash_count > answer:
                answer = trash_count
                
print(answer)