# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n, m = map(int, input().split())
A, B = [], []
b_in_a = defaultdict(list)
for x in range(n):
    A.append(input())
for y in range(m):
    B.append(input())
for b in B:
    if b in A:
        if not b_in_a[b]:
            for a in enumerate(A):
                if b == a[1]:
                    b_in_a[b].append(a[0]+1)
    else:
        b_in_a[b].append(-1)


for indices in B:
    print(' '.join(map(str, b_in_a[indices])))