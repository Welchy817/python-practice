# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
for index in range(N):
    line = input()
    if re.search(r"(?<=\s)([&]{2})(?=\s)", line):
        line = re.sub(r"(?<=\s)([&]{2})(?=\s)", "and", line)
    if re.search(r"(?<=\s)([|]{2})(?=\s)", line):
        line = re.sub(r"(?<=\s)([|]{2})(?=\s)", "or", line)
    print(line)