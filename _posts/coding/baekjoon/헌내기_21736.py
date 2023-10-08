import sys

def dfs(campus, stack, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    while stack:
        now = stack.pop()
        for d in range(4):
            if -1 < now[0] + dx[d] < N and -1 < now[1] + dy[d] < M:
                if campus[now[0] + dx[d]][now[1] + dy[d]] == 'O':
                    stack.append((now[0] + dx[d], now[1] + dy[d]))
                elif campus[now[0] + dx[d]][now[1] + dy[d]] == 'P':
                    count += 1
                    stack.append((now[0] + dx[d], now[1] + dy[d]))
                campus[now[0] + dx[d]][now[1] + dy[d]] = 'X'
    if count > 0:
        print(count)
    else:
        print("TT")


N, M = map(int, sys.stdin.readline().strip().split())

campus = [list(sys.stdin.readline().strip())  for _ in range(N)]

findI = False
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            findI = True
            campus[i][j] = 'X'
            dfs(campus, [(i, j)], N, M)
    if findI:
        break
