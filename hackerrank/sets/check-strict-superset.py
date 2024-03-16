# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
superset = True
for i in range(int(input())):
    N = set(map(int, input().split()))
    if not N.issubset(A):
        superset = False
        
print(superset)