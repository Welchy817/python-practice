# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

S = input()
groups = groupby(S)
for group, num in groups:
    print(f"({len(list(num))}, {group})", end=" ")