# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

T = int(input())

for i in range(T):
    stack = []
    n = int(input())
    cube = deque(list(map(int, input().split())))
    for j in range(n-1):
        right = cube.pop()
        left = cube.popleft()
        if not stack:
            if right > left:
                stack.append(right)
                cube.appendleft(left)
            elif left >= right:
                stack.append(left)
                cube.append(right)
        elif stack[j-1] < right or stack[j-1] < left:
            break
        elif right > left:
            stack.append(right)
            cube.appendleft(left)
        elif left >= right:
            stack.append(left)
            cube.append(right)
        if j == n-2:
            if right > left:
                stack.append(left)
            else:
                stack.append(right)
    if len(stack) == n:
        print("Yes")
    elif len(stack) < n:
        print("No")