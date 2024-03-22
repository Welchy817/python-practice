# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

N = int(input())
d = deque()

for i in range(N):
    action = list(map(str, input().split()))
    cmd = action[0]
    if len(action) > 1:
        val = action[1]
    if cmd == "append":
        d.append(val)
    elif cmd == "appendleft":
        d.appendleft(val)
    elif cmd == "pop":
        d.pop()
    elif cmd == "popleft":
        d.popleft()
        
print(' '.join(d))