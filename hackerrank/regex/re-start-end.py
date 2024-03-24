# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = input()
k = input()

pattern = re.compile(k)
regex = pattern.search(S)
if not regex:
    print("(-1, -1)")
while regex:
    print("({0}, {1})".format(regex.start(), regex.end() - 1))
    regex = pattern.search(S, regex.start() + 1)