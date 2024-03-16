# Enter your code here. Read input from STDIN. Print output to STDOUT
length = list(map(int, input().split()))
N = list(map(int, input().split()))
like = set(map(int, input().split()))
dislike = set(map(int, input().split()))
happiness = 0

for i in N:
    if i in like:
        happiness += 1
    elif i in dislike:
        happiness -= 1

print(happiness)