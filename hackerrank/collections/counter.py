# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = int(input())
shoe_sizes = list(map(int, input().split()))
size_counter = Counter(shoe_sizes)
earned = 0
for customers in range(int(input())):
    size, price = list(map(int, input().split()))
    if size in size_counter.keys() and size_counter[size] > 0:
        earned += price
        size_counter[size] -= 1
        
print(earned)