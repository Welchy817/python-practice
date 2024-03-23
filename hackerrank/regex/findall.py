# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = input()
regex = r"(?<=[qwrtypsdfghjklzxcvbnm])([AEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnm])"
vowels = re.findall(regex, S, re.IGNORECASE)
if vowels:
    print(*vowels, sep='\n')
else:
    print(-1)