# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

K = int(input())
roomNum = list(map(int, input().split()))
roomNum = sorted(roomNum)
captain = Counter(roomNum)
print(captain.most_common().pop()[0])