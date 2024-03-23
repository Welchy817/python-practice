# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()

matches = re.search(r"([a-zA-Z0-9])\1+", S)
if matches:
    print(matches.group(1))
else:
    print(-1)