# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

S, k = input().split()
S = sorted(S)
combos = list()
for i in range(1, int(k)+1):
    combos += (list(combinations(S, i)))
    
for combo in combos:
    print("".join(combo))