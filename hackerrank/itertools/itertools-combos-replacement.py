# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

S, k = input().split()
S = sorted(S)
combos = list(combinations_with_replacement(S, int(k)))
for combo in combos:
    print("".join(combo))