import sys

tc_list = []
for _ in range(int(sys.stdin.readline().strip())):
    tc_list.append(int(sys.stdin.readline().strip()))

counts = [(-1, -1) for _ in range(max(tc_list)+1)]
counts[0] = (1, 0)
if len(counts) > 1: 
    counts[1] = (0, 1)

def fibonacci(n):
    global counts
    if n == 0:
        return counts[0]
    elif n == 1:
        return counts[1]
    
    if counts[n] != (-1, -1):
        return counts[n]
    
    count1 = fibonacci(n-1)
    count2 = fibonacci(n-2)
    counts[n] = (count1[0] + count2[0], count1[1] + count2[1])
    return counts[n]

for tc in tc_list:
    print(*fibonacci(tc))
    
