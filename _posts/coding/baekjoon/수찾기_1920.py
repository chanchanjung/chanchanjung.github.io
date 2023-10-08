import sys

sys.stdin.readline()


num_list = list(map(int, sys.stdin.readline().strip().split()))

sys.stdin.readline()
answer_list = list(map(int, sys.stdin.readline().strip().split()))
num_dict = {num: 0 for num in answer_list}

for num in num_list:
    if num in num_dict.keys():
        num_dict[num] = 1

for num in answer_list:
    print(num_dict[num])

