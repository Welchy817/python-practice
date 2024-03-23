# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
T = int(input())
for n in range(T):
    N = input()
    print(bool(re.search(r"^([\+\-]?\d*[.]\d+)$", N)))