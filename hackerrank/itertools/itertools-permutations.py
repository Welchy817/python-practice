# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
S, k = input().split()
perm = sorted(list(permutations(S, int(k))))
for i in perm:
    print("".join(i))