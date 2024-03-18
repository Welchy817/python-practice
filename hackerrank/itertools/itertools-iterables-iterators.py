# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

N = int(input())
n = input().split()
K = int(input())
elements = list(combinations(n, K))
count = 0
for element in elements:
    if 'a' in element:
        count += 1
print(count/len(elements))