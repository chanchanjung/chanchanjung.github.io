import sys


N = int(sys.stdin.readline().strip())
if N == 1:
    print(1)
else:
    num_list = [num for num in range(1, N+1)]
    n = N % 2 == 1
    while len(num_list) > 1:
        num_list = [num for idx, num in enumerate(num_list) if idx % 2 == 1]
        # print(n, num_list)
        if n:
            num_list = num_list[1:] + [num_list[0]]
            
        n = len(num_list) % 2 == 1
        

    print(*num_list)
