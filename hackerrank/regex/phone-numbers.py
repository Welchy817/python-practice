# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
for numbers in range(N):
    num = input()
    if re.search(r"(^[7|8|9][0-9]{9}$)", num):
        print("YES")
    else:
        print("NO")