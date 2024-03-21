# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

K, M = map(int, input().split())
max_value = 0
k_lines = []
for i in range(K):
    k_lines.append(list(map(int, input().split()))[1:])
    
for maximum in product(*k_lines):
    if sum(list(map(lambda x: x ** 2, maximum)))% M > max_value:
        max_value = sum(list(map(lambda x: x ** 2, maximum)))% M
print(max_value)