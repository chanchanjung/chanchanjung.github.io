import sys

max_n = 0
max_k = 0
tc_list = []
for _ in range(int(sys.stdin.readline().strip())):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    if n > max_n:
        max_n = n
    if k > max_k:
        max_k = k
    tc_list.append((k, n))

rooms = {j : [i+1 if j == 0 else 1 if i == 0 else 0 for i in range(max_n)] for j in range(max_k+1)}

def dp(i, j):
    global rooms
    # if j == 1:
    #     return rooms[i][j-1]
    if i == 0 or j ==  1:
        return rooms[i][j-1]
    if rooms[i][j-1] > 0:
        return rooms[i][j-1]
    rooms[i][j-1] = dp(i,j-1) + dp(i-1,j)
    return rooms[i][j-1]
    

for tc in tc_list:
    print(dp(tc[0], tc[1]))
