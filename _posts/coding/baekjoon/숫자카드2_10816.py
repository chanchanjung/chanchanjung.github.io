import sys
from collections import defaultdict

sys.stdin.readline()

num_dict = defaultdict(int)

for num in map(int, sys.stdin.readline().strip().split()):
    num_dict[num] += 1

answer_list = []
sys.stdin.readline()
for num in map(int, sys.stdin.readline().strip().split()):
    answer_list.append(num_dict[num])

print(*answer_list)