# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())

for colors in range(N):
    line = input()
    colors = re.findall(r"((?<!^)#(?:[a-f0-9]{6}|[a-f0-9]{3})(?!$))", line, re.IGNORECASE)
    if colors:
        for color in colors:
            print(color)