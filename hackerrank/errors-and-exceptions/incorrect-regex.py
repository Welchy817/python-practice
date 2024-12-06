import re
n = int(input())
for i in range(n):
    S = input()
    try:
        re.compile(S)
        print(True)
    except re.error:
        print(False)